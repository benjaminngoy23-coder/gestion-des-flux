# Point d'entrée reconnu automatiquement par Nixpacks et Railpack.
from app import run_server

if __name__ == "__main__":
    run_server(open_browser=False)
