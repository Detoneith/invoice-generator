# Générateur de facture

## Prérequis

- Python 3.12+
- pip
- Git

## Installation

```bash
# Cloner le dépôt
git clone git@github.com:Detoneith/invoice-generator.git
cd invoice-generator

# Créer et activer l'environnement virtuel
python -m venv venv
# Windows :
venv\Scripts\activate
# macOS/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

```bash
# Appliquer les migrations
python manage.py migrate

# Lancer le serveur de développement
python manage.py runserver
```

- Interface publique : http://127.0.0.1:8000/
- Admin Django : http://127.0.0.1:8000/admin/

## Structure du projet

- products/ : CRUD produits (nom, prix, date de péremption)
- invoices/ : gestion des factures (sélection de produits, total, date)
- templates/ : gabarits HTML avec Bootstrap 5
- invoice_generator/ : configuration Django (settings, URLs)