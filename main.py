print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        result = str(number)
    return result

limit = int(input())

for i in range(1, limit + 1):
    if "3" in str(i) and i % 3 != 0 and i % 7 != 0:
        print("Almost Fizz")
    else:
        print(fizzbuzz(i))