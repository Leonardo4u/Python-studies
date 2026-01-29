

def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    """
    Cria o sandiwiche com os ingredientes fornecidos.
    
    args:
        bread_type(str): uma string que representa o tipo de pão
        filling(str): uma cadeia de caracteres para o recheio principal do sanduíche
        cheese(none): uma cadeia de caracteres opcional para o tipo de queijo, cujo padrão é "nenhum"
        toasted(boolean): um booleano opcional que indica se o sanduíche é tostado, cujo padrão é False
    """

    if cheese is None:
        cheese = "nenhum"

    sandwich = {
        "bread_type": bread_type,
        "filling": filling,
        "cheese": cheese,
        "toasted": toasted
    }

    return sandwich

# Exemplo de uso da função make_sandwich
sandwich1 = make_sandwich("integral", "frango", "cheddar", True)
sandwich2 = make_sandwich("ciabatta", "vegetariano")    
sandwich3= make_sandwich("baguete", "presunto", toasted=True)   

print(sandwich1)
print(sandwich2)
print(sandwich3)