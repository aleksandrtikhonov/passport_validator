from pydantic import BaseSettings


class Settings(BaseSettings):
    mvd_url: str = 'https://проверки.гувм.мвд.рф/upload/expired-passports/list_of_expired_passports.csv.bz2'
    local_mvd_url: str = 'http://127.0.0.1:8000/file.zip.gz'


settings = Settings()
