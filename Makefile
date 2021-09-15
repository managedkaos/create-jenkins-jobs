PORT       = 49000
BUILD_NAME = jenkins

all: jobs views folders build

jobs views folders build delete_jobs delete_folders delete_views delete_all apache_ivy_base_job move_jobs:
	honcho run python ./scripts/${@}.py

move_jobs : folders

clean: delete_jobs

clean-folders: delete_folders

clean-views: delete_views

clean-all: delete_all

pylint:
	pylint ./scripts/*.py

yamllint:
	yamllint ./ansible/*.yml

lint: pylint yamllint

down stop:
	docker-compose $(@)

up detach:
	docker-compose up -d
	./scripts/jenkins_on_docker.sh

open:
	open http://localhost:$(PORT)

password:
	docker exec jenkins-compose cat /var/jenkins_home/secrets/initialAdminPassword

health:
	docker inspect --format='{{json .State.Health}}' $(BUILD_NAME)

exec:
	docker exec -it $(BUILD_NAME) bash

