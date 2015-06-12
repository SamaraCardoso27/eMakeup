from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.router import to_path

__author__ = 'samara'


@login_not_required
@no_csrf
def index():
    comando = blob_facade.list_blob_files_cmd()
    arquivos = comando()
    download_path = to_path(download)
    for arq in arquivos:
        arq.download_path =  to_path(download_path,arq.key.id())

    ctx = {'arquivos':arquivos}
    return TemplateResponse(ctx,'upload_home.html')


@login_not_required
@no_csrf
def download(_handle,blob_id,filename):
    comando = blob_facade.list_blob_files_cmd(blob_id)
    arquivo_bd = comando()
    _handle.send_blob(arquivo_bd.blob_key)


@login_not_required
@no_csrf
def upload(_handler,blobs,id):
    blob_info = _handler.get_uploads('blobs')
    blob_facade.save_blob_files_cmd(blob_info).execute()

@login_not_required
@no_csrf
def upload(_handler,blobs,id):
    upload_path = to_path(upload)
    bucket = get_default_bucket_name()
    ctx = {'salvar_path':blobstore.create_upload_url(upload_path,bucket)}
    return TemplateResponse(ctx,'upload_form.html')

@login_not_required
@no_csrf
def form():
    return TemplateResponse(template_path='upload_form.html')