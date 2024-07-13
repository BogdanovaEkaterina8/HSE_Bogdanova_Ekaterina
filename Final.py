#Задача 1

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ввод данных от пользователя
if __name__ == '__main__':
    n = int(input("Введите количество чисел Фибоначчи для генерации: "))
    print(f"Первые {n} чисел Фибоначчи:")
    for num in fib(n):
        print(num)

#Задача 2

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Ввод данных от пользователя
if __name__ == '__main__':
    roman_numeral = input("Введите римское число: ")
    result = roman_to_int(roman_numeral)
    print(f"Значение {roman_numeral} в десятичной системе: {result}")

#Задача 3

def is_monotonic(nums):
    increasing = decreasing = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
    return increasing or decreasing

# Ввод данных от пользователя
if __name__ == '__main__':
    input_str = input("Введите элементы массива через пробел: ")
    nums = list(map(int, input_str.split()))
    result = is_monotonic(nums)
    print(f"Массив {nums} {'является' if result else 'не является'} монотонным")


