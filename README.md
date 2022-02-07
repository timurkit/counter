# counter
Написать декоратор counter, который заводит внутри объекта-функции метод counter(). Этот метод возвращает, сколько раз эта функция была вызвана. Использовать @wraps. Дополнительное требование: никаких других глобальных объектов (кроме counter и wraps).

Input:
```
@counter
def fun(a, b):
    return a * 1 + b

print(fun.counter())
res = sum(fun(i, i + 1) for i in range(5))
print(fun.counter(), res)
```

Output:
```
0
5 25
```
