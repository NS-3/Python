
class Date:
    @classmethod
    def pr (cls, dat):
        try:
            dat = [int(el) for el in dat]
            print(dat)
            return dat
        except ValueError: print("данные некорректны")



    @staticmethod
    def valid(dat):  # Статический метод
            cal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
            Date.pr(dt)

            if 0>int(dat[1]) or int(dat[1]) > 12:
                dat[1] = "номер месяца некоректный"
            elif 0>int(dat[0]) or int(dat[0]) > cal[int(dat[1])]:
                dat[0] = "дата некоректна"
            if 0 > int(dat[2]):
                dat[2] = "год некоректный"
            if int(dat[2]) < 100:
                dat[2] = int(dat[2]) + 2000

            print (dat)
            return dat


dt = input("введите число, месяц, год через пробел: ")
dt = dt.split()
print (dt)
print(Date.valid(dt))
