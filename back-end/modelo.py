from config import *

class Mouse(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    marca = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    peso = db.Column(db.String(254))
    dpi = db.Column(db.String(254))


    # método para expressar a pessoa em forma de texto
    def __str__(self):
        # return str(self.id)+") "+ self.nome + ", " +\
        #     self.email + ", " + self.telefone
        return f'''
                --- Mouse [{self.id}] --- 
                Nome [{self.nome}]      
                Marca [{self.marca}]    
                Cor [{self.cor}]        
                Peso [{self.peso}]      
                DPI [{self.dpi}]        
                __________________________
                '''
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca,
            "cor": self.cor,
            "peso": self.peso,
            "dpi": self.dpi
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Mouse
    m1 = Mouse(nome= "G403",marca="Logitech",cor="Preto",peso="220g",dpi="12000")
    m2 = Mouse(nome= "Pulsefire Core",marca="HyperX",cor="Preto",peso="220g",dpi="6.200")     
    
    # persistir
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()
     
    # exibir o mouse
    print(m2)

    # exibir o mouse no format json
    print(m2.json())