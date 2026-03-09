import os
from datetime import datetime

directory = 'files'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)

    current_time = datetime.now().strftime("%Y-%m-%d")

    new_filename = f'{filename[:-4]}-{current_time}.txt'

    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
    print('File renaming completed.')






