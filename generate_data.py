import pandas as pd
import numpy as np

# Generate 10,000 patient records
num_patients = 10000
np.random.seed(42)

# Generate Patient IDs
patient_ids = [f'P{str(i).zfill(5)}' for i in range(1, num_patients + 1)]

# Generate Age (18-90)
age = np.random.randint(18, 90, num_patients)

# Generate Gender (Male/Female)
gender = np.random.choice(['Male', 'Female'], num_patients)

# Generate BP (Systolic/Diastolic)
bp_systolic = np.random.randint(90, 180, num_patients)
bp_diastolic = np.random.randint(60, 120, num_patients)

# Generate Sugar Level (Random values in mg/dL)
sugar_level = np.random.randint(70, 250, num_patients)

# Generate Cholesterol Level (mg/dL)
cholesterol = np.random.randint(100, 300, num_patients)

# Generate Haemoglobin Level (g/dL)
haemoglobin = np.round(np.random.uniform(9, 17, num_patients), 1)

# Create DataFrame
df = pd.DataFrame({
    'Patient_ID': patient_ids,
    'Age': age,
    'Gender': gender,
    'BP_Systolic': bp_systolic,
    'BP_Diastolic': bp_diastolic,
    'Sugar_Level': sugar_level,
    'Cholesterol': cholesterol,
    'Haemoglobin': haemoglobin
})

# Save to CSV
df.to_csv('patient_data.csv', index=False)

print("Patient data generated and saved to patient_data.csv")