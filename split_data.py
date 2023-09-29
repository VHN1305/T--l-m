import pandas as pd

# Read the data
data = pd.read_csv('data\german_credit_data.csv')

# Split the data into train and test
train = data.sample(frac=0.8, random_state=0)
test = data.drop(train.index)

# Save the data
train.to_csv('data/train.csv', index=False)
test.to_csv('data/test.csv', index=False)

