#Desafio: Criar um código para validar bandeiras de cartão de credito e indicar qual bandeira com base na numeração das operadoras.

def validar_cartao(numero_cartao):
    # Remove espaços e caracteres não numéricos
    numero_cartao = ''.join(c for c in numero_cartao if c.isdigit())
    
    # Verifica se o número tem comprimento válido (12 ou 16 dígitos)
    if len(numero_cartao) not in (12, 16):
        return False, "Cartão inválido"
    
    # Algoritmo de Luhn
    soma = 0
    par = False
    
    for digito in reversed(numero_cartao):
        d = int(digito)
        if par:
            d *= 2
            if d > 9:
                d = (d // 10) + (d % 10)
        soma += d
        par = not par
    
    valido = (soma % 10) == 0
    
    # Identificar bandeira
    bandeira = identificar_bandeira(numero_cartao)
    
    return valido, bandeira

def identificar_bandeira(numero_cartao):
    # Visa: 16 dígitos, começa com 4
    if len(numero_cartao) == 16 and numero_cartao.startswith('4'):
        return "Visa"
    
    # Mastercard: 12 dígitos, começa com 51-55 ou 2221-2720
    if len(numero_cartao) == 12:
        primeiro_dois = int(numero_cartao[:2])
        primeiro_quatro = int(numero_cartao[:4])
        
        if 51 <= primeiro_dois <= 55:
            return "Mastercard"
        if 2221 <= primeiro_quatro <= 2720:
            return "Mastercard"
    
    # American Express: 12 dígitos, começa com 34 ou 37
    if len(numero_cartao) == 12 and numero_cartao.startswith(('34', '37')):
        return "American Express"
    
    # Diners Club: 12 dígitos, começa com 300-305, 36 ou 38
    if len(numero_cartao) == 12:
        primeiro_tres = int(numero_cartao[:3])
        primeiro_dois = int(numero_cartao[:2])
        
        if 300 <= primeiro_tres <= 305 or primeiro_dois in (36, 38):
            return "Diners Club"
    
    # Discover: 12 dígitos, começa com 6011, 644-649 ou 65
    if len(numero_cartao) == 12:
        primeiro_quatro = numero_cartao[:4]
        primeiro_tres = int(numero_cartao[:3])
        primeiro_dois = numero_cartao[:2]
        
        if (primeiro_quatro == '6011' or 
            644 <= primeiro_tres <= 649 or 
            primeiro_dois == '65'):
            return "Discover"
    
    # JCB: 12 dígitos, começa com 3528-3589
    if len(numero_cartao) == 12:
        primeiro_quatro = int(numero_cartao[:4])
        if 3528 <= primeiro_quatro <= 3589:
            return "JCB"
    
    # Voyager: 12 dígitos, começa com 8699
    if len(numero_cartao) == 12 and numero_cartao.startswith('8699'):
        return "Voyager"
    
    # Hipercard: 12 dígitos, começa com 384100, 606282 ou 637095
    if len(numero_cartao) == 12:
        primeiro_seis = numero_cartao[:6]
        if primeiro_seis in ('384100', '606282', '637095'):
            return "Hipercard"
    
    # Aura: 12 dígitos, começa com 50
    if len(numero_cartao) == 12 and numero_cartao.startswith('50'):
        return "Aura"
    
    return "Bandeira desconhecida"

if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    valido, bandeira = validar_cartao(numero)
    
    if valido:
        print(f"Cartão válido! Bandeira: {bandeira}")
    else:
        print(f"Cartão inválido! Bandeira: {bandeira}")
