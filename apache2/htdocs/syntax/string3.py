#positional formating
print('to {}. Note that some of these techniques are very old. Web design {} in the early 2000’s was a lot different than it is now, but there was still much thought being put into accessibility. ggu Because of that, most of these techniques still hold up today. {} It is still very interesting to see all the thought and problem solving that was {} put into this. Also note that I tested all these FF2, Opera 9, Safari 3, and IE 6 and they all behaved identically'.format('egoing', 12, 'egoing', 'egoing'))

#Named placeholder
print('to {name}. Note that some of these techniques are very old. Web design {age:d} in the early 2000’s was a lot different than it is now, but there was still much thought being put into accessibility. ggu Because of that, most of these techniques still hold up today. {name} It is still very interesting to see all the thought and problem solving that was {name} put into this. Also note that I tested all these FF2, Opera 9, Safari 3, and IE 6 and they all behaved identically'.format(name='egoing', age=12))