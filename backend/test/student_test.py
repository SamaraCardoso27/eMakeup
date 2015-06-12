from base import GAETestCase
from config.template_middleware import TemplateResponse
from routes.students import new
from tekton.gae.middleware.redirect import RedirectResponse
from student.student_model import Student

__author__ = 'samara'


#class NewTeste(GAETestCase):
#    def test_sucesso(self):
#        resposta = new.salvar(name='Samara',birthday='27/03/1994',phone_number='12988211378')
#        self.assertIsInstance(resposta, RedirectResponse)
#        self.assertEqual('/students',resposta.context)
#        alunos = Student.query().fetch()
#        self.assertEqual(1,len(alunos))
#        aluno = alunos[0]
#        self.assertEqual('Samara',aluno.name)
#        self.assertEqual('27/03/1994',aluno.birthday)
#        self.assertEqual('12988211378',aluno.phone_number)



#    def test_validacao(self):
#        resposta = new.salvar()
#        self.assertIsInstance(resposta,TemplateResponse)
#        self.assert_can_render(resposta)
#        self.assertIsNone(Student.query().get())
#        self.maxDiff = True
#        self.assertDictEqual({u'course':{},u'erros':{'name':u'Required field'}},resposta.context)












