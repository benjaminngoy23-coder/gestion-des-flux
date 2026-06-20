# FundFlow — Dokploy universel

Cette version est volontairement compatible avec **Dockerfile**, **Nixpacks**, **Railpack** et **Docker Compose**.

## Méthode recommandée

Dans Dokploy, créer une **Application** et choisir :

- Build Type : `Dockerfile`
- Dockerfile Path : `Dockerfile`
- Docker Context Path : `.`
- Port du domaine : `8000`

Ne pas définir de commande personnalisée dans l'onglet Advanced.

## Point d'entrée

Toutes les méthodes lancent :

```sh
sh start.sh
```

Le serveur écoute sur `0.0.0.0:8000`.

## Données

Monter un volume persistant sur `/app/data`.

## Contrôle

```text
/health
```

doit répondre en HTTP 200 avec `{"ok": true, ...}`.
