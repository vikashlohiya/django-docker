def generate_even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2

# Using the generator function
even_gen = generate_even_numbers(10)
print(even_gen)
for num in even_gen:
    print(num)
