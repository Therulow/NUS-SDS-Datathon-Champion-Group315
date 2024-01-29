# Model
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import missingno as msno
import datetime

# Data Processing 

# Drop columns
columns_to_drop = ['AccountID','Square Footage','Import/Export Status', 'Fiscal Year End','Company Description']
data = data.drop(columns = columns_to_drop)

# Calculate age of company
current_year = datetime.date.today().year
data.insert(loc = 5, column = 'Age', value = None)
data['Age'] = current_year - data['Year Found']
data = data.drop(columns = 'Year Found')

# Drop columns
columns_to_drop = ['Company', 'Parent Company', 'Global Ultimate Company', 'Domestic Ultimate Company']
data = data.drop(columns = columns_to_drop)

# Deal with missing values
data = data.dropna(subset=['8-Digit SIC Description', 'Parent Country', 'Employees (Domestic Ultimate Total)', 'Employees (Global Ultimate Total)', 'Global Ultimate Country', 'LATITUDE', 'LONGITUDE', 'Age'])     

# Replace NaNs in 'Employees (Single Site)' with median
single_site_employees_median = data['Employees (Single Site)'].median(skipna=True)
data['Employees (Single Site)'] = data['Employees (Single Site)'].fillna(single_site_employees_median)
data.isna().sum()

# Separate features and target variable
X = data.drop(['Sales (Domestic Ultimate Total USD)', 'NEC', 'Industry', '8-Digit SIC Code', '8-Digit SIC Description','Parent Country', 'Ownership Type', 'Company Status (Active/Inactive)', 'Global Ultimate Country', 'Is Domestic Ultimate', 'Is Global Ultimate', 'Entity Type'], axis=1)
Y = data['Sales (Domestic Ultimate Total USD)']

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize the GradientBoostingRegressor
model = GradientBoostingRegressor(random_state=42)

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize the GradientBoostingRegressor
model = GradientBoostingRegressor(random_state=42)

# Prediction 
