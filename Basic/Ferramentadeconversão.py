# fahrenheit = (celsius * 9/5) + 32
#celsius = (fahrenheit - 32) * 5/9


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature, unit):
    if unit.lower() == 'c':
        return celsius_to_fahrenheit(temperature)
    elif unit.lower() == 'f':
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Unidade desconhecida. Use 'C' ou 'F'.")

temperature = float(input("Digite a temperatura: "))
unit = input("Digite a unidade (C ou F): ")

resultado = convert_temperature(temperature, unit)

if unit.lower() == 'c':
    print(f"{temperature}°C é igual a {resultado}°F")
else:
    print(f"{temperature}°F é igual a {resultado}°C")
