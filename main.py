n = int(input("Введите количество измерений: "))
sum = 0.0

for i in range(1, n + 1):
    count = float(input(f"Введите измерение №{i}: "))
    sum += count

sr = sum / n

print("Сумма всех измерений:", sum)
print("Среднее арифметическое:", sr)
