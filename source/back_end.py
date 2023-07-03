from datetime import datetime
from pathlib import Path
import json

DATA = Path(__file__).parent.parent / "config\data.json"
NEW_FILE_PAHT = Path(__file__).parent.parent / "config"

class User:
    def adcionaMaterial(self, desc, val):
        with open(DATA, 'r') as file:
            relatoriomp = json.load(file)

        relatoriomp["material"]["index"].append(len(relatoriomp["material"]['index'])+1)
        relatoriomp["material"]["descricao"].append(desc)
        relatoriomp["material"]["valor"].append(val)

        with open(DATA, 'w') as file:
            json.dump(relatoriomp, file, indent=4)
    
    def editarMaterial(self, ind, desc, val):
        with open(DATA, 'r') as file:
            relatoriomp = json.load(file)
        
        relatoriomp["material"]["descricao"][ind-1] = desc
        relatoriomp["material"]["valor"][ind-1] = val

        with open(DATA, 'w') as file:
            json.dump(relatoriomp, file, indent=4)

    def adicionaMaoObra(self, desc, val):
        with open(DATA, 'r') as file:
            relatoriomo = json.load(file)

        relatoriomo["maodeobra"]["index"].append(len(relatoriomo["maodeobra"]['index'])+1)
        relatoriomo["maodeobra"]["descricao"].append(desc)
        relatoriomo["maodeobra"]["valor"].append(val)

        with open(DATA, 'w') as file:
            json.dump(relatoriomo, file, indent=4)
    
    def editarMaoObra(self, ind, desc, val):
        with open(DATA, 'r') as file:
            relatoriomo =json.load(file)
        
        relatoriomo["maodeobra"]["descricao"][ind-1] = desc
        relatoriomo["maodeobra"]["valor"][ind-1] = val

        with open(DATA, 'w') as file:
            json.dump(relatoriomo, file, indent=4)

    def gerarRelatorio(self, path_to_open=''):
        if path_to_open == '':
            with open(DATA, 'r') as file:
                relatoriomp = json.load(file)
                relatoriomo = json.load(file)
        else:
            with open(path_to_open, 'r+')as file:
                relatoriomp = json.load(file)
                relatoriomo = json.load(file)

        relatoriomp_formatado = ''
        for iten in range(0, len(relatoriomp["material"]['index'])):
            relatoriomp_formatado += ('{:<5}{:<120}R${}\n'.format(relatoriomp["material"]['index'][iten], relatoriomp["material"]['descricao'][iten], relatoriomp["material"]['valor'][iten]))
        
        relatoriomo_formatado = ''
        for iten in range(0, len(relatoriomo["maodeobra"]['index'])):
            relatoriomo_formatado += ('{:<5}{:<120}R${}\n'.format(relatoriomo["maodeobra"]['index'][iten], relatoriomo["maodeobra"]['descricao'][iten], relatoriomo["maodeobra"]['valor'][iten]))

    def salvarRelatorio(self):
        with open(DATA, 'r') as file:
            relatorio = json.load(file)
 

        relatorio_nome = '\{} - {}.json'.format(str(datetime.now())[0:10], relatorio["informacoes"]["cliente"][0:3])
        relatorio_nome = str(NEW_FILE_PAHT) + relatorio_nome

        try:
            new_file = open(relatorio_nome, 'w')
            json.dump(relatorio, new_file, indent=4)
        except:
            return print("Error: avise o leonardo...")
        finally:
            new_file.close()

    def abrirRelatorio(self, path):
        with open(path, "r") as file:
            self.gerarRelatorio(file)


if __name__ == "__main__":
    #carlos = User()
    #carlos.adcionaMaterial('batata', 75)
    #carlos.adcionaMaterial('macarrao', 50)
    #carlos.adcionaMaterial('uva', 15)
    #carlos.editarMaterial(1, "maca do amor", 15)
#
    #carlos.gerarRelatorio()

    #carlos.salvarRelatorio()
    pass