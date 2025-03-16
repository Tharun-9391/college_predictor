# Engineering Admission Predictor  

An AI-powered web application designed to predict engineering college admissions based on entrance scores, category, and extracurricular participation.  

## Overview  
Admission prediction is crucial for students aiming to secure a seat in their preferred engineering colleges. This project leverages **machine learning** to analyze past admission trends and predict the top 5 suitable colleges based on user input.  

## Methodology  
The system utilizes **Flask** for the backend and a **machine learning model** trained on historical admission data to predict the best-fit colleges. The user inputs their entrance exam rank, category, and extracurricular details, and the model returns the top predicted colleges and branches.  

## Data Source  
The dataset used for training the model consists of historical admission records, including **rank, category, and college cutoffs**. The data is cleaned, preprocessed, and structured to train an accurate prediction model.  

## Model Architecture  
The **machine learning model** is built using **Scikit-Learn**, employing algorithms like **KNN, Decision Trees, and Random Forest** for prediction. The model is trained and tested on the admission dataset, and the best-performing algorithm is used for final predictions.  

## Tech Stack  
- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **Database:** SQLite  
- **Machine Learning:** Scikit-Learn, Pandas, NumPy  

## Performance Evaluation  
The model's accuracy is evaluated using performance metrics like **F1-score, accuracy, and confusion matrix**. The results indicate that the model effectively learns admission trends and provides useful recommendations.  

## Future Enhancements  
While the model performs well on historical data, real-world admission predictions can be influenced by several factors such as **policy changes, new seat allocations, and reservation policies**. Future improvements may include:  
- **Integration of real-time admission data** from official sources.  
- **Incorporating additional features** like college reviews, faculty quality, and placements.  
- **Deploying the model on cloud platforms** for better scalability and accessibility.  

## Applications  
This admission predictor can be used in multiple scenarios, such as:  
- **Guidance for students** on college selection.  
- **Automated career counseling systems** for academic institutions.  
- **Analysis of admission trends** for education policymakers.  

## Installation  

To set up and run the project locally, follow these steps:  

### Clone the Repository  
```bash  
git clone https://github.com/Tharun-9391/Tharun-9391.git  
cd Tharun-9391  
```  

### Set Up Virtual Environment  
```bash  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```  

### Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Set Up the Database  
```bash  
python setup_db.py  # Creates the SQLite database and required tables  
```  

### Run the Flask App  
```bash  
python app.py  
```  
Now, open your browser and go to **`http://127.0.0.1:5000/`** to use the application. 🎉  

## Project Structure  
```
 admission-predictor  
│──  static        # CSS, images, JavaScript files  
│──  templates     # HTML templates  
│── app.py          # Main Flask application  
│── model.py        # ML model training script  
│── setup_db.py     # Database setup script  
│── requirements.txt # Dependencies  
│── README.md       # Documentation  
```  

 

