import pandas as pd

# Load Dataset
dataset = pd.read_excel("dataset/eamcet_dataset.xlsx")

def predict_colleges(rank, category, gender, branch, location):
    category_col = f"{category} {gender.upper()}"  # Example: 'OC BOYS'
    
    filtered_df = dataset[
        (dataset["Branch Code"] == branch) & 
        (dataset["Place"] == location) & 
        (dataset[category_col] >= rank)
    ]
    
    colleges = filtered_df["Institute Name"].unique().tolist()
    
    return colleges[:5]  # Return top 5 unique colleges
