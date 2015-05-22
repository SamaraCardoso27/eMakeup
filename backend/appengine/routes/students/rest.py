# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from student.student_model import StudentForm, Course, Student
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse, JsonResponse
from google.appengine.ext import ndb


@login_not_required
@no_csrf
def deletar(student_id):
    key=ndb.Key(Student,int(student_id))
    key.delete()

@login_not_required
@no_csrf
def listar():
    form = StudentForm()
    students = Student.query_order_by_name().fetch()
    students = [form.fill_with_model(s) for s in students]
    return JsonResponse(students)
    #return JsonUnsecureResponse(students)

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    propriedades['course']=ndb.Key(Course,int(propriedades['course']))
    form = StudentForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    student = form.fill_model()
    student.put()
    dct = form.fill_with_model(student)
    log.info(dct)
    return JsonResponse(dct)
    #return JsonUnsecureResponse(dct)
