def fizzbuzz(number):
    if (number % 15 == 0):
        return('fizzbuzz')
    elif (number % 3 == 0):
        return('fizz')
    elif    (number % 5 == 0):
        return('buzz')
    else:
        return number

print(fizzbuzz(15))
print(fizzbuzz(10))
print(fizzbuzz(45))
print(fizzbuzz(12))
