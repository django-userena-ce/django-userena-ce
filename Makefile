build:
	poetry build

publish: build
	poetry publish -r ubidots
