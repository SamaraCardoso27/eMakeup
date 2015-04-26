# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from student.student_model import Course
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.courses import edit
from routes.courses.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index():
    query = Course.query_order_by_name()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    courses = query.fetch()
    for cat in courses:
        key = cat.key
        key_id = key.id()
        cat.edit_path = to_path(edit_path_base, key_id)
        cat.deletar_path = to_path(deletar_path_base, key_id)
    ctx = {'salvar_path': to_path(salvar),
           'courses': courses}
    return TemplateResponse(ctx, 'courses/courses_home.html')


def deletar(course_id):
    key = ndb.Key(Course, int(course_id))
    key.delete()
    return RedirectResponse(index)