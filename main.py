import pandas as pd
import glob

# Get the list of all CSV files in the directory
csv_files = glob.glob("./*.csv")

# Initialize an empty list to hold DataFrames
data_frames = []

# Loop through the list of CSV files and read each into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    data_frames.append(df)

# Use pandas' concat function to merge the DataFrames
merged_df = pd.concat(data_frames, ignore_index=True, sort=False)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("./merged_file.csv", index=False)

