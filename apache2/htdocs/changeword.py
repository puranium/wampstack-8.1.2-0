import os

new_text_content = ''
target_word = 'Turquoise'
new_word = 'Vayuda Turquoise'

files = os.listdir('data')
for filename in files:
    with open('data/' + filename) as f:
        lines = f.readlines()
        new_string = ''
        for i, l in enumerate(lines):
            new_string = l.strip().replace(target_word, new_word)
            if new_string:
                new_text_content += new_string + '/n'
            else:
                new_text_content += '/n'
        print(new_text_content)
    with open('data/' + filename, 'w') as f:
        f.write(new_text_content)
