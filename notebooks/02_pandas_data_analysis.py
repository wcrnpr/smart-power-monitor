import pandas as pd

# สร้างข้อมูลจำลองแทน CSV
data = {
    "appliance": ["washing_machine", "washing_machine", "standby", "standby", "washing_machine"],
    "current_rms": [2.34, 2.35, 0.12, None, 2.36]
}

df = pd.DataFrame(data)

# เช็ค NaN
print("NaN count:")
print(df.isnull().sum())

# แทนค่า NaN ด้วยค่าเฉลี่ย
df["current_rms"] = df["current_rms"].fillna(df["current_rms"].mean())

# หาค่าเฉลี่ยแยกตาม Appliance
result = df.groupby("appliance")["current_rms"].mean()
print("\nMean current_rms by appliance:")
print(result)