SHELL = /bin/bash
APP_NAME = miniconf
VERSION = 1.0
COMMIT_SHA1 = $(shell git rev-parse HEAD)
DOCKER_REPO = acl2020
# relative path to the root directories
ROOT_DIR = $(shell cd .. && pwd -P)
# relevant files for tracking the docker image version
DEPENDENT_FILES = $(ROOT_DIR)/.dockerignore
DEPENDENT_FILES += $(ROOT_DIR)/docker
DEPENDENT_FILES += $(ROOT_DIR)/requirements-dev.txt
DEPENDENT_FILES += $(ROOT_DIR)/requirements.txt
DEPENDENT_FILES += $(ROOT_DIR)/scripts/requirements.txt
DEPENDENT_FILES += $(ROOT_DIR)/Makefile

.PHONY: git-status git-archive build tag publish

# check if relevant changes are committed
git-status: $(DEPENDENT_FILES)
	@ [[ -z $$(git status $(DEPENDENT_FILES) --porcelain -uno) ]] || (echo "please commit your changes in $(DEPENDENT_FILES)"; exit 1)

# build the docker image
build: git-status
	cd ..; docker build \
		-t $(APP_NAME):$(COMMIT_SHA1) \
		-t $(APP_NAME):$(BRANCH_NAME) \
		-t $(DOCKER_REPO)/$(APP_NAME):$(COMMIT_SHA1) \
		-t $(DOCKER_REPO)/$(APP_NAME):$(BRANCH_NAME) \
		--label branch=$(BRANCH_NAME) \
		--label commit=$(COMMIT_SHA1) \
		-f docker/Dockerfile \
		--ssh default \
		-m 4g \
		-c 2 \
		.

# publish the docker image
publish: build
	@echo 'publish $(BRANCH_NAME) $(COMMIT_SHA1) to $(DOCKER_REPO)'
	docker push $(DOCKER_REPO)/$(APP_NAME):$(COMMIT_SHA1)
	docker push $(DOCKER_REPO)/$(APP_NAME):$(BRANCH_NAME)
