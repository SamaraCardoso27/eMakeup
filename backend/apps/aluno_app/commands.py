# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from aluno_app.model import Aluno

class AlunoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Aluno
    _include = [Aluno.nome, 
                Aluno.data_nascimento, 
                Aluno.telefone]


class AlunoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Aluno
    _include = [Aluno.nome, 
                Aluno.data_nascimento, 
                Aluno.telefone]


class AlunoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Aluno
    _include = [Aluno.nome, 
                Aluno.creation, 
                Aluno.data_nascimento, 
                Aluno.telefone]


class AlunoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Aluno
    _include = [Aluno.nome, 
                Aluno.creation, 
                Aluno.data_nascimento, 
                Aluno.telefone]


class SaveAlunoCommand(SaveCommand):
    _model_form_class = AlunoForm


class UpdateAlunoCommand(UpdateNode):
    _model_form_class = AlunoForm


class ListAlunoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListAlunoCommand, self).__init__(Aluno.query_by_creation())

