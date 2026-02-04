import random
import string

def cadastrarProduto(nome, categoria, preco, estoque, codigo):
    return {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque,
        "codigo": codigo
    }

# Funções para gerar dados aleatórios

def gerarNomeProduto():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

def gerarCategoria():
    return random.choice(["Eletrônico", "Alimento", "Roupa", "Limpeza"])

def gerarPreco():
    return round(random.uniform(10, 500), 2)

def gerarEstoque():
    return random.randint(0, 100)

def gerarCodigo():
    return f"PROD-{random.randint(1000, 9999)}"


# Lista para armazenar os produtos
produtos = []

# Gera 10 produtos automaticamente
for _ in range(10):
    produto = cadastrarProduto(
        gerarNomeProduto(),
        gerarCategoria(),
        gerarPreco(),
        gerarEstoque(),
        gerarCodigo()
    )

    produtos.append(produto)

# Análise dos produtos
for produto in produtos:
    print(produto)

    if produto["estoque"] < 10:
        print("⚠️ Estoque baixo")

    if produto["preco"] > 300:
        print("💰 Produto premium")

    print("-" * 40)
