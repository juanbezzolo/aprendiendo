# Sistema de Seguimiento de Cultivo de Micelio

Este proyecto es un prototipo realizado con **Django**, **HTML**, **CSS** y **JavaScript** para llevar el control de cultivos de hongos medicinales.

## Características
- Registro de usuarios, cepas, cultivos, monotubes, cosechas y seguimiento técnico.
- Base de datos basada en **SQLite** por defecto (puede usarse MySQL configurando `DATABASES`).

## Requisitos
- Python 3.10+
- (Opcional) MySQL o MariaDB para persistencia

Instala las dependencias con:
```bash
pip install -r requirements.txt
```

## Ejecución
Crea las migraciones y arranca el servidor de desarrollo:
```bash
python manage.py migrate
python manage.py runserver
```

El sitio quedará disponible en `http://localhost:8000`.

La aplicación crea automáticamente un usuario administrador con nombre de
usuario `admin` y contraseña `myco` la primera vez que se ejecuta, para que
puedas iniciar sesión en `http://localhost:8000/login/`.

## Estructura
- `manage.py`: utilidades de administración de Django.
- `cultivo_project/`: configuración del proyecto.
- `core/`: aplicación principal con modelos y vistas.
- `templates/`: plantillas HTML.
- `static/`: archivos estáticos (CSS y JS).

Personaliza las vistas y la lógica de negocio según tus necesidades.
