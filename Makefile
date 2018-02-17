all: jobs views folders build

jobs views folders build delete apache-ivy-base-job:
	honcho run python ./scripts/${@}.py

clean: delete
