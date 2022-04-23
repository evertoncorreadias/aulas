import PySimpleGUI as sg

class Tela:
	def __init__(self):
		layout =[
					  [sg.Text('nome'),sg.Input(size = (20, 1),key='nome')],
					  [sg.Text('idade'),sg.Input(size = (20, 1),key='idade')],
					  [sg.Checkbox('gmail',key='gmail'),sg.Checkbox('outlook',key='outlook')],
					  [sg.Text('sexo')],
					  [sg.Radio('masculino','sexos',key='masc'),sg.Radio('feminino','sexos',key='fem')],
					  [sg.Button('enviar dados')],
					  [sg.Output(size = (20, 15))]
		]
		
		self.janela = sg.Window('dados do usuario', layout)
		
		
	def iniciar(self):
		
		self.button,self.values = self.janela.Read()
		nome = self.values['nome']
		idade = self.values['idade']
		gmail = self.values['gmail']
		outlook = self.values['outlook']
		masc = self.values['masc']
		fem = self.values['fem']
		print(f'gmail:{gmail}')
		print(f'idade:{idade}')
		print(f'nome:{nome}')
		print(f'gmail:{gmail}')
		print(f'outlook:{outlook}')
		print(f'sexo masculino:{masc}')
		print(f'sexo feminino:{fem}')
				
		while True:
			
			event,self.values = self.janela.Read()		
			
			
			if event == WIN_CLOSED:
				break		
					
					
									
					
				
				
				
	
	
tela = Tela()
tela.iniciar()