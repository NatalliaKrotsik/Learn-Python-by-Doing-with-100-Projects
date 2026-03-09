# Read the text from the file
with open('snowwhite.txt') as file:
    text = file.read()

# Split the text into sentences and save the sentences in a list
sentences = text.split(". ")

corrected_sentences = []

# Iterate over the list of sentences
# and add each capitalized sentence in a list
for sentence in sentences:
    sentence = sentence.capitalize()
    corrected_sentences.append(sentence)

# Join the sentences of the list into one single string
corrected_text = ". ".join(corrected_sentences)

# Write the corrected text to a file
with open('snowwhite_corrected.txt', 'w') as file:
    file.write(corrected_text)