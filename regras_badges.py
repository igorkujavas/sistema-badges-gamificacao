def verificar_badge(pontos):
    if pontos >= 100:
        return "Ouro"
    elif pontos >= 50:
        return "prata"
    else:
        return "Bronze"