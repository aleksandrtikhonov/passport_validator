import bz2
import pickle

from pyroaring import BitMap

from core.redis1 import redis_pipe1

suka = BitMap()

from collections import defaultdict


def save_to_redis() -> None:
    i = 0
    d = defaultdict(BitMap)
    with bz2.open("../media/spisok.csv.bz2", mode='rb') as mvd_file:
        next(mvd_file)
        while True:
            try:
                lines = [next(mvd_file) for x in range(10_000_000)]
            except Exception:
                break
            for line in lines:
                series, number = line.decode().split(',')
                try:
                    d[series].add(int(number))
                except Exception:
                    pass
            i += 1
            print(f'цикл прошёл {i} раз')
            # if i == 1:
            #     break
        with open("suka.csv", "wb+") as temp:
            pickle.dump(d, temp)

            #     redis_pipe1.setbit(f'series:{series}:', int(number), 1)
            # redis_pipe1.execute()
            # redis_pipe1.close()


save_to_redis()
