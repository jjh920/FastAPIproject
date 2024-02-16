from app.models.member import Member
from app.dbfactory import Session
from sqlalchemy import insert

class MemberService():
    @staticmethod
    def member_convert(mdto):
        # 클라이언트에서 전달받은 데이터를 dict 형식으로 변환
        data = mdto.model_dump()
        mb = Member(**data)
        data = {'userid':mb.userid, 'passwd':mb.passwd, 'name':mb.name, 'email': mb.email}
        return data


    @staticmethod
    def insert_member(mdto):
        data = MemberService.member_convert(mdto)
        # 변환된 회원정보를 member 테이블에 저장
        with Session() as sess:
            stmt = insert(Member).values(data)
            result = sess.execute(stmt)
            sess.commit()

            return result


    @staticmethod
    def check_login(userid, passwd):
        with Session() as sess:
            # member 테이블에서 아이디로 회원 조회 후
            result = sess.query(Member).filter_by(userid=userid).scalar()
            # 실제 회원이 존재하고 비밀번호가 일치한다면
            if result and passwd == result.passwd:
                return result

        return None