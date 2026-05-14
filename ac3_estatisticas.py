# Avaliação Continuada 3 - 1 ponto
# PROJETO DE VENDAS - parte 1
# Exercicios de estatisticas de vendas.
# Entrega - dia 17/05/2026

import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pemalta1410",
        database="projeto_vendas_eletronicos_unifecaf"
    )


def total_vendas_periodo():
    conexao = conectar()
    cursor = conexao.cursor()

    data_inicio = input("Digite a data inicial (AAAA-MM-DD): ")
    data_fim = input("Digite a data final (AAAA-MM-DD): ")

    sql = """
    SELECT SUM(valor_final)
    FROM vendas
    WHERE DATE(data_e_hora) BETWEEN %s AND %s
    """

    cursor.execute(sql, (data_inicio, data_fim))
    total = cursor.fetchone()[0] or 0

    print(f"\nTotal de vendas de {data_inicio} até {data_fim}: R$ {total:.2f}")

    cursor.close()
    conexao.close()



def qtd_vendas_por_vendedor():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_vendedor, COUNT(*) 
        FROM vendas 
        GROUP BY id_vendedor
    """)

    resultados = cursor.fetchall()

    for v in resultados:
        print(f"Vendedor {v[0]} → {v[1]} vendas")

    cursor.close()
    conexao.close()


def ticket_medio_geral():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT AVG(valor_final) FROM vendas")
    resultado = cursor.fetchone()[0] or 0

    print(f" Ticket médio geral: R$ {resultado:.2f}")

    cursor.close()
    conexao.close()


def ticket_medio_por_vendedor():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_vendedor, AVG(valor_final)
        FROM vendas
        GROUP BY id_vendedor
    """)

    for v in cursor.fetchall():
        print(f"Vendedor {v[0]} → R$ {v[1]:.2f}")

    cursor.close()
    conexao.close()


def produto_mais_vendido_qtd():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, SUM(quantidade)
        FROM vendas_produtos
        GROUP BY id_produto
        ORDER BY SUM(quantidade) DESC
        LIMIT 1
    """)

    r = cursor.fetchone()
    print(f" Produto {r[0]} → {r[1]} unidades")

    cursor.close()
    conexao.close()


def produto_mais_rentavel_valor():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, SUM(valor_total)
        FROM vendas_produtos
        GROUP BY id_produto
        ORDER BY SUM(valor_total) DESC
        LIMIT 1
    """)

    r = cursor.fetchone()
    print(f" Produto {r[0]} → R$ {r[1]:.2f}")

    cursor.close()
    conexao.close()


def total_descontos_aplicados():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT SUM(desconto) FROM vendas")
    total = cursor.fetchone()[0] or 0

    print(f" Total descontos: R$ {total:.2f}")

    cursor.close()
    conexao.close()


def percentual_desconto_medio():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT (SUM(desconto) / SUM(valor_final)) * 100
        FROM vendas
    """)

    p = cursor.fetchone()[0] or 0

    print(f" Desconto médio: {p:.2f}%")

    cursor.close()
    conexao.close()


def faturamento_por_dia():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT DATE(data_e_hora), SUM(valor_final)
        FROM vendas
        GROUP BY DATE(data_e_hora)
    """)

    for d in cursor.fetchall():
        print(f"{d[0]} → R$ {d[1]:.2f}")

    cursor.close()
    conexao.close()


def top_3_vendedores_faturamento():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_vendedor, SUM(valor_final)
        FROM vendas
        GROUP BY id_vendedor
        ORDER BY SUM(valor_final) DESC
        LIMIT 3
    """)

    for v in cursor.fetchall():
        print(f"Vendedor {v[0]} → R$ {v[1]:.2f}")

    cursor.close()
    conexao.close()


def menu_relatorios():

    opcoes = {
        "1": ("Total de vendas", total_vendas_periodo),
        "2": ("Qtd vendas por vendedor", qtd_vendas_por_vendedor),
        "3": ("Ticket médio geral", ticket_medio_geral),
        "4": ("Ticket médio por vendedor", ticket_medio_por_vendedor),
        "5": ("Produto mais vendido", produto_mais_vendido_qtd),
        "6": ("Produto mais rentável", produto_mais_rentavel_valor),
        "7": ("Total de descontos", total_descontos_aplicados),
        "8": ("Percentual médio desconto", percentual_desconto_medio),
        "9": ("Faturamento por dia", faturamento_por_dia),
        "10": ("Top 3 vendedores", top_3_vendedores_faturamento),
    }

    while True:
        print("\n=== MENU RELATÓRIOS ===")

        for k, v in opcoes.items():
            print(f"{k} - {v[0]}")

        print("0 - sair")

        escolha = input("\nEscolha: ").strip()

        if escolha == "0":
            break

        if escolha in opcoes:
            print("\n" + "="*30)
            print(opcoes[escolha][0])
            print("="*30)

            opcoes[escolha][1]()  

        else:
            print(" Opção inválida")


if __name__ == "__main__":
    menu_relatorios()