all: jobs views folders build

jobs views folders build delete_jobs delete_folders delete_views delete_all apache_ivy_base_job move_jobs challenge_jobs challenge_folders challenge_views challenge_move_jobs:
	honcho run python ./scripts/${@}.py

move_jobs : folders

list_plugins:
	honcho run python ./scripts/list_plugins.py

clean: delete_jobs

clean_folders: delete_folders

clean_views: delete_views

clean_all: delete_all

pylint:
	pylint ./scripts/*.py

yamllint:
	yamllint ./ansible/*.yml

lint: pylint yamllint

jenkins:
	./scripts/jenkins_on_docker.sh
