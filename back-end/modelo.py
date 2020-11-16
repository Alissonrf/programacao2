from config import *

class Mouse(db.Model):
    # atributos da mouse
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    marca = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    peso = db.Column(db.String(254))
    dpi = db.Column(db.String(254))


    # método para expressar a mouse em forma de texto
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
    
class inspecaoRealizado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(254)) # data do exame
    resultado = db.Column(db.String(254)) # apenas o valor

    # mouse que fez o exame; não pode ser nulo (composição!)
    mouse_id = db.Column(db.Integer, db.ForeignKey(Mouse.id), nullable=False)
    mouse = db.relationship("Mouse")

    def __str__(self): # expressão da classe em forma de texto
        return f"{self.data}, {self.resultado}, " + \
            f"{str(self.mouse)}"

    def json(self):
        return {
            "id":self.id,
            "data":self.data,
            "resultado":self.resultado,
            "mouse_id":self.mouse_id,
            "mouse":self.mouse.json(),
        }

class EmprestimoMouse(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id interno
    codigo = db.Column(db.String(254)) # código do equipamento
    data_aquisicao = db.Column(db.String(254))
    data_emprestimo = db.Column(db.String(254)) # emprestado? se sim, desde quando?

    # atributo de chave estrangeira
    mouse_id = db.Column(db.Integer, db.ForeignKey(Mouse.id))
    # atributo de relacionamento, para acesso aos dados via objeto
    mouse = db.relationship("Mouse")

    def __str__(self): # expressão da classe em forma de texto
        s = f"EmprestimoMouse {self.codigo} adquirido em {self.data_aquisicao}"
        if self.mouse != None:
            s += f", emprestado para {self.mouse} desde {self.data_aquisicao}"
        return s

    def json(self):
        if self.mouse is None: # o Mouse não está emprestado?
            mouse_id = ""
            mouse = ""
            data_emprestimo = ""
        else: # o Mouse está emprestado!! :-)
            mouse_id = self.mouse_id
            mouse = self.mouse.json()
            data_emprestimo = self.data_emprestimo

        return {
            "id": self.id,
            "codigo": self.codigo,
            "data_aquisicao": self.data_aquisicao,
            "mouse_id": mouse_id,
            "mouse": mouse,
            "data_emprestimo": data_emprestimo
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

