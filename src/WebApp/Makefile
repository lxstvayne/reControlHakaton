include .dev_env
export

run-dev:
	poetry run python ./manage.py runserver 0.0.0.0:8888

shell:
	poetry run python ./manage.py shell

migrate:
	poetry run python ./manage.py migrate $(ARGS)

makemigrations:
	poetry run python ./manage.py makemigrations

flush:
	poetry run python ./manage.py flush

startapp:
	poetry run python ./manage.py startapp $(ARGS)

collectstatic:
	poetry run python ./manage.py collectstatic
