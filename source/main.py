from front_end import layout
from back_end import User
import PySimpleGUI as sg


window = sg.Window('Nitrotec', layout)
event, values = window.read()

carlos = User()

while True:
    if event == sg.WINDOW_CLOSED or event == 'sair_key':
        break
    if event == 'Gerar relatorio':
        pass
    if event == 'Alterar configurações':
        pass
    if event == 'add_trabalho_key':
        pass
    if event == 'add_material_key':
        carlos.adcionaMaterial(values['mat_descricao'], values['mat_valor'])
    
    if event == 'Editar material':
        pass
    if event == 'Editar mão de obra':
        pass
    