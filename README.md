# Django Rest Framework Simple Project
___
Docs for setting up this project.
## 1. Instalar Python
### 1.1. Instalar PIP
> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
> python get-pip.py
___
## 2. Instalar virtualenv
> pip install virtualenv
___
## 3. Crear un ambiente virtual
> virtualenv venv --python=python3.10
### 3.1. Activar ambiente
> source venv/bin/activate
#### 3.1.1. En Windows
> venv/Scripts/activate.ps1
___
## 4. Instalar dependencias
> pip install -r requirements.txt
___
## 5. Realizar migraciones
### 5.1. Configurar settings para el uso de la base de datos, en settings.py modificar lo siguiente de acuerdo a lo necesario:
```json lines
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.YOUR_DB_ENGINE',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'DB_HOST',
        'PORT': 'DB_PORT'
    }
}
```
#### 5.1.1. Crear la base de datos
Crear la base de datos antes de poder realizar las migraciones.  
### 5.2. Revisar si no existen migraciones no registradas
> Python manage.py makemigrations
### 5.3. Migrar base de datos
> Python manage.py migrate
___
## 6. Empezar la aplicación
> Python manage.py runserver