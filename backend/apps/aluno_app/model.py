# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Aluno(Node):
    nome = ndb.StringProperty(required=True)
    data_nascimento = ndb.DateProperty(required=True)
    telefone = ndb.StringProperty(required=True)

