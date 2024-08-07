import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Parameters for data generation
num_records = 1000
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
activities = ['Order Placed', 'Order Confirmed', 'Order Shipped', 'Order Delivered']
resources = ['System', 'User A', 'User B', 'User C']
categories = ['Electronics', 'Clothing', 'Home', 'Beauty']

# Generate synthetic data
data = {
    'order_id': np.random.randint(1000, 2000, size=num_records),
    'date': [random_date(start_date, end_date) for _ in range(num_records)],
    'activity': [random.choice(activities) for _ in range(num_records)],
    'resource': [random.choice(resources) for _ in range(num_records)],
    'category': [random.choice(categories) for _ in range(num_records)],
    'sales': np.random.uniform(10.0, 1000.0, size=num_records)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sales_data.csv', index=False)

# Display the first few rows
print(df.head())
