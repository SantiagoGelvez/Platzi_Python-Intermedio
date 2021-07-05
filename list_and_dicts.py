def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Santiago', 'lastname': 'Gelvez'}

    super_list = [
        {'firstname': 'Santiago', 'lastname': 'Gelvez'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Pepe', 'lastname': 'Rodelo'},
        {'firstname': 'Susana', 'lastname': 'Martinez'},
        {'firstname': 'Jose', 'lastname': 'Garcia'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    # for field in super_list:
    #     for key, value in field.items():
    #         print(key, '-', value)

    for value in super_list:
        print(value['firstname'], '-', value['lastname'])

if __name__ == '__main__':
    run()