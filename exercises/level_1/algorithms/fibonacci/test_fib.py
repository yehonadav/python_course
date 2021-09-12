from fib_memo import fib_memo
from fib import fib

fib_memo.load()
print(fib(1))
print(fib(11))
print(fib(112))
print(fib(33))
print(fib(5))
fib_memo.save()
print(fib(112))
fib_memo.clear()
