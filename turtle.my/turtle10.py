number_get = int(input("Введите номер: "))


def fib(number):
    if number < 2:
        return number
    else:
        return fib(number-2)+fib(number-1)


print(fib(number_get))
