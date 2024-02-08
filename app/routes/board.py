from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi import status
from app.schemas.board import NewBoard
from app.services.board import BoardService

board_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
board_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 페이징 알고리즘
# 페이지당 게시글 수 : 25
# 1page : 1 ~ 25
# 2page : 26 ~ 50
# 3page : 51 ~ 75
# ...
# npage : (n-1)*25 ~ (n)*25+25

@board_router.get('/list/{cpg}', response_class=HTMLResponse)
def list(req: Request, cpg: int):
    bdlist = BoardService.select_board(cpg)
    return templates.TemplateResponse('board/list.html', {'request': req, 'bdlist': bdlist, 'cpg':cpg})


@board_router.get('/write',  response_class=HTMLResponse)
def write(req: Request):
    return templates.TemplateResponse('board/write.html', {'request': req})

@board_router.post('/write')
def writeok(bdto: NewBoard):
    result = BoardService.insert_board(bdto)
    res_url = '/error'
    if result.rowcount > 0: res_url = '/board/list'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)


@board_router.get('/view/{bno}', response_class=HTMLResponse)
def view(req: Request, bno: str):

    bd=BoardService.selectone_board(bno)[0]
    BoardService.update_count_board(bno)
    return templates.TemplateResponse('board/view.html', {'request': req, 'bd': bd})
