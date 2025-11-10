NOMES_MESES = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

DIAS_POR_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dia(dia, mes, ano):
    if not (-10000 <= ano <= 10000):
        return "Data Invalida"
    if not (1 <= mes <= 12):
        return "Data Invalida"
    max_dias_no_mes = DIAS_POR_MES[mes - 1]
    if not (1 <= dia <= max_dias_no_mes):
        return "Data Invalida"

    dia_formatado = f"{dia:02d}"
    mes_formatado = NOMES_MESES[mes - 1]
    return f"{dia_formatado} de {mes_formatado} de {ano}"
