# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gallery.gallery_model import Gallery, GalleryForm
from config.template_middleware import TemplateResponse
from routes import gallerys
from tekton.gae.middleware.redirect import RedirectResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def salvar(**kwargs):
    form = GalleryForm(**kwargs)
    erros=form.validate()
    if not erros:
        propriedades=form.normalize()
        gallery = Gallery(**propriedades)
        gallery.put()
        return RedirectResponse(gallerys)
    else:
        ctx = {'gallery': kwargs, 'erros':erros}
        return TemplateResponse(ctx, 'gallerys/gallery_form.html')