from flask import Flask, render_template, request, redirect, session,flash
import sqlite3
import pandas as pd

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

# Load college dataset
df = pd.read_excel("dataset/eamcet_dataset.xlsx")
df.columns = df.columns.str.strip().str.replace("\n", " ").str.replace("\r", "")  # Remove extra spaces and newlines


# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect("users.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Register Route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        conn.execute("PRAGMA journal_mode=WAL;")  # ✅ Enables write-ahead logging
        cursor = conn.cursor()

        # ✅ Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Username already exists!")  # ✅ Show error if username exists
            conn.close()
            return redirect("/register")

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Registration successful! You can now log in.")  # ✅ Success message
        except sqlite3.Error as e:
            conn.rollback()
            flash(f"Database Error: {e}")  # ✅ Show DB error if any
        finally:
            cursor.close()
            conn.close()  # ✅ Ensure database is closed

        return redirect("/login")

    return render_template("register.html")

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            session["user"] = username  # ✅ Store session data
            return redirect("/predict")  # ✅ Redirect to predict page after login
        else:
            flash("Invalid username or password!")  # ✅ Flash message for invalid credentials
            return redirect("/login")  # ✅ Redirect back to login page
    
    return render_template("login.html")



@app.route('/users')
def view_users():
    conn = sqlite3.connect('users.db')  # Change to your DB name
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users")  # Fetch user details
    users = cursor.fetchall()
    conn.close()
    
    return render_template('users.html', users=users)



# Prediction Route
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect("/login")  # ✅ Redirect if not logged in
    
    if request.method == "POST":
        category = request.form["category"]
        rank = int(request.form["rank"])

        df = pd.read_excel("dataset/eamcet_dataset.xlsx", engine="openpyxl")  # ✅ Load dataset
        
        # ✅ Filter based on category and rank
        df_filtered = df[df[category] >= rank]  

        # ✅ Get top 5 colleges based on category rank
        predicted_data = df_filtered.nsmallest(5, category)[["Institute Name", "Branch Name"]].drop_duplicates()

        # ✅ Ensure at least 5 colleges are returned
        while len(predicted_data) < 5:
            df_filtered = df[df[category] > rank]  # Get more colleges with slightly higher rank
            extra_data = df_filtered.nsmallest(5 - len(predicted_data), category)[["Institute Name", "Branch Name"]]
            predicted_data = pd.concat([predicted_data, extra_data]).drop_duplicates()

        # ✅ Convert DataFrame to list of tuples (college, branch)
        predicted_colleges = list(predicted_data.itertuples(index=False, name=None))

        return render_template("results.html", colleges=predicted_colleges)

    return render_template("predict.html")




# Logout Route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)