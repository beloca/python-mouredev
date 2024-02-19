### Lambdas ### como una función pero anonima: no tienen nombre, pero se puede almacenar en una varible

sum_two_values = lambda first_value, second_value:first_value + second_value
print(sum_two_values(2, 4))

multiply_values= lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

#podemos hacer que una lambda pase a estar dentro de una función:


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))
