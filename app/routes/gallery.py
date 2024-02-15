from fastapi import APIRouter, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi import status

from app.schemas.gallery import NewGallery
from app.services.gallery import GalleryService

gallery_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
gallery_router.mount('/static', StaticFiles(directory='views/static'), name='static')


# m = ((cpg - 1) / 10) * 10 + 1


@gallery_router.get('/list/{cpg}', response_class=HTMLResponse)
def list(req: Request, cpg: int):
    stpg = int((cpg - 1) / 10) * 10 + 1     # 페이지네이션 시작값
    galist, cnt = GalleryService.select_gallery(cpg)
    # allpage = ceil(cnt /25)     # 총 페이지 수
    return templates.TemplateResponse(
        'gallery/list.html',{'request': req, 'galist': galist,
           'cpg': cpg, 'stpg': 1, 'allpage': 1, 'baseurl': '/gallery/list/'})


@gallery_router.get('/list/{ftype}/{fkey}/{cpg}', response_class=HTMLResponse)
def find(req: Request, ftype: str, fkey: str, cpg: int):
    # stpg = int((cpg - 1) / 10) * 10 + 1     # 페이지네이션 시작값
    # galist, cnt = GalleryService.find_select_gallery(ftype, '%'+fkey+'%', cpg)
    # allpage = ceil(cnt /25)     # 총 페이지 수
    return templates.TemplateResponse(
        'gallery/list.html',{'request': req, 'galist': None,
                'cpg': cpg, 'stpg': 1, 'allpage': 1, 'baseurl': f'/gallery/list/{ftype}/{fkey}/'})


@gallery_router.get('/write',  response_class=HTMLResponse)
def write(req: Request):
    return templates.TemplateResponse('gallery/write.html', {'request': req})


@gallery_router.post('/write')
async def writeok(title: str = Form(), userid: str = Form(),
            contents: str = Form(), attach: UploadFile = File()):
    res_url = '/gallery/list/1'

    # print(title, userid, contents)
    # print(attach.filename, attach.content_type, attach.size)

    fname, fsize = await GalleryService.process_upload(attach)
    gdto = NewGallery(title=title, userid=userid, contents=contents)
    GalleryService.insert_gallery(gdto, fname, fsize)

    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)


@gallery_router.get('/view/{gno}', response_class=HTMLResponse)
def view(req: Request, gno: str):

    # bd=BoardService.selectone_board(gno)[0]
    # BoardService.update_count_board(gno)
    return templates.TemplateResponse('gallery/view.html', {'request': req, 'bd': None})
