# Déploiement sur Cloudflare Pages

Ce dépôt est un site de documentation **Sphinx** (thème Wagtail + MyST).
Le HTML compilé est généré dans `build/html` — c'est le dossier servi en production.

## Option A — Git + reconstruction (recommandé)

Cloudflare reconstruit le site à chaque `git push`.

1. Pousser ce dépôt sur GitHub/GitLab.
2. Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** →
   **Connect to Git**, sélectionner le dépôt.
3. Régler la configuration de build :
   - **Framework preset** : `None`
   - **Build command** : `pip install -r requirements.txt && sphinx-build -b html source build/html`
   - **Build output directory** : `build/html`
   - Variable d'environnement `PYTHON_VERSION` = `3.12` (ou laisser `.python-version`).
4. **Save and Deploy**.

Les versions des dépendances sont figées dans `requirements.txt` et la version
de Python dans `.python-version`.

## Option B — Déploiement direct du HTML déjà compilé (le plus rapide)

Le dossier `build/html` est déjà versionné, donc aucune recompilation n'est
nécessaire :

```bash
npx wrangler pages deploy build/html --project-name software-defined-radio
```

`wrangler.toml` indique déjà `pages_build_output_dir = "build/html"`, donc on
peut aussi simplement faire :

```bash
npx wrangler pages deploy
```

(Première fois : `npx wrangler login` pour s'authentifier.)

## Reconstruire localement

```bash
pip install -r requirements.txt
make html        # ou : sphinx-build -b html source build/html
```
