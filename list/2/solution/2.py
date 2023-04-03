def average_tuple(tuple_tuple):
    average_list = [sum(num_tuple) / 2 for num_tuple in tuple_tuple]
    return tuple(average_list)
