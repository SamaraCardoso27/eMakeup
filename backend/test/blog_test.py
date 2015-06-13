from base import GAETestCase
from config.template_middleware import TemplateResponse
from routes.blogs import new
from tekton.gae.middleware.redirect import RedirectResponse
from blog.blog_model import Blog

__author__ = 'samara'


class NewTeste(GAETestCase):
    def test_sucesso(self):
        resposta = new.salvar(author='author',subject='subject',title='title',text='text')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/blogs',resposta.context)
        blogs = Blog.query().fetch()
        self.assertEqual(1,len(blogs))
        blog = blogs[0]
        self.assertEqual('author',blog.author)
        self.assertEqual('subject',blog.subject)
        self.assertEqual('title',blog.title)
        self.assertEqual('text',blog.text)


    def test_validacao(self):
        resposta = new.salvar()
        self.assertIsInstance(resposta,TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(Blog.query().get())
        self.maxDiff = True
        self.assertDictEqual({u'blog':{},u'erros':{'author':u'Required field','subject':u'Required field',
                                                   'title':u'Required field','text':u'Required field'}},resposta.context)











