DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = list(filter(lambda devs: devs['language'] == 'python', DATA))
    all_python_devs = list(map(lambda devs: devs['name'], all_python_devs))

    all_platzi_workers = list(filter(lambda workers: workers['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda workers: workers['name'], all_platzi_workers))

    old_people = [{**worker, **{'old': worker['age']>70}} for worker in DATA]

    adults = [worker['name'] for worker in DATA if worker['age']>18]

    print('''
    All Python Devs''')
    for dev in all_python_devs:
        print(dev)
    
    print('''
    All Platzi Workers''')
    for worker in all_platzi_workers:
        print(worker)
    
    print('''
    Old people''')
    for worker in old_people:
        print(worker)
    
    print('''
    Adults''')
    for worker in adults:
        print(worker)


if __name__ == '__main__':
    run()