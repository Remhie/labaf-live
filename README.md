# LABAF Live

Suivi en direct des joueurs LABAF Paris dans les tournois de baby-foot enregistrés sur Coral.

- **Accueil** : tous les tournois français de la saison, classés par niveau (national, régional, loisir, championnats), avec le nombre de licenciés LABAF inscrits. Les tournois en cours ressortent en rouge.
- **Fiche tournoi** : matchs en cours, prochains matchs, puis résultats par catégorie pour chaque joueur du club.

Seuls les joueurs avec une **licence LABAF active** sur Coral sont suivis. Les anciens membres sont exclus automatiquement.

## Comment ça marche

Un petit programme tourne gratuitement sur GitHub :

- toutes les 5 minutes, il regarde s'il y a un tournoi en cours et, si oui, relit sa page publique sur Coral ;
- toutes les 3 heures, il relit aussi les inscriptions et les modalités de tous les tournois de la saison.

Il enregistre les données dans `docs/data/`, et GitHub Pages publie le site à partir du dossier `docs/`.

Les horaires GitHub ne sont pas garantis à la minute : compte en pratique 5 à 15 minutes de décalage sur un score.

## Mise en ligne (une seule fois)

1. Sur github.com, crée un nouveau dépôt **public** nommé `labaf-live` (public = le programme tourne sans limite gratuite).
2. Dans le dépôt, clique **Add file → Upload files** et glisse le contenu du dossier (les dossiers `docs` et `scripts`, et le fichier `package.json`). Valide avec **Commit changes**.
3. Le dossier `.github` est souvent caché par l'ordinateur. Crée-le à la main : **Add file → Create new file**, tape comme nom `.github/workflows/update.yml`, colle le contenu du fichier `update.yml` fourni, puis **Commit changes**.
4. **Settings → Actions → General** : tout en bas, dans *Workflow permissions*, choisis **Read and write permissions** puis **Save**.
5. **Settings → Pages** : dans *Build and deployment*, choisis **Deploy from a branch**, branche **main**, dossier **/docs**, puis **Save**.
6. Onglet **Actions** : ouvre *Mise à jour des tournois*, clique **Run workflow** (mode `full`). Au bout de 2 à 3 minutes, les données sont à jour.

Le site est alors en ligne à l'adresse `https://TON-NOM-GITHUB.github.io/labaf-live/`.

## Bon à savoir

- GitHub met en pause les programmes automatiques d'un dépôt resté 60 jours sans activité. Ici, chaque mise à jour des données compte comme une activité, donc ça ne devrait pas arriver pendant la saison. Si c'est le cas, un bouton *Enable* apparaît dans l'onglet Actions.
- Changer de saison : rien à faire, la liste suit le calendrier FFBF publié sur Coral.
- Si Coral modifie son site, la lecture peut s'arrêter. Il suffit alors de revenir me voir avec le message d'erreur visible dans l'onglet Actions.
