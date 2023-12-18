import pandas as pd
from fuzzywuzzy import fuzz

# Step 1: Read the CSV file
input_file = 'test1.csv'
output_file = 'test2.csv'
df = pd.read_csv(input_file)

# Step 2: Create a temporary DataFrame 'temp1'
temp1 = df.copy()
temp1['Sl_No'] = temp1.index + 1
temp1['Fuzzy_Group_Id'] = 0

# Step 3: Insert data into 'temp1' with Sl_No and initial Fuzzy_Group_Id
temp1['Fuzzy_Group_Id'] = temp1.index + 1

# Step 4: Update 'temp1' based on Levenshtein similarity
for i, row1 in temp1.iterrows():
    for j, row2 in temp1.iterrows():
        if i != j:
            similarity = fuzz.ratio(row1['Vendor_Legal_Name'], row2['Vendor_Legal_Name']) / 100.0
            if similarity >= 0.57:
                temp1.at[i, 'Fuzzy_Group_Id'] = temp1.at[j, 'Fuzzy_Group_Id']

# Step 5: Export 'temp1' to 'test2.csv'
temp1.to_csv(output_file, index=False)

# Print 'temp1' for reference (optional)
print(temp1)
