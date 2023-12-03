def helpdesk(nome, titulo, descricao):
    Card = (
        f"Usuário: {nome}\n"
        f"Titulo: {titulo}\n"
        f"descrição: {descricao}"
    )
    return Card 

nome = input("digite o seu nome: ")
titulo = input("Titulo do seu problema: ")
descricao = input("Descreva seu problema com maior detalhes: ")

resultado = helpdesk(nome, titulo, descricao)

print(resultado)