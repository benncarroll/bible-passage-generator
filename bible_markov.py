import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import markovify

try:
    # Read model
    file = open("models/bible_markov_model.txt", 'r')
    #print('Found previously generated model, reading...')
    model = markovify.Text.from_json(file.read())

except FileNotFoundError:
    #print('No previously generated model found, creating...')
    with open("kjvdat.txt") as f:
        text = f.read()

    line_arr = []

    for line in text.split('\n'):
        if line == '':
            continue
        line_arr.append(line.split('|')[3][1:-1])

    corpus = ' '.join(line_arr)

    model = markovify.Text(corpus, state_size=5)

    # Save model
    model_json = model.to_json()
    with open("bible_markov_model.txt", "w+") as f:
        f.write(model_json)

while True:
    p = model.make_short_sentence(140)
    if len(str(p)) > 50:
        print(p.strip())
        break

#print('Done. Generating sentences...')
# print()
# sen_arr = []
# for i in range(10):
#     sen_arr.append(model.make_short_sentence(140))
# for sen in sen_arr:
#     print('    -', sen)
# print()
