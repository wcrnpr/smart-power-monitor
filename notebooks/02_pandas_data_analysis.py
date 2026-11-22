import pandas as pd

# Create synthetic data in place of loading a CSV file.
data = {
    "appliance": ["washing_machine", "washing_machine", "standby", "standby", "washing_machine"],
    "current_rms": [2.34, 2.35, 0.12, None, 2.36]
}

df = pd.DataFrame(data)

# Count missing values in each column.
print("NaN count:")
print(df.isnull().sum())

# Fill missing RMS current values with the overall column mean.
df["current_rms"] = df["current_rms"].fillna(df["current_rms"].mean())

# Calculate mean RMS current for each appliance label.
result = df.groupby("appliance")["current_rms"].mean()
print("\nMean current_rms by appliance:")
print(result)