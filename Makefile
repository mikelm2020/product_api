# ==============================================================================
# Makefile para la gestión del proyecto Django con Docker Compose
# ==============================================================================

# Variables
PROJECT_NAME = api_producto
DJANGO_APP_NAME = api
DOCKER_COMPOSE_COMMAND = docker compose
PYTHON_COMMAND = python manage.py

# ==============================================================================
# Comandos principales (Comandos Docker Compose)
# ==============================================================================

# Iniciar todos los servicios en segundo plano
up: ## Inicia los contenedores (web) en segundo plano
	$(DOCKER_COMPOSE_COMMAND) up -d

# Iniciar todos los servicios en segundo plano y eliminar contenedores huérfanos
up-clean: ## Inicia los contenedores y elimina los huérfanos
	$(DOCKER_COMPOSE_COMMAND) up -d --remove-orphans

# Detener todos los servicios
down: ## Detiene los contenedores
	$(DOCKER_COMPOSE_COMMAND) down

# Detener y eliminar todos los servicios y sus volúmenes (¡Precaución: borra datos de DB!)
down-clean: ## Detiene y elimina contenedores y volúmenes (¡CUIDADO con los datos!)
	$(DOCKER_COMPOSE_COMMAND) down -v

# Construir/reconstruir las imágenes de los servicios
build: ## Construye/reconstruye las imágenes de los servicios
	$(DOCKER_COMPOSE_COMMAND) build

# Reconstruir imágenes y levantar servicios
rebuild: ## Reconstruye las imágenes y levanta los servicios
	$(DOCKER_COMPOSE_COMMAND) down --rmi all
	$(DOCKER_COMPOSE_COMMAND) up -d --build

# Ver el estado de los servicios
ps: ## Muestra el estado de los servicios Docker
	$(DOCKER_COMPOSE_COMMAND) ps

# Ver logs de todos los servicios o de un servicio específico (e.g., make logs service=web)
logs: ## Muestra los logs en tiempo real (todos o de un 'service=<nombre>')
ifeq ($(service),)
	$(DOCKER_COMPOSE_COMMAND) logs -f
else
	$(DOCKER_COMPOSE_COMMAND) logs -f $(service)
endif

# ==============================================================================
# Comandos de Django (ejecutadas dentro del contenedor 'web')
# ==============================================================================

# Crear una nueva aplicación de Django. Uso: make startapp name=mi_nueva_app
startapp: ## Crea una nueva aplicación Django (uso: make startapp name=mi_app)
ifndef name
	$(error ERROR: Debes proporcionar el nombre de la app. Uso: make startapp name=mi_nueva_app)
endif
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) startapp $(name)

# Crear migraciones para una app específica o para todas. Uso: make makemigrations app=my_app (opcional)
makemigrations: ## Crea migraciones (uso: make makemigrations app=<nombre_app> o sin 'app')
ifeq ($(app),)
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) makemigrations
else
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) makemigrations $(app)
endif

# Aplicar migraciones a la base de datos
migrate: ## Aplica las migraciones a la base de datos
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) migrate

# Crear superusuario de Django
createsuperuser: ## Crea un superusuario para Django
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) createsuperuser

# Ejecutar el servidor de desarrollo de Django (en primer plano)
runserver: ## Inicia el servidor de desarrollo de Django
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) runserver 0.0.0.0:8000

# Acceder al shell de Django
shell: ## Accede al shell interactivo de Django
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) shell

# Generar la Django Secret Key
secretkey: ## Genera una nueva Django SECRET_KEY
	$(DOCKER_COMPOSE_COMMAND) exec web $(PYTHON_COMMAND) -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Ejecutar un script Python arbitrario dentro del contenedor 'web'.
# Uso: make run-script file=licensing_management/firebird_connector.py
run-script: ## Ejecuta un script Python dentro del contenedor web (uso: make run-script file=<ruta_script>)
ifndef file
	$(error ERROR: Debes proporcionar la ruta del script. Uso: make run-script file=my_script.py)
endif
	$(DOCKER_COMPOSE_COMMAND) exec web python $(file)

# ==============================================================================
# Limpieza
# ==============================================================================

# Eliminar archivos .pyc y __pycache__
clean-pyc: ## Elimina archivos .pyc y directorios __pycache__
	find . -name "*.pyc" -exec rm {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Eliminar todas las imágenes de Docker no usadas (dangling)
clean-docker-images: ## Elimina imágenes de Docker no usadas
	docker image prune -f

# Ayuda (muestra esta lista de comandos)
help: ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: up up-clean down down-clean build rebuild ps logs startapp makemigrations migrate createsuperuser runserver shell secretkey clean-pyc clean-docker-images help
