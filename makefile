##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/app/main.py

##############################################################################################
# Automated actions
##############################################################################################
#Run docker application
.PHONY: docker-init
docker-init: ## Docker automation
	@echo Automated push to dev branch to origin
	@docker image build -t python:0.0.1 /app/
#Check docker images in env
.PHONY: verify-built
verify-built: ## Verify Docker built
	@echo Checking docker images
	@docker images

##############################################################################################
# Complex commands
########################################################

docker-build: docker-init verify-built