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

    def adicionaMaoObra(self):
        pass
    def editarMaoObra(self):
        pass
    def gerarRelatorio(self):
        pass
    def salvarRelatorio(self):
        pass
    def abrirRelatorio(self):
        pass

if __name__ == "__main__":
    carlos = User()
    carlos.adcionaMaterial('batata', 75)

    carlos.editarMaterial(1, "maca do amor", 15)