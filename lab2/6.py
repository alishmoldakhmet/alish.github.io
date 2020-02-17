def generator_example():
    n = 8
    print("first print")
    yield n
    n = 6
    print("second print")
    yield n
    n = 9
    print("third print")
    yield n

a = generator_example() # a -> iterator
b = generator_example()

print(next(a))
print(next(a))

print(next(b))
print(next(b))
print(next(b))
