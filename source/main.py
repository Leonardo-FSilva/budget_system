from front_end import layout
from back_end import User
import PySimpleGUI as sg


window = sg.Window('Nitrotec', layout)

carlos = User()
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'sair_key':
        break
    
    if event == 'Gerar relatorio':
        cliente = values['nome_cliente_key']
        estado = values['estado_key']
        cidade = values['cidade_key']
        telefone = values['telefone_key']
        email = values['mail_key']
        responsavel = values['responsavel_key']
        
        carlos.gerarRelatorio(cliente, estado, cidade, telefone, email, responsavel)

    if event == 'Alterar configurações':
        comissao = float((values['comissao']).replace(',','.'))
        imposto = float((values['imposto']).replace(',','.'))
        mobra = float((values['mobra_coeficiente']).replace(',','.'))
        material = float((values['material_coeficiente']).replace(',','.'))
        estrutura = float((values['estrutura_coeficiente']).replace(',','.'))
        carlos.alterarSetup(comissao, imposto, mobra, material, estrutura)

    if event == 'add_trabalho_key':
        try:
            carlos.adicionaMaoObra(values['trab_descricao'].upper(), values['trab_valor'])
            valor = carlos.gerarRelatorio()
            window['tra_multiline'].update(valor[0], font=('Courier', 8))
        except:
            sg.popup('erro ao executar ação')

    if event == 'add_material_key':
            carlos.adcionaMaterial(values['mat_descricao'].upper(), values['mat_valor'])
            valor = carlos.gerarRelatorio()
            window['mat_multiline'].update(valor[1], font=('Courier', 8))

    if event == 'Editar Material':
        window_edicao = sg.Window('Nitrotec', carlos.tela_editarlinha())
        while True:
            event, values = window_edicao.read()
            if event == sg.WINDOW_CLOSED:
               break
            if event == 'Editar linha':
                carlos.editarMaterial(int(values['editarlinha_ind']), values['editarlinha_des'], values['editarlinha_val'])
                window_edicao.close()
                valor = carlos.gerarRelatorio()
                window['mat_multiline'].update(valor[1], font=('Courier', 8))
    
    if event == 'Editar mão de obra':
        window_edicao = sg.Window('Nitrotec', carlos.tela_editarlinha())
        while True:
            event, values = window_edicao.read()
            if event == sg.WINDOW_CLOSED:
               break
            if event == 'Editar linha':
                carlos.editarMaoObra(int(values['editarlinha_ind']), values['editarlinha_des'], values['editarlinha_val'])
                window_edicao.close()
                valor = carlos.gerarRelatorio()
                window['tra_multiline'].update(valor[0], font=('Courier', 8))

    if event == 'Remover linha':
        try:
            if values['seletor_remove_linhas_mat']:
                tipo = 'material'
            elif values['seletor_remove_linhas_mobra']:
                tipo = 'maodeobra'

            carlos.removerLinha(tipo, int(values['linha_indice']))
            valor = carlos.gerarRelatorio()
            window['tra_multiline'].update(valor[0], font=('Courier', 8))
            window['mat_multiline'].update(valor[1], font=('Courier', 8))
        except:
            sg.popup('erro ao executar ação')