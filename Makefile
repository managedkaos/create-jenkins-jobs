all: jobs views folders build

jobs views folders build delete_jobs delete_folders delete_views delete_all apache-ivy-base-job:
	honcho run python ./scripts/${@}.py

clean: delete_jobs

clean-folders: delete_folders

clean-views: delete_views

clean-all: delete_all

pylint:
	pylint ./scripts/*.py

yamllint:
	yamllint ./ansible/*.yml

lint: pylint yamllint

jenkins: 
	./scripts/jenkins_on_docker.sh
