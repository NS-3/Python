from random import randint


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    def get_full_name (self):
        full_name = surname + " " + name
        print(f'сотрудник {full_name} в должности {position}')
        return (full_name)
    def get_total_income (self):
        total_income = int(Worker._income['wage']) + int(Worker._income['bonus'])
        print(f'имеет средмемесячный доход в размере {total_income} рублей')
        return (total_income)



try:
    surname = input("введите фамилию: ", )
    name = input("введите имя: ", )
    position = input("введите должность: ", )
except: "что-то не так. попробуйте снова"
Worker._income = {}
wage = randint(10000, 50000)
bonus = randint(20000, 80000)
Worker._income[wage] = wage
Worker._income[bonus] = bonus
Worker._income = {"wage": wage, "bonus": bonus}
#income = incomes
print(Worker._income)



my_c_worker = Worker(name, surname, position,Worker._income)
#my_c_worker.w_i()
my_c_position = Position(name, surname, position,Worker._income)
my_c_position.get_full_name()
my_c_position.get_total_income()
# super().gas()