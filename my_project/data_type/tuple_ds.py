my_tuple = (1, "hello", 3.14, True, (2, 3))
print(my_tuple[3])
print(my_tuple)
print(my_tuple[:4])
print(my_tuple[::3])
print(my_tuple[4][0])

for item in my_tuple:
    print(item)

    print(item, type(item))

tuple_data_count = my_tuple.count("hello")

student_tuple = ('Amanda', [98, 85, 87], 279)
student_list = ['Amanda,' [98, 85, 87], 270]

new_name = 'Elvis'

student_tuple = list(student_tuple)
student_tuple[0] = new_name
student_tuple.append('new_data')
student_tuple = tuple(student_tuple)
print(student_tuple)

# student_list[2] = update
