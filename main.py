name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
print("Тип возраста до преобразования:", type(age))

age = int(age)
height = float(input("Введите ваш рост: "))

print("Имя:", name)
print("Фамилия:", last_name)
print("Возраст:", age, "Тип:", type(age))
print("Рост:", height, "Тип:", type(height))
