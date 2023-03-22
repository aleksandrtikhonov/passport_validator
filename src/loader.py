import bz2
import pickle
from datetime import datetime

import httpx
from httpx import Client
from pyroaring import BitMap

from core.redis1 import redis_pipe
from core.settings import settings

update_date = datetime.strptime('2023-03-01 22:00:14', '%Y-%m-%d %H:%M:%S')


def check_file() -> None:
    with Client() as client:
        response = client.head(settings.local_mvd_url)
        date = datetime.strptime(response.headers.get("last-modified"), '%a, %d %b %Y %H:%M:%S %Z')
        if update_date > date:
            download_file(client)


def download_file(client: httpx.Client) -> None:
    with open("./te.gz", 'w+b') as download_file:
        with client.stream('GET', settings.local_mvd_url) as response:
            for chunk in response.iter_bytes():
                download_file.write(chunk)


def save_to_redis() -> None:
    # TODO хранилище в конфиг, путь другой.
    with bz2.open("../media/spisok.csv.bz2", mode='rb') as mvd_file:
        next(mvd_file)
        while True:
            lines = [next(mvd_file) for x in range(100000)]
            for line in lines:
                series, number = line.decode().split(',')
                redis_pipe.setbit(f'series:{series}:', int(number), 1)
            redis_pipe.execute()
            redis_pipe.close()


def load_memory_db_from_local_file() -> dict[str, BitMap]:
    # TODO: файл с данными вынести в параметры
    with open('suka.csv', 'rb') as source_file:
        # TODO: заменить пикл
        return pickle.load(source_file)
