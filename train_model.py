import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("mobile_data.csv")

X = df[['ScreenTime', 'AppUsage', 'SocialMediaTime', 'SleepHours']]
y = df['Addicted']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("mobile_model.pkl", "wb"))

print("Model trained and saved!")