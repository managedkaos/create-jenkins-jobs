all: jobs views folders build

jobs views folders build delete:
	honcho run python ./${@}.py

apache-ivy-base-job:
	honcho run python apache-ivy-base-job.py

clean: delete
