# ida_irma_dsm

Django prototype for managing metadata and user permissions.

![](static/ida_core/Bundesbank_Logo.png?raw=true)
![](static/ida_core/IDA_Logo.jpg?raw=true)
![](static/ida_core/FDSZ.jpg?raw=true)

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

Use the following command to fill the database with some limited test data.
```bash
python manage.py populate_db
```

Next, you can start the server.
```bash
python manage.py runserver
```

Use the following commands to visualize the data model:
```bash
# To group all the application and output into PNG file
python manage.py graph_models -a -g -o models.png
# Include only ida_core
python manage.py graph_models ida_core -o models_ida_core.png
```

## Structure
The project currently consists of three apps:
* ida_core (this is the main development focus for now)
* dsm_core
* irma_core
