init:
	python3 -m venv env
	bash -c "source env/bin/activate && pip install -r requirements.txt"
	cp .start.env .env
	npm install
	git init
	bash -c "source env/bin/activate && python manage.py migrate && python manage.py makesuperuser && python manage.py generate_tailwind_directories"
	npm run tailwind:build
	git add .
	git commit -m "Initial commit"
	@echo "Run 'make run' to start the server"
	@echo "Run 'make tw' to start tailwind watch"
	@echo "Run 'make mm' to make migrations"
	@echo "Run 'make m' to migrate"

init-docker:
	git init
	git add .
	git commit -m "Initial commit"
	cp .docker.env .env
	docker compose build
	docker compose up -d db
	docker compose up -d redis
	sleep 2
	docker compose run --rm web python manage.py migrate
	docker compose run --rm web python manage.py makesuperuser
	docker compose run --rm web python manage.py generate_tailwind_directories
	docker compose run --rm tailwind
	docker compose up

manage:
	bash -c "source env/bin/activate && python manage.py $(command)"

run: command=runserver
run: manage


mm: command=makemigrations
mm: manage

m: command=migrate
m: manage

tw-directories: command=generate_tailwind_directories
tw-directories: manage
tw: tw-directories
	npm run tailwind:watch


tw-build: tw-directories
	npm run tailwind:build