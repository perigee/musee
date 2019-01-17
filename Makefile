.PHONY: all


ENV := dev


export


build:
	docker-compose -f docker-compose.$(ENV).yml build musee

dev: build
	docker-compose -f docker-compose.$(ENV).yml up musee

clean:
	docker-compose -f docker-compose.$(ENV).yml down --remove-orphans
