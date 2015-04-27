# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from blog.blog_model import Blog
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import blogs
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
def index(blog_id):
    blog = Blog.get_by_id(int(blog_id))
    ctx={'blog':blog,
         'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx,'blogs/blogs_form.html')

@login_not_required
@no_csrf
def atualizar(blog_id,author,subject,title,text):
    blog = Blog.get_by_id(int(blog_id))
    blog.author = author
    blog.subject = subject
    blog.title = title
    blog.text = text
    blog.put()
    return RedirectResponse(blogs)

