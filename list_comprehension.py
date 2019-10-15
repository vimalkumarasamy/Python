students = ['john', 'jane', 'doe']

x=[student[0].upper()+student[1:] for student in students]

print(f'The initial array was this {students}')
print(f'The edited array is this   {x}')

# ## You can add conditional logic to list comprehension!

numbers = range(20)

even = [number for number in numbers if number % 2 == 0 ]
odd = [number for number in numbers if number % 2 != 0 ]

[number if number % 2 == 0 else number**3 for number in range(10)]