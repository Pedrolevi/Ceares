# LingCeara — Projeto 1

Linguagem esotérica baseada no [Dicionário Cearês da ABIH-CE](https://www.abih-ce.com.br/dicionario-ceares).

## 👥 Integrantes da Equipe
- Nome: [Nome do Aluno 1] - Matrícula: [Matrícula]
- Nome: [Nome do Aluno 2] - Matrícula: [Matrícula]
- Nome: [Nome do Aluno 3] - Matrícula: [Matrícula]

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

