# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from aluno_app import facade
from routes.alunos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'alunos/admin/form.html')


def save(_handler, aluno_id=None, **aluno_properties):
    cmd = facade.save_aluno_cmd(**aluno_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'aluno': cmd.form}

        return TemplateResponse(context, 'alunos/admin/form.html')
    _handler.redirect(router.to_path(admin))

