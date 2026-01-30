import random
import string

def cadastrarUser(nome, idade, email, senha, cpf):
    """
    Docstring for cadastrarUser
    
    nome: Description
    idade: Description
    email: Description
    senha: Description
    cpf: Description
    """

    return {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha,
        "cpf": cpf
    }

# Dados Aleatorios para Teste

def gerarNome():
    return ''.join(random.choices(string.ascii_lowercase, k=7)).capitalize()

def gerarIdade():
    return random.randint(18, 65)

def gerarEmail(nome):
    return f"{nome.lower()}@exemplo.com"

def gerarSenha():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def gerarCpf():
    return f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}"



user1 = cadastrarUser(
    "Leo", 21, "leogomesgiroti@gmail.com", "senha2929", "421.222.343-27"
)

# lista para armazenar os usuários
usuarios = []

# cria 4 usuários automaticamente
for _ in range(10):
    nome = gerarNome()

    usuario = cadastrarUser(
        nome,
        gerarIdade(),
        gerarEmail(nome),
        gerarSenha(),
        gerarCpf()
    )

    usuarios.append(usuario)

# usuário fixo
user1 = cadastrarUser(
    "Leo", 21, "leogomesgiroti@gmail.com", "senha2929", "421.222.343-27"
)

print(user1)

# imprime os usuários gerados
for usuario in usuarios:
    print(usuario)

    if usuario['idade'] > 30:
        print("Usuário maior de 30 anos")
        