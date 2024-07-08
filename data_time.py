from datetime import datetime


class SuperDate(datetime):
    SEASONS = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter'
    }

    TIME_OF_DAY = {
        'Morning': range(6, 12),
        'Day': range(12, 18),
        'Evening': range(18, 24),
        'Night': range(0, 6)
    }

    def get_season(self):
        return self.SEASONS[self.month]

    def get_time_of_day(self):
        hour = self.hour
        for time, hours_range in self.TIME_OF_DAY.items():
            if hour in hours_range:
                return time


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
