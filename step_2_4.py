text = (input('введите текст: '))

my_text = text.split()
for ind, el in enumerate(my_text):
    print(ind+1, el[:10:])
