# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from student.student_model import Course
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import courses
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
def index(course_id):
    course=Course.get_by_id(int(course_id))
    ctx={'course':course,
         'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx,'courses/courses_form.html')


@login_not_required
def atualizar(course_id,name):
    course=Course.get_by_id(int(course_id))
    course.name=name
    course.put()
    return RedirectResponse(courses)