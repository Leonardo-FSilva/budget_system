from pathlib import Path
import json

MATERIAIS = Path(__file__).parent.parent / "config\materiais.json"
MAODEOBRA = Path(__file__).parent.parent / "config\maodeobra.json"

class User:
    def adcionaMaterial(self, desc, val):
        with open(MATERIAIS, 'r') as file:
            relatoriomp = json.load(file)

        relatoriomp["index"].append(len(relatoriomp['index'])+1)
        relatoriomp["descricao"].append(desc)
        relatoriomp["valor"].append(val)

        with open(MATERIAIS, 'w') as file:
            json.dump(relatoriomp, file, indent=4)
    
    def editarMaterial(self, ind, desc, val):
        with open(MATERIAIS, 'r') as file:
            relatoriomp =json.load(file)
        
        relatoriomp["descricao"][ind-1] = desc
        relatoriomp["valor"][ind-1] = val

        with open(MATERIAIS, 'w') as file:
            json.dump(relatoriomp, file, indent=4)

    def adicionaMaoObra(self, desc, val):
        with open(MAODEOBRA, 'r') as file:
            relatoriomo = json.load(file)

        relatoriomo["index"].append(len(relatoriomo['index'])+1)
        relatoriomo["descricao"].append(desc)
        relatoriomo["valor"].append(val)

        with open(MAODEOBRA, 'w') as file:
            json.dump(relatoriomo, file, indent=4)
    
    def editarMaoObra(self, ind, desc, val):
        with open(MAODEOBRA, 'r') as file:
            relatoriomo =json.load(file)
        
        relatoriomo["descricao"][ind-1] = desc
        relatoriomo["valor"][ind-1] = val

        with open(MAODEOBRA, 'w') as file:
            json.dump(relatoriomo, file, indent=4)

    def gerarRelatorio(self):
        with open(MATERIAIS, 'w') as file:
            relatoriomp = json.load(file)
        
        relatoriomp_formatado = ''
        for iten in range(0, len(relatoriomp['index'])):
            relatoriomp_formatado += ('{}{}R${}\n}'.format(relatoriomp['index'][iten], relatoriomp['descricao'][iten], relatoriomp['valor'][iten]))

        with open(MAODEOBRA, 'w') as file:
            relatoriomo = json.load(file)
        
        relatoriomo_formatado = ''
        for iten in range(0, len(relatoriomo['index'])):
            relatoriomo_formatado += ('{}{}R${}\n}'.format(relatoriomo['index'][iten], relatoriomo['descricao'][iten], relatoriomo['valor'][iten]))


    def salvarRelatorio(self):
        pass
    def abrirRelatorio(self):
        pass

if __name__ == "__main__":
    carlos = User()
    #carlos.adcionaMaterial('batata', 75)

    #carlos.editarMaterial(1, "maca do amor", 15)