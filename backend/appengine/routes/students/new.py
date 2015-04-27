# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from student.student_model import StudentForm, Course
from tekton.gae.middleware.redirect import RedirectResponse
from routes import students
from gaepermission.decorator import login_not_required

@login_not_required
def salvar(**propriedades):
    propriedades['course']=ndb.Key(Course,int(propriedades['course']))
    form= StudentForm(**propriedades)
    erros=form.validate()
    if not erros:
        student=form.fill_model()
        student.put()
        return RedirectResponse(students)
    else:
        ctx = {'student': propriedades, 'erros':erros, 'courses':Course.query_order_by_name().fetch()}
        return TemplateResponse(ctx, 'students/students_form.html')