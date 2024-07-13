import csv
def write_holiday_cities(letter):
    with open('travel-notes.csv', 'r') as file:
        with open('holiday.csv', 'w', encoding='utf-8') as output_file:
            visited_cities = []
            wish_list_cities = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3 and parts[0].startswith(letter):
                    visited_cities.extend(parts[1].split(';'))
                    wish_list_cities.extend(parts[2].split(';'))

            visited_cities = sorted(list(set(visited_cities)))
            wish_list_cities = sorted(list(set(wish_list_cities)))

            output_file.write(f'Посетили: {", ".join(visited_cities)}\n')
            output_file.write(f'Хотят посетить: {", ".join(wish_list_cities)}\n')
            output_file.write(f'Никогда не были в: {", ".join(sorted(set(wish_list_cities) - set(visited_cities)))}\n')
            output_file.write(f'Следующим городом будет: {wish_list_cities[0]}\n')


write_holiday_cities('L')
