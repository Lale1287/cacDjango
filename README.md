# cacDjango - Info Linux
En una carpeta X crear entorno virtual
python3 -m venv django

Clonar el repo de git
git clone git@github.com:Lale1287/cacDjango.git

Van a quedar dos carpetas: django y cacDjango. django es para el entorno virtual,
el repo de trabajo es cacDjango

Activar entorno
source django/bin/activate

Instalar Django 3.2
pip install django==3.2

Correr servidor //parada en cacDjango, que tiene el archivo manage.py
python manage.py runserver

Si pide hacer un migrate, se para el server y se ejecuta
python manage.py migrate

En localhost:8000 se pueden ver las páginas definidas en urls.py.
El proyecto es cacDjango, y tiene definida una app core, que contiene los templates.
