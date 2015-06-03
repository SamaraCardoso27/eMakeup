# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from student.student_model import Course, CourseForm
from config.template_middleware import TemplateResponse
from routes import courses
from tekton.gae.middleware.redirect import RedirectResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
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




