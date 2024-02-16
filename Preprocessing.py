import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the CSV file
file_path = '/Users/charles/Desktop/TENNIS/Data'
csv_file = 'AllResults.csv'  # Replace 'your_file_name.csv' with the actual file name
full_path = f'{file_path}/{csv_file}'

# Read CSV into a pandas DataFrame
tennis_data = pd.read_csv(full_path)

# Drop specified columns
columns_to_drop = ['winner_seed', 'loser_seed', 'winner_entry', 'loser_entry', 'minutes', 'winner_ioc', 'score']
tennis_data = tennis_data.drop(columns=columns_to_drop, axis=1)

# Remove rows with missing values
tennis_data_cleaned = tennis_data.dropna()

# Rearrange columns
tennis_data_cleaned = tennis_data_cleaned[['winner_name', 'winner_id', 'loser_name', 'loser_id'] + [col for col in tennis_data_cleaned if col not in ['winner_name', 'winner_id', 'loser_name', 'loser_id']]]

# Save the preprocessed DataFrame to a new CSV file
preprocessed_file_name = csv_file.replace('.csv', '_preprocessed.csv')
preprocessed_full_path = f'{file_path}/{preprocessed_file_name}'
tennis_data_cleaned.to_csv(preprocessed_full_path, index=False)

# Display the cleaned and preprocessed DataFrame
print("Cleaned and Preprocessed DataFrame:")
print(tennis_data_cleaned)
print(f"Preprocessed DataFrame saved to: {preprocessed_full_path}")


# Feature Engineering (e.g., one-hot encoding for surface and winner_hand)
tennis_data_cleaned = pd.get_dummies(tennis_data_cleaned, columns=['surface', 'winner_hand'])

# Label encode categorical columns (e.g., 'round', 'score')
label_encoder = LabelEncoder()
tennis_data_cleaned['round'] = label_encoder.fit_transform(tennis_data_cleaned['round'])
# You may need a similar process for the 'score' column depending on your specific use case.

# Date Handling
tennis_data_cleaned['tourney_date'] = pd.to_datetime(tennis_data_cleaned['tourney_date'], format='%Y%m%d')

# Target Variable (e.g., binary outcome indicating whether the player of interest won)
tennis_data_cleaned['target'] = (tennis_data_cleaned['winner_id'] == 100644).astype(int)

# Train-Test Split
X = tennis_data_cleaned.drop(columns=['target'])
y = tennis_data_cleaned['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the preprocessed DataFrame to a new CSV file
preprocessed_file_name = csv_file.replace('.csv', '_preprocessed.csv')
preprocessed_full_path = f'{file_path}/{preprocessed_file_name}'
tennis_data_cleaned.to_csv(preprocessed_full_path, index=False)

# Display the cleaned and preprocessed DataFrame
print("Cleaned and Preprocessed DataFrame Downloaded")
print(tennis_data_cleaned)
