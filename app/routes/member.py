from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.schemas.member import NewMember

member_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
member_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@member_router.get('/join', response_class=HTMLResponse)
def join(req: Request):
    return templates.TemplateResponse('join.html', {'request': req})

@member_router.post('/join')
def joinok(req: Request, mdto: NewMember):
    print(mdto)
    return 1


@member_router.get('/login', response_class=HTMLResponse)
def login(req: Request):
    return templates.TemplateResponse('login.html', {'request': req})


@member_router.get('/myinfo', response_class=HTMLResponse)
def myinfo(req: Request):
    return templates.TemplateResponse('myinfo.html', {'request': req})
