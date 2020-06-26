'Create Fibonacci Series upto n using Lambda'

x = int( input('Enter the number of terms:'))

def fibonacci(count):
    fibo_list = [0, 1]
    any(map(lambda _: fibo_list.append(sum(fibo_list[-2:])),
            range(2, count)))
    return fibo_list[:count]
print(fibonacci(x))