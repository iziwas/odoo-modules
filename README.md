# Modules Odoo

Modules pour **Odoo 17**, publiés sous licence libre.

| Module | Rôle | Licence |
| --- | --- | --- |
| [`preferred_companies`](preferred_companies) | Réactive automatiquement les sociétés préférées de l'utilisateur à la connexion | LGPL-3 |
| [`save_discard_buttons_form`](save_discard_buttons_form) | Rend les boutons Enregistrer et Annuler des formulaires bien visibles | AGPL-3 |

## preferred_companies

Dans une base multi-sociétés, chaque utilisateur choisit les sociétés à activer à sa connexion, sans avoir à les resélectionner à chaque session.

- La société par défaut de l'utilisateur est placée en premier, si elle fait partie de ses sociétés préférées.
- Seules les sociétés autorisées pour l'utilisateur peuvent être choisies, ce qui est aussi contrôlé côté serveur.
- Si un administrateur retire l'accès à une société, celle-ci disparaît des sociétés préférées.
- Une sélection déjà présente dans la session (URL ou cookie) reste prioritaire.

**Configuration :** cliquer sur son avatar en haut à droite, ouvrir **Préférences**, puis renseigner le champ **Sociétés préférentielles**. Le choix s'applique à la connexion suivante.

## save_discard_buttons_form

Par défaut, les commandes d'enregistrement et d'annulation des formulaires Odoo 17 sont de petites icônes peu contrastées. Ce module les rend immédiatement repérables :

- **Enregistrer** apparaît en vert et **Annuler** avec un contour rouge, avec des libellés à côté des icônes.
- Les états de survol et de focus sont bien marqués.
- Le bouton du menu Actions (roue dentée) reprend un style de bouton cohérent.

Le module est purement visuel : il ne change pas le comportement des boutons et n'ajoute ni champ ni réglage. Aucune configuration n'est nécessaire.

## Installation

```bash
git clone --branch 17.0 https://github.com/iziwas/odoo-modules.git
```

1. Ajouter le dossier cloné au paramètre `addons_path` d'Odoo, puis redémarrer le serveur.
2. Mettre à jour la liste des applications.
3. Installer le module souhaité.

## Développement

La qualité du code est contrôlée par des hooks [pre-commit](https://pre-commit.com/) (black, isort, flake8, pylint) :

```bash
pre-commit install
pre-commit run --all-files
```
