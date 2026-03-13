import os
import re

directory = 'documents'

filenames = os.listdir(directory)

all_emails = []
for filename in filenames:
    filepath = os.path.join(directory, filename)
    with open(filepath) as file:
        content = file.read()

    pattern = '[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, content)
    all_emails.extend(emails)


print(all_emails)


