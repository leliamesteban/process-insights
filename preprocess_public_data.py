import pandas as pd

# Load public dataset (example: sales data from Kaggle)
# Adjust the file path and dataset accordingly
data = pd.read_csv('public_sales_data.csv')

# Preprocess to fit required format
# Assume the dataset has columns: 'OrderID', 'OrderDate', 'Product', 'Category', 'Amount'
# Rename and select necessary columns
data = data.rename(columns={
    'OrderID': 'order_id',
    'OrderDate': 'date',
    'Product': 'activity',
    'Amount': 'sales'
})

# Add synthetic 'resource' column for the sake of the example
data['resource'] = np.random.choice(['System', 'User A', 'User B', 'User C'], size=len(data))

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Save cleaned data
data.to_csv('cleaned_sales_data.csv', index=False)

# Display the first few rows
print(data.head())
