from front_end import layout
import back_end
import PySimpleGUI as sg

window = sg.Window('Nitrotec', layout)
event, values = window.read()

while True:
    if event == sg.WINDOW_CLOSED or event == 'sair_key':
        break
