import sys, os, re, argparse

def traduzir_expressao(expr):
    partes = re.split(r'("[^"]*"|\'[^\']*\')', expr)
    subst = [
        (r'\bARRETADO\b', 'True'), (r'\bARIADO\b', 'False'),
        (r'\bMAIS\b', '+'), (r'\bMENOS\b', '-'), (r'\bVEZES\b', '*'),
        (r'\bIGUAL A\b', '=='), (r'\bDIFERENTE DE\b', '!='),
        (r'\bMAIOR OU IGUAL A\b', '>='), (r'\bMENOR OU IGUAL A\b', '<='),
        (r'\bMAIOR QUE\b', '>'), (r'\bMENOR QUE\b', '<'),
    ]
    resultado = []
    for p in partes:
        if p.startswith(('"', "'")):
            resultado.append(p)
        else:
            for padrao, troca in subst:
                p = re.sub(padrao, troca, p, flags=re.IGNORECASE)
            resultado.append(p)
    return "".join(resultado)

def traduzir(codigo_fonte):
    linhas = codigo_fonte.splitlines()
    codigo_py, indent = [], 0
    iniciou, finalizou = False, False

    for num, raw in enumerate(linhas, 1):
        linha = raw.strip()
        if not linha or linha.startswith(("//", "#", "FUXICO:")):
            continue
        if not iniciou:
            if re.match(r'^EI\s+MACHO\s*,?\s*PRESTA\s+ATEN[CÇ][AÃ]O\s*!?$', linha, re.IGNORECASE):
                iniciou = True
                continue
            raise SyntaxError(f"Linha {num}: Deve iniciar com 'EI MACHO, PRESTA ATENÇÃO!'")
        if re.match(r'^CAB[OÔ]-SE\s+O\s+QUE\s+ERA\s+DOCE\s*!?$', linha, re.IGNORECASE):
            finalizou = True
            break

        # Declaração e Atribuição
        m = re.match(r'^EI\s+MACHO\s+([a-zA-Z_]\w*)\s+[EÉ]\s+UM\s+CABRA\s+([a-zA-Z_]\w*)\s+COM\s+(.+)$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"{m.group(1)} = {traduzir_expressao(m.group(3))}")
            continue
        m = re.match(r'^EI\s+MACHO\s+([a-zA-Z_]\w*)\s+[EÉ]\s+UM\s+CABRA\s+([a-zA-Z_]\w*)$', linha, re.IGNORECASE)
        if m:
            v_pad = '""' if m.group(2).upper() == "GASGUITO" else "0"
            codigo_py.append("    " * indent + f"{m.group(1)} = {v_pad}")
            continue
        m = re.match(r'^BOTE\s+(.+)\s+NO\s+QUENGO\s+DE\s+([a-zA-Z_]\w*)$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"{m.group(2)} = {traduzir_expressao(m.group(1))}")
            continue

        # Operações Aritméticas
        m = re.match(r'^BOTAR\s+PRA\s+MOER\s+([a-zA-Z_]\w*)\s+COM\s+(.+)$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"{m.group(1)} += {traduzir_expressao(m.group(2))}")
            continue
        m = re.match(r'^RANCAR\s+EM\s+([a-zA-Z_]\w*)\s+COM\s+(.+)$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"{m.group(1)} -= {traduzir_expressao(m.group(2))}")
            continue
        m = re.match(r'^ESTRIBAR\s+([a-zA-Z_]\w*)\s+COM\s+(.+)$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"{m.group(1)} *= {traduzir_expressao(m.group(2))}")
            continue

        # Saída (print)
        m = re.match(r'^GAITAR(?:\s+(.+))?$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"print({traduzir_expressao(m.group(1) or '')})")
            continue

        # Laço (while)
        m = re.match(r'^ARRUDIE\s+ENQUANTO\s+(.+)\s*:$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"while {traduzir_expressao(m.group(1))}:")
            indent += 1
            continue
        if re.match(r'^ACABOU\s+O\s+ARRODEIO$', linha, re.IGNORECASE):
            indent -= 1
            continue

        # Condicional (if / else)
        m = re.match(r'^SE\s+(.+)\s*:$', linha, re.IGNORECASE)
        if m:
            codigo_py.append("    " * indent + f"if {traduzir_expressao(m.group(1))}:")
            indent += 1
            continue
        if re.match(r'^A[IÍ]\s+DENTO\s*:$', linha, re.IGNORECASE):
            indent -= 1
            codigo_py.append("    " * indent + "else:")
            indent += 1
            continue
        if re.match(r'^V[OÔ]TE\s*!?$', linha, re.IGNORECASE):
            indent -= 1
            continue

        raise SyntaxError(f"Linha {num}: Comando não reconhecido: '{linha}'")

    if not iniciou: raise SyntaxError("Faltou o cabeçalho 'EI MACHO, PRESTA ATENÇÃO!'")
    if not finalizou: raise SyntaxError("Faltou o encerramento 'CABÔ-SE O QUE ERA DOCE!'")
    return "\n".join(codigo_py) + "\n"

def main():
    parser = argparse.ArgumentParser(description="Tradutor LingCeara - Projeto 1 (.ce -> .py)")
    parser.add_argument("arquivo", help="Arquivo fonte .ce")
    parser.add_argument("-o", "--saida", help="Arquivo de saída .py", default=None)
    parser.add_argument("-r", "--run", action="store_true", help="Executa o código após a tradução")
    args = parser.parse_args()

    arq_ce = args.arquivo
    if args.saida:
        arq_py = args.saida
    else:
        nome_base = os.path.basename(os.path.splitext(arq_ce)[0])
        os.makedirs("exemplos_gerados", exist_ok=True)
        arq_py = os.path.join("exemplos_gerados", nome_base + ".py")

    os.makedirs(os.path.dirname(arq_py) or ".", exist_ok=True)
    with open(arq_ce, "r", encoding="utf-8") as f:
        conteudo = f.read()

    codigo_gerado = traduzir(conteudo)
    with open(arq_py, "w", encoding="utf-8") as f:
        f.write(codigo_gerado)

    print(f"Traduzido com sucesso: {arq_ce} -> {arq_py}")
    if args.run:
        print(f"\n--- Executando {arq_py} ---")
        exec(codigo_gerado, {"__name__": "__main__"})

if __name__ == "__main__":
    main()

