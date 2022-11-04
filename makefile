##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/app/main.py

##############################################################################################
# Automated actions
##############################################################################################

.PHONY: docker-init
docker-init: ## Docker automation
	@echo Automated push to dev branch to origin
	@docker image build -t python:0.0.1 /app/

.PHONY: verify-built
verify-built: ## Verify Docker built
	@echo Checking docker images
	@docker images

##############################################################################################
# Complex commands
########################################################

docker-build: docker-init verify-built