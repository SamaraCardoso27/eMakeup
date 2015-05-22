# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from aluno_app import facade
from routes.alunos import admin


@no_csrf
def index(aluno_id):
    aluno = facade.get_filme_cmd(aluno_id)()
    detail_form = facade.filme_detail_form()
    context = {'save_path': router.to_path(save, aluno_id), 'aluno': detail_form.fill_with_model(aluno)}
    return TemplateResponse(context, 'alunos/admin/form.html')


def save(_handler, aluno_id, **aluno_properties):
    cmd = facade.update_filme_cmd(aluno_id, **aluno_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'aluno': cmd.form}

        return TemplateResponse(context, 'alunos/admin/form.html')
    _handler.redirect(router.to_path(admin))

