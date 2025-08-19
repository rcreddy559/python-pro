def pass_by_reference_example(my_list):
    my_list.append("9090")
    print("Inside function:", my_list)

original_list = [1, 2, 3]
pass_by_reference_example(original_list)
print("Outside function:", original_list)
