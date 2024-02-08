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

@board_router.get('/list')
def list(req: Request):
    bdlist = BoardService.select_board()
    return templates.TemplateResponse('board/list.html', {'request': req, 'bdlist': bdlist})


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
    return templates.TemplateResponse('board/view.html', {'request': req, 'bd': bd})
