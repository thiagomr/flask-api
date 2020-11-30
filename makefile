dev:
	FLASK_APP=app.py FLASK_ENV=development FLASK_DEBUG=1 flask run

deps:
	pip install -r requirements.txt
