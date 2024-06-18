data_atual = "2024-01-01"
medicamentos = ["Aspirina", "Paracetamol", "Ibuprofeno", "Dipirona", "Amoxicilina"]
datas_validade = ["2023-05-01", "2024-01-15", "2022-12-30", "2023-11-20", "2025-06-10"]

def comparar_datas(data1, data2):
    ano1, mes1, dia1 = data1.split('-')
    ano2, mes2, dia2 = data2.split('-')
    if ano1 < ano2:
        return -1
    elif ano1 > ano2:
        return 1
    else:
        if mes1 < mes2:
            return -1
        elif mes1 > mes2:
            return 1
        else:
            if dia1 < dia2:
                return -1
            elif dia1 > dia2:
                return 1
            else:
                return 0

medicamentos_vencidos = []
for nome, data_validade in zip(medicamentos, datas_validade):
    if comparar_datas(data_validade, data_atual) == -1:
        medicamentos_vencidos.append((nome, data_validade))

print(f"Data atual: {data_atual}")

if medicamentos_vencidos:
    print("Medicamentos vencidos:")
    for nome, data in medicamentos_vencidos:
        print(f"{nome}: {data}")
else:
    print("Nenhum medicamento vencido.")

print(f"Quantidade de medicamentos vencidos: {len(medicamentos_vencidos)}")
