from pathlib import Path
import py_compile
import sys

root = Path(__file__).resolve().parent
required = [
    "app.py", "main.py", "start.sh", "Dockerfile", "requirements.txt",
    "Procfile", "nixpacks.toml", "railpack.json"
]
missing = [name for name in required if not (root / name).is_file()]
if missing:
    print("ERREUR - fichiers manquants:", ", ".join(missing))
    sys.exit(1)
py_compile.compile(str(root / "app.py"), doraise=True)
py_compile.compile(str(root / "main.py"), doraise=True)
print("OK - structure correcte et code Python compilable.")
