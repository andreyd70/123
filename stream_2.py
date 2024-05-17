from threading import Thread
import time


class Khights(Thread):
    def __init__(self, name, skill, enemy, *args, **kwargs):
        super(Khights, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemy = enemy
        print(f'{self.name}, на нас напали!')

    def run(self):
        d = 0
        for scill in range(self.enemy, 0, -self.skill):
            d += 1
            self.enemy -= self.skill
            print(f'{self.name} сражается {d} день (дней)...,осталось {self.enemy} воинов !')
            time.sleep(1)
        print(f'Ура! {self.name} одержал победу за {d} дней!')


knight1 = Khights("Sir Lancelot", 20, 100)
knight2 = Khights("Sir Galahad", 10, 100)

knight1.start()
knight2.start()

knight1.join()
knight2.join()
print('Все битвы закончились!')
