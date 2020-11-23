from kivy.app               import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder      import Builder
from kivymd.app             import MDApp
from kivymd.uix.screen      import Screen 
from kivymd.theming         import ThemeManager
import math
from banco_de_exercicio     import dict_exercicios
import random 
import minha_materia

#variables

class MainApp(MDApp):
    dicionario_marcada = {}
    dicionario_correcao = {}
    dicionario_enunciado = {}
    dicionario_alternativa_correta  = {}
    dicionario_valores_alternativas_corretas = {}
    dicionario_valores_alternativas_marcadas = {}
    lista_checa_exercicios = []
    lista_exercicios_selecionados = []

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue ="A700"
        Builder.load_string(open('main.kv', encoding = "utf-8").read())
        return MyMainWidget()

class MyMainWidget(ScreenManager):
    pass

class Menu(Screen):
    pass

class Introducao1(Screen):
    string_intro = minha_materia.primeira_string

    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Introducao2(Screen):
    string_intro = minha_materia.segunda_string

    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Introducao3(Screen):
    string_intro = minha_materia.terceira_string

    def voltar(self):
        MDApp.get_running_app().root.current = "menu"
class Introducao4(Screen):
    string_intro = minha_materia.quarta_string

    def voltar(self):
        MDApp.get_running_app().root.current = "menu"
class create_questionario():
    def __init__(self, **kwargs):
        super(create_questionario, self).__init__(**kwargs)
        self.dicionario_exercicios = dict_exercicios
        self.dicionario_correcao = {}
        self.dicionario_marcada  = {}
        self.dicionario_enunciado = {}
        self.dicionario_alternativa_correta  = {}
        self.lista_checa_exercicios = []
        self.lista_exercicios_selecionados = []
        self.questao = {}
        self.pergunta = ''
        self.alternativa_correta = ''
        self.alternativa_marcada = ''

    def clear_tudo (self, **kwargs):
        self.dicionario_exercicios = dict_exercicios
        self.dicionario_correcao = {}
        self.dicionario_marcada  = {}
        self.dicionario_enunciado = {}
        self.dicionario_alternativa_correta  = {}
        self.dicionario_alternativa_marcada_value = {}
        self.lista_checa_exercicios = []
        self.lista_exercicios_selecionados = []
        self.questao = {}
        self.pergunta = ''
        self.alternativa_correta = ''         
        self.alternativa_marcada = ''


    def create_lista_exercicios(self, **kwargs):
        while len(self.lista_checa_exercicios) < 5:
            ex = random.randrange(0,len(dict_exercicios),1)
            if ex in self.lista_checa_exercicios:
                continue
            else:
                exercicio = dict_exercicios[ex]
                self.lista_checa_exercicios.append(ex)
                self.lista_exercicios_selecionados.append(exercicio)

    def pega_exercicio(self,contador, **kwargs):
        self.questao  = self.lista_exercicios_selecionados[contador]
        self.pergunta = self.questao['enunciado']
        self.alternativa_correta = self.questao['resposta_correta']


class Calculadora(Screen):
    resposta = ''
    
    def calcular(self):
        a = self.ids.variavel_a.text
        b = self.ids.variavel_b.text
        c = self.ids.variavel_c.text
        resposta = self.ids.calculadora_label
        if (a == '' or b == '' or c == ''):
            resposta.text = f"Por favor preencha com números inteiros"  
        else :
            a = int(a)
            b = int(b)
            c = int(c)
            delta      = b**2 - 4*a*c
            if delta < 0:
                resposta.text = "Não possui raízes reais."
            elif delta == 0 :
                raiz_delta = math.sqrt(delta)
                x = (-b + raiz_delta)/(2 * a)
                resposta.text = f"Possui uma raíz real igual {x}."
            elif delta > 0 :
                raiz_delta = math.sqrt(delta)
                x_1 = (-b + raiz_delta)/(2 * a)
                x_2 = (-b - raiz_delta)/(2 * a)
                x_1 = round(x_1, 2)
                x_2 = round(x_2,2)
                resposta.text = f"Possui duas raízes reais iguais a {x_1} e {x_2}."

    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Exercicios(Screen):     
    def __init__(self, **kwargs):
        super(Exercicios, self).__init__(**kwargs)   

    def criando_exercicios(self):
        app = MDApp.get_running_app()
        criando_questionario = create_questionario()        
        criando_questionario.create_lista_exercicios()
        lista_criada = criando_questionario.lista_exercicios_selecionados
        app.lista_exercicios_selecionados = lista_criada
        
    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Prova1(Screen):
    def __init__(self, **kwargs):
        super(Prova1, self).__init__(**kwargs)

    def comecando_exercicios(self):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_alternativa_correta[0]           = lista_criada[0]['resposta_correta']
        resposta_correta                                = lista_criada[0]['resposta_correta']
        app.dicionario_valores_alternativas_corretas[0] = lista_criada[0]['alternativas'][resposta_correta]
        app.dicionario_enunciado[0]                     = lista_criada[0]['enunciado']

        self.enunciado        = lista_criada[0]['enunciado']
        self.alternativas     = lista_criada[0]['alternativas']
        self.alternativa_a    = self.alternativas['a']
        self.alternativa_b    = self.alternativas['b']
        self.alternativa_c    = self.alternativas['c']
        self.alternativa_d    = self.alternativas['d']
        self.alternativa_e    = self.alternativas['e']


        self.ids.prova1_enunciado.text    = str(self.enunciado)
        self.ids.prova1_alternativa1.text = str(self.alternativa_a)
        self.ids.prova1_alternativa2.text = str(self.alternativa_b)
        self.ids.prova1_alternativa3.text = str(self.alternativa_c)
        self.ids.prova1_alternativa4.text = str(self.alternativa_d)
        self.ids.prova1_alternativa5.text = str(self.alternativa_e)


    def salvando_os_dados_do_usuario(self, resposta_marcada):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_marcada[0] = resposta_marcada
        valor_resposta_marcada    = lista_criada[0]['alternativas'][resposta_marcada]
        app.dicionario_valores_alternativas_marcadas[0] = valor_resposta_marcada
        MDApp.get_running_app().root.current = 'prova2'


    def voltar(self):
        MDApp.get_running_app().root.current = "menu"   

class Prova2(Screen):
    def __init__(self, **kwargs):
        super(Prova2, self).__init__(**kwargs)
        
    def comecando_exercicios(self):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_alternativa_correta[1] = lista_criada[1]['resposta_correta']
        resposta_correta                      = lista_criada[0]['resposta_correta']
        app.dicionario_valores_alternativas_corretas[1] = lista_criada[1]['alternativas'][resposta_correta]
        app.dicionario_enunciado[1]           = lista_criada[1]['enunciado']

        self.enunciado        = lista_criada[1]['enunciado']
        self.alternativas     = lista_criada[1]['alternativas']
        self.alternativa_a    = self.alternativas['a']
        self.alternativa_b    = self.alternativas['b']
        self.alternativa_c    = self.alternativas['c']
        self.alternativa_d    = self.alternativas['d']
        self.alternativa_e    = self.alternativas['e']

        self.ids.prova2_enunciado.text    = str(self.enunciado)
        self.ids.prova2_alternativa1.text = str(self.alternativa_a)
        self.ids.prova2_alternativa2.text = str(self.alternativa_b)
        self.ids.prova2_alternativa3.text = str(self.alternativa_c)
        self.ids.prova2_alternativa4.text = str(self.alternativa_d)
        self.ids.prova2_alternativa5.text = str(self.alternativa_e)


    def salvando_os_dados_do_usuario(self, resposta_marcada):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_marcada[1] = resposta_marcada
        valor_resposta_marcada    = lista_criada[1]['alternativas'][resposta_marcada]
        app.dicionario_valores_alternativas_marcadas[1] = valor_resposta_marcada
        MDApp.get_running_app().root.current = 'prova3'


    def voltar(self):
        MDApp.get_running_app().root.current = "menu"      
        
class Prova3(Screen):
    def __init__(self, **kwargs):
        super(Prova3, self).__init__(**kwargs)

    def comecando_exercicios(self):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_alternativa_correta[2] = lista_criada[2]['resposta_correta']
        resposta_correta                      = lista_criada[0]['resposta_correta']
        app.dicionario_valores_alternativas_corretas[2] = lista_criada[2]['alternativas'][resposta_correta]
        app.dicionario_enunciado[2]           = lista_criada[2]['enunciado']

        self.enunciado        = lista_criada[2]['enunciado']
        self.resposta_correta = lista_criada[2]['resposta_correta']
        self.alternativas     = lista_criada[2]['alternativas']
        self.alternativa_a    = self.alternativas['a']
        self.alternativa_b    = self.alternativas['b']
        self.alternativa_c    = self.alternativas['c']
        self.alternativa_d    = self.alternativas['d']
        self.alternativa_e    = self.alternativas['e']

        self.ids.prova3_enunciado.text    = str(self.enunciado)
        self.ids.prova3_alternativa1.text = str(self.alternativa_a)
        self.ids.prova3_alternativa2.text = str(self.alternativa_b)
        self.ids.prova3_alternativa3.text = str(self.alternativa_c)
        self.ids.prova3_alternativa4.text = str(self.alternativa_d)
        self.ids.prova3_alternativa5.text = str(self.alternativa_e)


    def salvando_os_dados_do_usuario(self, resposta_marcada):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_marcada[2] = resposta_marcada
        valor_resposta_marcada    = lista_criada[2]['alternativas'][resposta_marcada]
        app.dicionario_valores_alternativas_marcadas[2] = valor_resposta_marcada
        MDApp.get_running_app().root.current = 'prova4'


    def voltar(self):
        MDApp.get_running_app().root.current = "menu"    

class Prova4(Screen):
    def __init__(self, **kwargs):
        super(Prova4, self).__init__(**kwargs)


    def comecando_exercicios(self):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_alternativa_correta[3] = lista_criada[3]['resposta_correta']
        resposta_correta                      = lista_criada[0]['resposta_correta']
        app.dicionario_valores_alternativas_corretas[3] = lista_criada[3]['alternativas'][resposta_correta]
        app.dicionario_enunciado[3]           = lista_criada[3]['enunciado']

        self.enunciado        = lista_criada[3]['enunciado']
        self.resposta_correta = lista_criada[3]['resposta_correta']
        self.alternativas     = lista_criada[3]['alternativas']
        self.alternativa_a    = self.alternativas['a']
        self.alternativa_b    = self.alternativas['b']
        self.alternativa_c    = self.alternativas['c']
        self.alternativa_d    = self.alternativas['d']
        self.alternativa_e    = self.alternativas['e']

        self.ids.prova4_enunciado.text    = str(self.enunciado)
        self.ids.prova4_alternativa1.text = str(self.alternativa_a)
        self.ids.prova4_alternativa2.text = str(self.alternativa_b)
        self.ids.prova4_alternativa3.text = str(self.alternativa_c)
        self.ids.prova4_alternativa4.text = str(self.alternativa_d)
        self.ids.prova4_alternativa5.text = str(self.alternativa_e)


    def salvando_os_dados_do_usuario(self, resposta_marcada):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_marcada[3] = resposta_marcada
        valor_resposta_marcada    = lista_criada[3]['alternativas'][resposta_marcada]
        app.dicionario_valores_alternativas_marcadas[3] = valor_resposta_marcada
        MDApp.get_running_app().root.current = 'prova5'


    def voltar(self):
        MDApp.get_running_app().root.current = "menu"    

class Prova5(Screen):
    def __init__(self, **kwargs):
        super(Prova5, self).__init__(**kwargs)

    def comecando_exercicios(self):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_alternativa_correta[4]        = lista_criada[4]['resposta_correta']
        resposta_correta                             = lista_criada[0]['resposta_correta']
        app.dicionario_valores_alternativas_corretas[4] = lista_criada[4]['alternativas'][resposta_correta]
        app.dicionario_enunciado[4]                  = lista_criada[4]['enunciado']

        self.enunciado        = lista_criada[4]['enunciado']
        self.resposta_correta = lista_criada[4]['resposta_correta']
        self.alternativas     = lista_criada[4]['alternativas']
        self.alternativa_a    = self.alternativas['a']
        self.alternativa_b    = self.alternativas['b']
        self.alternativa_c    = self.alternativas['c']
        self.alternativa_d    = self.alternativas['d']
        self.alternativa_e    = self.alternativas['e']

        self.ids.prova5_enunciado.text    = str(self.enunciado)
        self.ids.prova5_alternativa1.text = str(self.alternativa_a)
        self.ids.prova5_alternativa2.text = str(self.alternativa_b)
        self.ids.prova5_alternativa3.text = str(self.alternativa_c)
        self.ids.prova5_alternativa4.text = str(self.alternativa_d)
        self.ids.prova5_alternativa5.text = str(self.alternativa_e)


    def salvando_os_dados_do_usuario(self, resposta_marcada):
        app = MDApp.get_running_app()
        lista_criada = app.lista_exercicios_selecionados
        app.dicionario_marcada[4] = resposta_marcada
        valor_resposta_marcada    = lista_criada[4]['alternativas'][resposta_marcada]
        app.dicionario_valores_alternativas_marcadas[4] = valor_resposta_marcada
        MDApp.get_running_app().root.current = 'correcao1'

    def voltar(self):
        MDApp.get_running_app().root.current = "menu"  

class Correcao1(Screen):
    def __init__(self, **kwargs):
        super(Correcao1, self).__init__(**kwargs)
        
        app = MDApp.get_running_app()
        self.minhas_respostas     = app.dicionario_valores_alternativas_marcadas
        self.alternativa_corretas = app.dicionario_valores_alternativas_corretas
        self.meus_enunciados      = app.dicionario_enunciado

    def pegando_respostas(self):
        #colocando as respostas do usuário
        self.ids.resposta_marcada1.text = 'Altenativa assinalada :' + self.minhas_respostas[0]

        #colocando enunciado
        self.ids.enunciado1.text = '1) ' + self.meus_enunciados[0]

        #colocando alternativas corretas
        self.ids.resposta_correta1.text = 'Altenativa correta :' + self.alternativa_corretas[0]

    
    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Correcao2(Screen):
    def __init__(self, **kwargs):
        super(Correcao2, self).__init__(**kwargs)
        
        app = MDApp.get_running_app()
        self.minhas_respostas     = app.dicionario_valores_alternativas_marcadas
        self.alternativa_corretas = app.dicionario_valores_alternativas_corretas
        self.meus_enunciados      = app.dicionario_enunciado

    def pegando_respostas(self):
        #colocando as respostas do usuário
        self.ids.resposta_marcada2.text = 'Altenativa assinalada :' + self.minhas_respostas[1]

        #colocando enunciado
        self.ids.enunciado2.text = '2) ' + self.meus_enunciados[1]

        #colocando alternativas corretas
        self.ids.resposta_correta2.text = 'Altenativa correta :' + self.alternativa_corretas[1]


class Correcao3(Screen):
    def __init__(self, **kwargs):
        super(Correcao3, self).__init__(**kwargs)
        
        app = MDApp.get_running_app()
        self.minhas_respostas     = app.dicionario_valores_alternativas_marcadas
        self.alternativa_corretas = app.dicionario_valores_alternativas_corretas
        self.meus_enunciados      = app.dicionario_enunciado

    def pegando_respostas(self):
        #colocando as respostas do usuário
        self.ids.resposta_marcada3.text = 'Altenativa assinalada :' + self.minhas_respostas[2]

        #colocando enunciado
        self.ids.enunciado3.text = '2) ' + self.meus_enunciados[2]

        #colocando alternativas corretas
        self.ids.resposta_correta3.text = 'Altenativa correta :' + self.alternativa_corretas[2]

class Correcao4(Screen):
    def __init__(self, **kwargs):
        super(Correcao4, self).__init__(**kwargs)
        
        app = MDApp.get_running_app()
        self.minhas_respostas     = app.dicionario_valores_alternativas_marcadas
        self.alternativa_corretas = app.dicionario_valores_alternativas_corretas
        self.meus_enunciados      = app.dicionario_enunciado

    def pegando_respostas(self):
        #colocando as respostas do usuário
        self.ids.resposta_marcada4.text = 'Altenativa assinalada :' + self.minhas_respostas[3]

        #colocando enunciado
        self.ids.enunciado4.text = '2) ' + self.meus_enunciados[3]

        #colocando alternativas corretas
        self.ids.resposta_correta4.text = 'Altenativa correta :' + self.alternativa_corretas[3]

class Correcao5(Screen):
    def __init__(self, **kwargs):
        super(Correcao5, self).__init__(**kwargs)
        
        app = MDApp.get_running_app()
        self.minhas_respostas     = app.dicionario_valores_alternativas_marcadas
        self.alternativa_corretas = app.dicionario_valores_alternativas_corretas
        self.meus_enunciados      = app.dicionario_enunciado

    def pegando_respostas(self):
        #colocando as respostas do usuário
        self.ids.resposta_marcada5.text = 'Altenativa assinalada :' + self.minhas_respostas[4]

        #colocando enunciado
        self.ids.enunciado5.text = '2) ' + self.meus_enunciados[4]

        #colocando alternativas corretas
        self.ids.resposta_correta5.text = 'Altenativa correta :' + self.alternativa_corretas[4]

MainApp().run()