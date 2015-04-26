# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from student.student_model import Course, Student
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.students.new import salvar
from routes.students import edit
from tekton.router import to_path
from tekton.gae.middleware.redirect import RedirectResponse
from google.appengine.ext import ndb

@login_not_required
@no_csrf
def index(selected_course=None):
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    ctx={'courses':Course.query_order_by_name().fetch(),
         'salvar_path':to_path(salvar)}
    if selected_course is None:
        ctx['students']=Student.query_order_by_name().fetch()
        ctx['selected_course'] = None
    else:
        ctx['selected_course'] = Course.get_by_id(int(selected_course))
        ctx['students']=Student.query_by_course_order_by_name(selected_course).fetch()

    for course in ctx['students']:
        key = course.key
        key_id = key.id()
        course.edit_path = to_path(edit_path_base, key_id)
        course.deletar_path = to_path(deletar_path_base, key_id)
    return TemplateResponse(ctx,'students/students_home.html')


def deletar(student_id):
    key = ndb.Key(Student, int(student_id))
    key.delete()
    return RedirectResponse(index)


