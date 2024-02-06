from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.schemas.member import NewMember
from app.services.member import MemberService

member_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
member_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@member_router.get('/join', response_class=HTMLResponse)
def join(req: Request):
    return templates.TemplateResponse('join.html', {'request': req})

@member_router.post('/join')
def joincheck(mdto: NewMember):
    result = MemberService.insert_member(mdto)
    return result.rowcount

@member_router.get('/joinok', response_class=HTMLResponse)
def loginok(req: Request):
    return templates.TemplateResponse('joinok.html', {'request': req})


@member_router.get('/login', response_class=HTMLResponse)
def login(req: Request):
    return templates.TemplateResponse('login.html', {'request': req})


@member_router.get('/myinfo', response_class=HTMLResponse)
def myinfo(req: Request):
    return templates.TemplateResponse('myinfo.html', {'request': req})
