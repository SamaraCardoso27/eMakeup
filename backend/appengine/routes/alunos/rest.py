# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from aluno_app import facade


@login_not_required
@no_csrf
def index():
    cmd = facade.list_alunos_cmd()
    aluno_list = cmd()
    short_form = facade.aluno_short_form()
    aluno_short = [short_form.fill_with_model(m) for m in aluno_list]
    return JsonResponse(aluno_short)


@login_not_required
@no_csrf
def save(_resp, **aluno_properties):
    cmd = facade.save_aluno_cmd(**aluno_properties)
    return _save_or_update_json_response(_resp, cmd)


@login_not_required
@no_csrf
def update(_resp, id, **aluno_properties):
    cmd = facade.update_aluno_cmd(id, **aluno_properties)
    return _save_or_update_json_response(_resp, cmd)


@login_not_required
@no_csrf
def delete(id):
    facade.delete_aluno_cmd(id)()


def _save_or_update_json_response(_resp, cmd):
    try:
        aluno = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse(cmd.errors)
    short_form = facade.aluno_short_form()
    return JsonResponse(short_form.fill_with_model(aluno))

