import json

allowed_sort_keys = ['firstName', 'lastName', 'department', 'salary']


def employees_rewrite(sort_type):
    if sort_type not in allowed_sort_keys:
        raise ValueError('Bad key for sorting')

    with open('employees.json', 'r') as file:
        data = json.load(file)

        data['employees'] = sorted(data['employees'], key=lambda x: x[sort_type], reverse=(sort_type == 'salary'))

    with open(f'employees_{sort_type}_sorted.json', 'w') as output_file:
        json.dump(data, output_file, indent=4)

# Пример вызова функций для сортировки по каждому ключу
for key in allowed_sort_keys:
    employees_rewrite(key)
