from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import config
from app.models import member

# sqlite 사용시 check_same_thread를 추가 - 쓰레드 사용 안함
engine = create_engine(config.db_conn, echo=True, connect_args={'check_same_thread':False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 서버시작시 테이블 생성
def db_startup():

    member.Base.metadata.create_all(engine)