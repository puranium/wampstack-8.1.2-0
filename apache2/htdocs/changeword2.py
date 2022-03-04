import os

target_word = 'Topaz'
new_word = 'Prithiva Topaz'

files = os.listdir('data')
for file_name in files:
    with open('data/'+file_name)as f:
        line = f.readline()
        new_line = line.replace(target_word, new_word)

    with open('data/'+file_name, 'w')as f:
        f.write(new_line)
