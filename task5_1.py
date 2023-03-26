## Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию 
# умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def multiplication(n1,n2):
   
    if n2 == 0:
        return 1
    return multiplication(n1, n2-1) * n1

print(multiplication(2,0))
print(multiplication(2,1))
print(multiplication(2,3))
print(multiplication(2,4))

#решено
