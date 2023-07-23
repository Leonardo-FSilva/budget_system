import PySimpleGUI as sg
from pathlib import Path
import json
from back_end import User

DATA = Path(__file__).parent.parent / "config\data.json"

carlos = User()

with open(DATA, 'r') as file:
    relatorio = json.load(file)

col1 = sg.Column([
            [sg.Frame('Informações',
                [[sg.Text(), sg.Column([[sg.Text('cliente empresa:')],
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
                ], size=(297, 330), pad=(0, 0))]])],

            [sg.Frame('Ações:', [
                [sg.Column([[sg.Button('Editar Material'), sg.Button('Editar mão de obra')],
                [sg.Button('Remover linha'), sg.Input(key='linha_indice' ,size=5), sg.Radio('Mat.', 'removelinha', key='seletor_remove_linhas_mat'), sg.Radio('M. Obra.', 'removelinha', key='seletor_remove_linhas_mobra')],
                                   
                [sg.Frame('Coeficientes', [
                    [sg.Text('Comissão: '), sg.Input(key='comissao', size=(7), default_text=str(relatorio['coeficientes']['comissao']).replace('.', ','))],
                    [sg.Text('Imposto: '), sg.Input(key='imposto', size=(7), default_text=str(relatorio['coeficientes']['impostos']).replace('.', ','))],
                    [sg.Text('Coef. mão de obra: '), sg.Input(key='mobra_coeficiente', size=(7), default_text=str(relatorio['coeficientes']['maodeobra']).replace('.', ','))],
                    [sg.Text('Corf. material: '), sg.Input(key='material_coeficiente', size=(7), default_text=str(relatorio['coeficientes']['material']).replace('.', ','))],
                    [sg.Text('Coef. estrutura: '), sg.Input(key='estrutura_coeficiente', size=(7), default_text=str(relatorio['coeficientes']['coeficientedeestrutura']).replace('.', ','))],
                    [sg.Button('Alterar configurações') ]])],                  
                [sg.Button('Gerar relatorio')]], size=(310,290), pad=(0, 0))]])]])

col2 = sg.Column([
    [sg.Frame('Mão de obra',
        [[sg.Text('Descrição:', size=(88, 1)), sg.Text('Valor R$:')],
        [sg.InputText(key='trab_descricao', size=(100, 1)),
        sg.InputText(key='trab_valor', size=(10, 1)),
        sg.Button('Adicionar Trabalho', key='add_trabalho_key')],
        
        [sg.Multiline(key='tra_multiline', default_text=((carlos.gerarRelatorio())[0]),font=('Courier', 8), size=(128, 15))]])],

    [sg.Frame('Material',
        [[sg.Text('Descrição:', size=(88, 1)), sg.Text('Valor R$:', )],
        [sg.InputText(key='mat_descricao', size=(100, 1)), sg.InputText(key='mat_valor', size=(10, 1)), sg.Button(' Adicionar Material', key='add_material_key')],
        [sg.Multiline(key='mat_multiline',default_text=((carlos.gerarRelatorio())[1]),font=('Courier', 8), size=(128, 15))]])]])

layout = [[col1, col2]]

if __name__ == '__main__':
    window = sg.Window('Nitrotec', layout)
    event, values = window.read()

    while True:
        if event == sg.WINDOW_CLOSED or event:
            break


