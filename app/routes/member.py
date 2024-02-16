from fastapi import APIRouter, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from app.schemas.member import NewMember
from app.services.member import MemberService
from starlette import status

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

@member_router.post('/login')
def login(req: Request, userid: str = Form(), passwd: str = Form()):
    result = MemberService.check_login(userid, passwd)

    if result:
        # 세션처리 - 회원아이디를 세션에 등록
        req.session['m'] = result.userid
        return RedirectResponse(url='/myinfo', status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)

@member_router.get('/logout')
def login(req: Request):
    req.session.clear()     # 생성된 세션객체 제거
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)



@member_router.get('/myinfo', response_class=HTMLResponse)
def myinfo(req: Request):
    if 'm' not in req.session:
        return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse('myinfo.html', {'request': req})
