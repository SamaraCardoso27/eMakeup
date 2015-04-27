# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from student.student_model import Student, Course
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import students
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
def index(student_id):
    student = Student.get_by_id(int(student_id))
    ctx = {'courses': Course.query_order_by_name().fetch(),
           'student': student,
           'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'students/students_form.html')

@login_not_required
def atualizar(student_id, name, birthday, phone_number, course):
    student = Student.get_by_id(int(student_id))
    student.name = name
    student.birthday = birthday
    student.phone_number = phone_number
    student.course = ndb.Key(Course, int(course))
    student.put()
    return RedirectResponse(students)