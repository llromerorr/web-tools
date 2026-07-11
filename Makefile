.PHONY: install dev start build clean

install:
	npm install

dev:
	npm run dev

start: dev

build:
	npm run build

clean:
	npx rimraf dist node_modules
