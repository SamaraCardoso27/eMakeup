from base import GAETestCase
from config.template_middleware import TemplateResponse
from routes.courses import new
from tekton.gae.middleware.redirect import RedirectResponse
from student.student_model import Course

__author__ = 'samara'


class NewTeste(GAETestCase):
    def test_sucesso(self):
        resposta = new.salvar(name='bla')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/courses',resposta.context)
        cursos = Course.query().fetch()
        self.assertEqual(1,len(cursos))
        curso = cursos[0]
        self.assertEqual('bla',curso.name)


    def test_validacao(self):
        resposta = new.salvar()
        self.assertIsInstance(resposta,TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(Course.query().get())
        self.maxDiff = True
        self.assertDictEqual({u'course':{},u'erros':{'name':u'Required field'}},resposta.context)












