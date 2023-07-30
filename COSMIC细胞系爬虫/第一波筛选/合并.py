import os
import pandas as pd
folder_path = "C:\\Users\\XXX\\Desktop\\XXX\\爬虫\\第一波筛选"
os.chdir("C:\\Users\\XXX\\Desktop\\XXX\\爬虫\\第一波筛选")
cwd = os.getcwd()
print(cwd)
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
combined_data = pd.DataFrame()
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    data = pd.read_csv(file_path) 
    combined_data = pd.concat([combined_data, data], ignore_index=True)
output_file = "COSMIC_all_cell_lines.csv"
combined_data.to_csv(output_file, index=False)
