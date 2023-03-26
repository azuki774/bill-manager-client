CONTAINER_NAME_REGISTER=bill-manager-register

.PHONY: build start
build:
	docker build -t $(CONTAINER_NAME_REGISTER) -f build/Dockerfile .

start:
	docker compose -f deployment/compose-local.yaml up
