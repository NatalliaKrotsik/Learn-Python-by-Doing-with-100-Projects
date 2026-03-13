import os
import dropbox
import dotenv

dotenv.load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

d = dropbox.Dropbox(ACCESS_TOKEN)

filepath = 'ocean.png'

with open(filepath, 'rb') as file:
    content = file.read()
    d.files_upload(content, f'/{filepath}', mode=dropbox.files.WriteMode('overwrite'))
    print(f'Uploaded {filepath}')


