import glob

filepaths = sorted(glob.glob('text_files/*.txt'))

words_counter = {}

for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
        words = content.split()

        for word in words:
            if not word in words_counter:
                words_counter[word] = 1
            else:
                words_counter[word] += 1

with open('text_files/word_frequencies.txt', 'w') as file:
    for word, count in words_counter.items():
        file.write(f'{word}: {count}\n')


