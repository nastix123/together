
mkm: ## make migrations
	docker exec -it together_auth python manage.py makemigrations

m: ## migrate
	docker exec -it together_auth python manage.py migrate

csu: ## create superuser
	docker exec -it together_auth python manage.py createsuperuser

pr: ## run pre-commit
	pre-commit run --all-files

mtr: ## create django.po
	python manage.py makemessages -l ru

ctr: ## create django.mo
	python manage.py compilemessages --use-fuzzy

dcr: ## docker compose -f docker-compose.local up
	docker compose -f docker-compose.local.yml up

dcrb: ## docker compose -f docker-compose.local up --build
	docker compose -f docker-compose.local.yml up --build

dcrd: ## docker compose -f docker-compose.local down
	docker compose -f docker-compose.local.yml down

dcrdv: ## docker compose -f docker-compose.local down -v
	docker compose -f docker-compose.local.yml down -v
