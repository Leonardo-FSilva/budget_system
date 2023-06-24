import PySimpleGUI as sg

class Item:
    def __init__(self):
        self.tra_description = ''
        self.tra_value = ''
        self.tra_report = {'desc':[], 'val':[]}

        self.mat_description = ''
        self.mat_value = ''
        self.mat_report = {'desc':[], 'val':[]}

    def saving_list(self, type):
        if type == 'trabalho':
            self.tra_report['desc'].append(self.tra_description)
            self.tra_report['val'].append(self.tra_value)
        else:
            self.mat_report['desc'].append(self.mat_description)
            self.mat_report['val'].append(self.mat_value)

class ProgramWindows:
    def __init__(self):
        sg.theme('DarkBlue')
        self.col1 = sg.Column([
            [sg.Frame('Informações', 
                      [
                [sg.Text(), sg.Column([[sg.Text('Nome cliente:')],
                [sg.Input(key='nome_cliente_key', size=(30,1))],
                [sg.Text('Estado:')],
                [sg.Input(key='estado_key', size=(30,1))],
                [sg.Text('Cidade:')],
                [sg.Input(key='cidade_key', size=(30,1))],
                [sg.Text('Telefone:')],
                [sg.Input(key='telefone_key', size=(30,1))],
                [sg.Text('E-mail:')],
                [sg.Input(key='e-mail_key', size=(30,1))],
                [sg.Text('Responsavel:')],
                [sg.Input(key='responsavel_key', size=(30,1))]
                ], size=(235,350), pad=(0,0))]
                ])], 
            
            [sg.Frame('Ações:',
                      [
                [sg.Column([[sg.Button('Gerar relatorio'), sg.Button('Configurações'), sg.Button('Sair', key='sair_key'), ]], size=(250,45), pad=(0,0))]
                ])]], pad=(0,0))
                             
        self.col2 = sg.Column([
            [sg.Frame('Mão de obra',
                [
                    [sg.Text('Descrição:', size=(88,1)), sg.Text('Valor R$:')],
                    [sg.InputText(key='trab_descricao', size=(100,1)), sg.InputText(key='trab_valor', size=(10,1)), sg.Button('Adicionar Trabalho', key='add_trabalho_key')],
                    [sg.Multiline(key='tra_multiline', size=(128, 15))]])],

            [sg.Frame('Material',
                [
                    [sg.Text('Descrição:', size=(88,1)), sg.Text('Valor R$:',)],
                    [sg.InputText(size=(100,1)), sg.InputText(size=(10,1)), sg.Button(' Adicionar Material', key='add_material_key')],
                    [sg.Multiline(size=(128, 15))]
                    ])]])

        self.layout = [[self.col1, self.col2]]
        self.window = sg.Window('Nitrotec', self.layout)

    def add_itens(self):
        item.saving_list()

    def calculate(self):
        pass

    def make_report():
        pass

    def execute(self): 
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'sair_key':
                break

            elif event == 'add_trabalho_key':
                program.add_itens(type='trabalho')

            elif event == 'add_material_key':
                program.add_itens(type='material')

            elif event == 'Gerar relatorio':
                program.make_report()

if __name__ == '__main__':
    item = Item()
    program = ProgramWindows()
    program.execute()
