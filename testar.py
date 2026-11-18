import subprocess
import sys
import os

pasta_projeto = os.path.dirname(os.path.abspath(__file__))
env_utf8 = {**os.environ, "PYTHONIOENCODING": "utf-8"}

testes = [
    ("programas/ola_mundo.ce", None, "Hello World!"),
    ("programas/99_garrafas.ce", None, "garrafa de cerveja"),
    ("programas/tabuada.ce", None, "7  x  10  =  70"),
]

print("=== TESTANDO PROGRAMAS DO PROJETO 1 ===")
todos_ok = True
for prog, entrada, esperado in testes:
    res = subprocess.run(
        [sys.executable, "tradutor.py", prog, "--run"],
        input=entrada,
        text=True,
        encoding="utf-8",
        capture_output=True,
        cwd=pasta_projeto,
        env=env_utf8,
    )
    if res.returncode == 0 and esperado in res.stdout:
        print(f"  [OK] {prog}")
    else:
        print(f"  [ERRO] {prog}: {res.stderr or res.stdout}")
        todos_ok = False

if todos_ok:
    print("\nTODOS OS PROGRAMAS DO PROJETO 1 PASSARAM COM SUCESSO!")
else:
    print("\nHouve falhas em alguns programas.")
    sys.exit(1)
