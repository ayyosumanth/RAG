import pandas as pd
import numpy as np

# Read the uploaded datasets to understand the structure
company_df = pd.read_csv('NewCompanyDATAset.csv')
financial_df = pd.read_csv('msme_financial_data.csv')

print("Company Dataset Shape:", company_df.shape)
print("\nCompany Dataset Columns:")
print(company_df.columns.tolist())
print("\nFirst few rows of Company Dataset:")
print(company_df.head())

print("\n" + "="*50)

print("Financial Dataset Shape:", financial_df.shape)
print("\nFinancial Dataset Columns:")
print(financial_df.columns.tolist())
print("\nFirst few rows of Financial Dataset:")
print(financial_df.head())