from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.dbfactory import db_startup
from app.routes.board import board_router
from app.routes.gallery import gallery_router
from app.routes.member import member_router

# 서버시작시 디비 생성
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    db_startup()

app = FastAPI(lifespan=lifespan)

# 세션처리를 위한 미들웨어 설정
# 미들웨어 - 프론트엔드와 백엔드 사이 또는 어플리케이션내 구성요소 사이에서
# 작동하는 특수한 소프트웨어
# 미들웨어의 목적은 요청처리, 응답생성, 에러 처리등을 담당
# 요청시 생성된 세션객체를 사용할 수 있게 해 줌
app.add_middleware(SessionMiddleware, secret_key='20240216103735')



# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
# app.mount('/static', StaticFiles(directory='views/static'), name='static')

# 외부 route 파일 불러오기
app.include_router(member_router)
app.include_router(board_router, prefix='/board')
app.include_router(gallery_router, prefix='/gallery')



@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'index.html', {'request': req})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
