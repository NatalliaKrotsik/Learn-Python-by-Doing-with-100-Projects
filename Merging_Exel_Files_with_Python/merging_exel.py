import pandas as pd
import os

directory = 'excel_files'

filenames = os.listdir(directory)
filepaths = [os.path.join(directory, filename) for filename in filenames]

dataframes = [pd.read_excel(filepath) for filepath in filepaths]

merged_df = pd.concat(dataframes, ignore_index=True)
merged_df.to_excel(os.path.join(directory, 'merged.xlsx'))




