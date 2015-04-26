# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from student.student_model import Course, CourseForm
from config.template_middleware import TemplateResponse
from routes import courses
from tekton.gae.middleware.redirect import RedirectResponse


def salvar(**kwargs):
    form= CourseForm(**kwargs)
    erros=form.validate()
    if not erros:
        propriedades=form.normalize()
        course = Course(**propriedades)
        course.put()
        return RedirectResponse(courses)
    else:
        ctx = {'course': kwargs, 'erros':erros}
        return TemplateResponse(ctx, 'courses/courses_form.html')