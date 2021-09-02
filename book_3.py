name = 'Camus'
'''
for letter in name:
    print(letter)

lancuch1 = input('Podaj wartość 1: ')
lancuch2 = input('Podaj wartość 2: ')

print('Wczoraj napisałem {} i wysłałem do {}'.format(lancuch1, lancuch2))



words = "aldous Huxley"

print(words.capitalize())

'''

sentence = 'Gdzie teraz? Kto teraz? Kiedy, teraz?'
print(sentence.split('?'))

list1 = ['Zwinny', 'lis', 'przeskoczył', 'nad', 'leniwym', 'psem', '.']

words = ' '.join(list1)
print(words)
words = words[0: -2] + "."
print(words)

sen = 'W czasie suszy szosa sucha'
print(sen.replace('s', '$'))

wor = 'Hemingway'
print(wor.index('m'))

th = 'trzy'
print(th +' ' + th + ' '+ th)
print((th + ' ') * 3)
print('trzy' + 'trzy')

sentence = 'To jest pierwsze zdanie. A to jest drugie.'
print(sentence[:24])