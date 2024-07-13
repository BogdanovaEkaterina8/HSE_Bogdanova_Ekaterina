#Задание 2 (функции и циклы)
"""Напишите функцию, которая будет принимать в себя тип данных int (число) и
возвращать тип bool, если переданное число является палиндромом.
"""
def is_palindrome(num):
return str(num) == str(num)[::-1]

def count_even_odd_digits(num):
even_count = 0
odd_count = 0
for digit in str(num):
if int(digit) % 2 == 0:
even_count += 1
else:
odd_count += 1
return even_count, odd_count

#Пример
num = 12321
print(is_palindrome(num)) # True
num2 = 45678
print(is_palindrome(num2)) # False

#Пример
number = str(input())
x = len(number)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if number[x - i] == number[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")

  """Напишите функцию, которая в качестве аргументов принимает массив (list) с числами
и целевое число. Функция должна возвращать индексы элементов, которые в сумме
дают целевое число."""

  def find_target_indexes(arr, target):
      for i in range(len(arr)):
          for j in range(i + 1, len(arr)):
          if arr[i] + arr[j] == target:
          return [i, j]

  return ["элемент"]

 #Пример
  arr = [1, 2, 3, 4, 5]
  target = 9
  print(find_target_indexes(arr, target))  # [3, 4]

  arr2 = [2, 3, 6, 8]
  target2 = 10
  print(find_target_indexes(arr2, target2))  # [1, 3]