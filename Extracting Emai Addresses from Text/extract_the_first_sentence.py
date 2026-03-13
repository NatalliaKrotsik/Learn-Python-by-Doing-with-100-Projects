import re
import os

directory = 'texts'

filenames = os.listdir(directory)

all_first_sentences = []
for filename in filenames:
    filepath = os.path.join(directory, filename)
    with open(filepath) as file:
        content = file.read()

    pattern = r'[A-Za-z0-9,;"\'\s\-()]+[.!?]'
    first_sentence = re.findall(pattern, content)
    all_first_sentences.append(first_sentence[0])

for sentence in all_first_sentences:
    print(sentence)

