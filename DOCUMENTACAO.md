# Documentação da Linguagem LingCeara — Projeto 1

**Referência das gírias:** [Dicionário Cearês da ABIH-CE](https://www.abih-ce.com.br/dicionario-ceares)  
**Extensão dos arquivos:** `.ce`  
**Linguagem de destino:** Python 3 (`.py`)  
**Propósito:** Geral (Turing-completa)  

---

## 1. Visão Geral
A **LingCeara** é uma linguagem esotérica inspirada nas expressões típicas do Ceará. 

Para não ser apenas uma tradução direta do inglês:
- O programa começa com `EI MACHO, PRESTA ATENÇÃO!` e finaliza com `SÓ O MIOLO DA PIPOCA!`.
- Atribuições de variáveis são feitas "no quengo" (cabeça).
- O laço de repetição é o **Arrodeio** (`ARRUDIE ENQUANTO ... :`).
- O bloco condicional usa `AÍ DENTO :` para o ramo alternativo (*else*) e fecha com `VÔTE`.
- As operações aritméticas usam gírias cearenses (`DAR O GRAU EM`, `TRISCAR EM`, `BOTAR PRA MOER`).

---

## 2. Tipos de Dados Suportados

| Tipo LingCeara | Tipo Python | Significado no Cearês | Exemplo |
| :--- | :--- | :--- | :--- |
| **`ESTRIBADO`** | `int` | Pessoa cheia do dinheiro (inteiro) | `99`, `7` |
| **`GASGUITA`** | `str` | Voz fina e estridente (texto) | `"Hello World!"` |
| **`BUIÉ`** | `bool` | Café com leite / brincadeira | `ARRETADO` (True), `PAIA` (False) |

---

## 3. Comandos e Regras da Linguagem

### 3.1. Comentários (Fuxico)
Comentários são considerados fuxicos (fofocas) e são ignorados pelo tradutor:
- `FUXICO: texto do comentário`
- Também aceita `//` e `#`.

### 3.2. Declaração e Atribuição
- `EI MACHO <var> É UM CABRA <tipo> COM <valor>`
- `EI MACHO <var> É UM CABRA <tipo>` *(inicia vazio/zerado)*
- `BOTE <expressao> NO QUENGO DE <var>`

### 3.3. Operações Aritméticas e Expressões
- **Soma:** `DAR O GRAU EM <var> COM <valor>`
- **Subtração:** `TRISCAR EM <var> COM <valor>`
- **Multiplicação:** `BOTAR PRA MOER <var> COM <valor>`
- **Operadores em expressões:** `MAIS` (`+`), `MENOS` (`-`), `VEZES` (`*`), `IGUAL A` (`==`), `DIFERENTE DE` (`!=`), `MAIOR QUE` (`>`), `MENOR QUE` (`<`), `MAIOR OU IGUAL A` (`>=`), `MENOR OU IGUAL A` (`<=`).

### 3.4. Saída de Dados
- **Impressão:** `GAITAR <argumentos>`

### 3.5. Controle de Fluxo
- **Enquanto:** `ARRUDIE ENQUANTO <condicao> :` ... `ACABOU O ARRODEIO`
- **Condicional:** `SE <condicao> :` ... `AÍ DENTO :` ... `VÔTE`

---

## 4. Dicionário de Termos Usados

- **Fuxico:** Fofoca, conversa fiada (comentários).
- **Quengo:** Cabeça (memória das variáveis).
- **Arrudiar:** Dar a volta (laço while).
- **Aí dento!:** Desaforo/negação (ramo else).
- **Vôte:** Espanto (fim de if).
- **Gaitar:** Falar alto (print).
- **Triscar:** Tocar de leve, tirar (subtração).
- **Dar o grau:** Ajustar, somar (adição).
- **Botar pra moer:** Acelerar (multiplicação).
- **Só o miolo da pipoca:** A melhor coisa do mundo (fim de execução).

---

## 5. Como Executar os Programas do Projeto 1

```bash
# 1. Hello World
python tradutor.py programas/ola_mundo.ce --run

# 2. 99 Garrafas de Cerveja
python tradutor.py programas/99_garrafas.ce --run

# 3. Tabuada do 7
python tradutor.py programas/tabuada.ce --run
```

