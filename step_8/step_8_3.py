class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

l = []
inp_data1 = 0
print("Введите числа (для окончания ввода введите stop):")
i=0
while inp_data1 != "stop":
    try:
        inp_data1 = input()

        inp_data1 = int(inp_data1)
        l.append(inp_data1)

    except ValueError: print(OwnError("Вы ввели не целое число или не число"))

print(f"Ваш результат: {l}")