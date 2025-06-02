import pandas as pd
import os

# Use the absolute path to the CSV file
csv_path = r"C:\Users\lauri\Documents\Cours\ELISA 4\Machine learning\Projet\PlanCrash\Data_Project_02\project_02.csv"

# Load the CSV
df = pd.read_csv(csv_path, encoding='latin1', engine='python', quotechar='"', on_bad_lines='warn')
print(df.head())

# Fill missing values with 'NaN'
df['Country/Region'].fillna('NaN', inplace=True)
df['Operator'].fillna('NaN', inplace=True)

# Display the first few rows of the modified dataframe
print("Cleaned DataFrame:")
print(df.head())

# Save the cleaned dataset to a new CSV file
cleaned_csv_path = r"C:\Users\lauri\Documents\Cours\ELISA 4\Machine learning\Projet\PlanCrash\Data_Project_02\cleaned_project_02.csv"
df.to_csv(cleaned_csv_path, index=False)

print(f"Cleaned dataset saved to {cleaned_csv_path}")