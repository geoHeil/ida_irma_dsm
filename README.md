# ida_irma_dsm

Django prototype for managing metadata and user permissions.

## Getting Started

Use conda to manage your environment.

```bash
# Create the environment from the YAML file
conda env create -f environment.yml

# Activate the environment
conda activate djangoenv
```

After checking out the code from git, there won't be a database. In order for the web app to function, you will have to apply migrations first.
```bash
# optional; if models changed: python manage.py makemigrations ida_core
python manage.py migrate
python manage.py createsuperuser # Admin user
```

Next, you can start the server.
```bash
python manage.py runserver
```

## Structure
The project currently consists of three apps:
* ida_core (this is the main development focus for now)
* dsm_core
* irma_core
