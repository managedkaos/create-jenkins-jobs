all: jobs views folders build

jobs views folders build delete delete_all_jobs apache-ivy-base-job:
	honcho run python ./scripts/${@}.py

clean: delete

clean-all: delete_all_jobs
