from database import conectar

def criar_marca(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO marca(nome) VALUES (%s)",
        (nome,)
    )

    conn.commit()
    conn.close()


#def listar_marcas():



#def atualizar_marca(id, nome):



#def excluir_marca(id):
