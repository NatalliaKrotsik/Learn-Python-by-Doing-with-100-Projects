with open('snowwhite.txt') as file:
    text = file.read()

sentences = text.split(". ")
sentences = [s.capitalize() for s in sentences]

corrected_text = ". ".join(sentences)

with open('corrected_text.txt', 'w') as file:
    file.write(corrected_text)


