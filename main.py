import json
import os


allowed_sort_keys = ['firstName', 'lastName', 'department', 'salary']

def normalize_key(key):
    return key.lower().replace('_', '')

def employees_rewrite(sort_type):
    normalized_sort_type = normalize_key(sort_type)

    if normalized_sort_type not in [normalize_key(k) for k in allowed_sort_keys]:
        raise ValueError('Bad key for sorting')

    if not os.path.exists('employees.json'):
        raise FileNotFoundError('The file employees.json does not exist.')

    with open('employees.json', 'r') as file:
        data = json.load(file)

    for employee in data['employees']:
        for key in list(employee.keys()):
            normalized_key = normalize_key(key)
            employee[normalized_key] = employee.pop(key)

    if not all(normalized_sort_type in employee for employee in data['employees']):
        raise ValueError('Bad key for sorting')

    data['employees'] = sorted(
        data['employees'],
        key=lambda x: x[normalized_sort_type],
        reverse=(normalized_sort_type == 'salary')
    )

    output_file_name = f'employees_{normalized_sort_type}_sorted.json'
    with open(output_file_name, 'w') as output_file:
        json.dump(data, output_file, indent=4)

    print(f'Employees sorted by {normalized_sort_type} and saved to {output_file_name}.')

for key in allowed_sort_keys:
    try:
        employees_rewrite(key)
    except Exception as e:
        print(f'Error processing {key}: {e}')
