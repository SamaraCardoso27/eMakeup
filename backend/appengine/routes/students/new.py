# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from student.student_model import StudentForm, Course
from tekton.gae.middleware.redirect import RedirectResponse
from routes import students


def salvar(**propriedades):
    propriedades['course']=ndb.Key(Course,int(propriedades['course']))
    form= StudentForm(**propriedades)
    erros=form.validate()
    if erros:
        return
    student=form.fill_model()
    student.put()
    return RedirectResponse(students)