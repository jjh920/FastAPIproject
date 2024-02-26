from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    userid: str = ''
    passwd: str = ''
    # dbname: str = 'clouds2024.db'
    dbname: str = 'bigdata'
    # dbname: str = 'clouds2024.db'
    dburl: str = 'bigdata.c7lzyml8zvod.ap-northeast-2.rds.amazonaws.com'
    # db_conn: str = f'sqlite:///app/{dbname}'
    db_conn: str = f'mysql+pymysql://{userid}:{passwd}@{dburl}:3306/{dbname}?charset=utf8mb4'
    #db_conn = f'oracle+cx_pymysql://{userid}:{passwd}'

    class Config:
        env_file = '.env'


config = Settings()
