# Clean and prepare the dataset

# Convert 'orderdate' to datetime
df['orderdate'] = pd.to_datetime(df['orderdate'])

# Create a new 'MonthYear' column
df['MonthYear'] = df['orderdate'].dt.strftime('%b %Y')

# Rename columns for Power BI readability
df.rename(columns={
    'territory': 'Region',
    'productline': 'Category',
    'orderdate': 'Order Date',
    'sales': 'Sales'
}, inplace=True)

# Select only relevant columns for dashboard
dashboard_df = df[['Order Date', 'MonthYear', 'Region', 'Category', 'Sales']]

# Save the cleaned version
cleaned_path = "/mnt/data/cleaned_sales_dashboard.csv"
dashboard_df.to_csv(cleaned_path, index=False)

cleaned_path
