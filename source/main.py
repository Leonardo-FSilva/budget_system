import PySimpleGUI as sg

class Item:
    def __init__(self):
        self.tra_report = {'desc': [], 'val': []}
        self.mat_report = {'desc': [], 'val': []}

    def saving_list(self, desc, valor, type):
        if type == 'trabalho':
            self.tra_report['desc'].append(desc)
            self.tra_report['val'].append(valor)
        else:
            self.mat_report['desc'].append(desc)
            self.mat_report['val'].append(valor)

class ProgramWindows:
    def __init__(self):
        sg.theme('DarkBlue')
        self.col1 = sg.Column([
            [sg.Frame('Informações',
                [
                    [sg.Text(), sg.Column([[sg.Text('cliente empresa:')],
                                           [sg.Input(key='nome_cliente_key', size=(30, 1))],
                                           [sg.Text('Estado:')],
                                           [sg.Input(key='estado_key', size=(30, 1))],
                                           [sg.Text('Cidade:')],
                                           [sg.Input(key='cidade_key', size=(30, 1))],
                                           [sg.Text('Telefone:')],
                                           [sg.Input(key='telefone_key', size=(30, 1))],
                                           [sg.Text('E-mail:')],
                                           [sg.Input(key='e-mail_key', size=(30, 1))],
                                           [sg.Text('Responsavel:')],
                                           [sg.Input(key='responsavel_key', size=(30, 1))]
                                           ], size=(235, 350), pad=(0, 0))]
                     ])],

            [sg.Frame('Ações:',
                      [
                          [sg.Column([[sg.Button('Gerar relatorio'), sg.Button('Configurações'),
                                        sg.Button('Sair', key='sair_key'), ]], size=(250, 45), pad=(0, 0))]
                           ])]])

        self.col2 = sg.Column([
            [sg.Frame('Mão de obra',
                       [
                           [sg.Text('Descrição:', size=(88, 1)), sg.Text('Valor R$:')],
                           [sg.InputText(key='trab_descricao', size=(100, 1)),
                            sg.InputText(key='trab_valor', size=(10, 1)),
                            sg.Button('Adicionar Trabalho', key='add_trabalho_key')],
                           [sg.Multiline(key='tra_multiline', size=(128, 15))]
                       ]
                       )],

            [sg.Frame('Material',
                       [[sg.Text('Descrição:', size=(88, 1)), sg.Text('Valor R$:', )],
                        [sg.InputText(key='mat_descricao', size=(100, 1)),
                         sg.InputText(key='mat_valor', size=(10, 1)),
                         sg.Button(' Adicionar Material', key='add_material_key')],
                        [sg.Multiline(key='mat_multiline', size=(128, 15))]])]
        ])

        self.layout = [[self.col1, self.col2]]
        self.window = sg.Window('Nitrotec', self.layout)

    def add_itens(self, desc, valor, type):
        item.saving_list(desc, valor, type)

    def calculate(self):
        # Realize os cálculos necessários com base nos itens adicionados
        pass

    def make_report(self, report):
        # Gere o relatório com base nos itens adicionados e nos cálculos realizados

        ### nao é possivel referenciar coisas da janela que teoricamente nao foram criadas ainda (codigo futuro)

        sg.popup_scrolled(report, title='Relatório', size=(110, 25))

    def execute(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'sair_key':
                break

            elif event == 'add_trabalho_key':
                self.add_itens(values['trab_descricao'], values['trab_valor'], 'trabalho')
                desc = values['trab_descricao']
                val = values['trab_valor']
                self.window['tra_multiline'].print(
                    "{: <3}- {: <110}{: >9}".format(str(len(item.tra_report['desc'])), desc, val), font=('Courier New', 9))

            elif event == 'add_material_key':
                self.add_itens(values['mat_descricao'], values['mat_valor'], 'material')
                desc = values['mat_descricao'][:100]
                val = values['mat_valor']
                self.window['mat_multiline'].print(
                    "{: <3}{: <110}{: >9}".format(str(len(item.mat_report['desc'])), desc, val), font=('Courier New', 9))

            elif event == 'Gerar relatorio':
                self.calculate()

                report = ("Relatório: {}".format(values['nome_cliente_key']))       
                report += ('\n{} - {}'.format(values['estado_key'], values['cidade_key']))
                report += ('\nSr {} telefone: {}'.format(values["responsavel_key"], values["telefone_key"]))
                report += ('E-mail: {}\n\n'.format(values["e-mail_key"]))

                report += "Trabalho:\n"
                for i in range(len(item.tra_report['desc'])):
                    desc = item.tra_report['desc'][i][:100].ljust(100)
                    val = item.tra_report['val'][i][:20].rjust(20)
                    report += ("{}{}{}\n".format(i, desc, val))

                report += "\nMaterial:\n"
                for i in range(len(item.mat_report['desc'])):
                    desc = item.mat_report['desc'][i][:100].ljust(100)
                    val = item.mat_report['val'][i][:20].rjust(20)
                    report += ("{}{}{}\n".format(i, desc, val))
                self.make_report(report)

if __name__ == '__main__':
    item = Item()
    program = ProgramWindows()
    program.execute()