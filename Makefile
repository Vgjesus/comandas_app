install:
	pip install -r requirements.txt

start:
	python src/main.py

build_docker:
	docker build -t app .

start_docker:
	docker run -p 5000:5000 app