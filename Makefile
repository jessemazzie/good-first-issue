build:
	docker build -t gfi .
clean:
	docker rmi gfi
	rm gfi.log
run-dev:
	flask --app good-first-issue/app run --debug
run-container:
	docker run -d -p 8000:8000 gfi
compose-up:
	docker compose up -d