# Clean the datasets and prepare them for the RAG system
# Clean company dataset
company_df = company_df.drop(['Unnamed: 28', 'Unnamed: 29'], axis=1, errors='ignore')

# Check for unique sectors and companies
print("Unique Sectors:", company_df['Sector'].unique())
print("Number of companies:", len(company_df))

# Sample financial data for a few companies
print("\nSample companies with financial data:")
sample_companies = ['MSME001', 'MSME010', 'MSME020', 'MSME030', 'MSME040']
for company in sample_companies:
    if company in financial_df['Company_ID'].values:
        company_info = company_df[company_df['Company_ID'] == company]
        if not company_info.empty:
            print(f"{company}: {company_info['Company_Name'].iloc[0]} - {company_info['Sector'].iloc[0]}")

# Save cleaned datasets
company_df.to_csv('cleaned_companies.csv', index=False)
financial_df.to_csv('cleaned_financial.csv', index=False)

print("\nDatasets cleaned and saved!")