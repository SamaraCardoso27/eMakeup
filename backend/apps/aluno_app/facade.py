# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from aluno_app.commands import ListAlunoCommand, SaveAlunoCommand, UpdateAlunoCommand, \
    AlunoPublicForm, AlunoDetailForm, AlunoShortForm


def save_aluno_cmd(**aluno_properties):
    """
    Command to save Aluno entity
    :param aluno_properties: a dict of properties to save on model
    :return: a Command that save Aluno, validating and localizing properties received as strings
    """
    return SaveAlunoCommand(**aluno_properties)


def update_aluno_cmd(aluno_id, **aluno_properties):
    """
    Command to update Aluno entity with id equals 'aluno_id'
    :param aluno_properties: a dict of properties to update model
    :return: a Command that update Aluno, validating and localizing properties received as strings
    """
    return UpdateAlunoCommand(aluno_id, **aluno_properties)


def list_alunos_cmd():
    """
    Command to list Aluno entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListAlunoCommand()


def aluno_detail_form(**kwargs):
    """
    Function to get Aluno's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return AlunoDetailForm(**kwargs)


def aluno_short_form(**kwargs):
    """
    Function to get Aluno's short form. just a subset of aluno's properties
    :param kwargs: form properties
    :return: Form
    """
    return AlunoShortForm(**kwargs)

def aluno_public_form(**kwargs):
    """
    Function to get Aluno'spublic form. just a subset of aluno's properties
    :param kwargs: form properties
    :return: Form
    """
    return AlunoPublicForm(**kwargs)


def get_aluno_cmd(aluno_id):
    """
    Find aluno by her id
    :param aluno_id: the aluno id
    :return: Command
    """
    return NodeSearch(aluno_id)


def delete_aluno_cmd(aluno_id):
    """
    Construct a command to delete a Aluno
    :param aluno_id: aluno's id
    :return: Command
    """
    return DeleteNode(aluno_id)

