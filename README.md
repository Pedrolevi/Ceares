# Cearês — Projeto 1

Linguagem esotérica baseada no [Dicionário Cearês da ABIH-CE](https://www.abih-ce.com.br/dicionario-ceares).

## 👥 Integrantes da Equipe
- Nome: PEDRO LEVI MOURA XIMENES - Matrícula: 592812
- Nome: KLAVIA MIRANDA RODRIGUES - Matrícula: 592814
- Nome: JAMESSON ALBERTO TOME FERREIRA - Matrícula: 596028
- Nome: GUSTAVO MENESES XAVIER ABREU CARDOSO - Matrícula: 596031
- Nome: THALISIA PEREIRA OLIVEIRA - Matrícula: 558447
- Nome: LAYNY VITORIA CARLOS DE MORAIS - Matrícula: 558448


## Arquivos do Projeto 1
- `tradutor.py`: Tradutor de código `.ce` para Python `.py`.
- `DOCUMENTACAO.md`: Documentação das regras, tipos e comandos do Projeto 1.
- `testar.py`: Script para testar os 3 programas automaticamente.
- `programas/`:
  - `ola_mundo.ce`: "Hello World!"
  - `99_garrafas.ce`: "99 garrafas de cerveja"
  - `tabuada.ce`: Tabuada do 7
- `exemplos_gerados/`: Arquivos Python gerados após a tradução.

## Como Executar
```bash
# Testar todos os 3 programas de uma vez:
python testar.py

# Ou executar individualmente:
python tradutor.py programas/ola_mundo.ce --run
python tradutor.py programas/99_garrafas.ce --run
python tradutor.py programas/tabuada.ce --run
```

