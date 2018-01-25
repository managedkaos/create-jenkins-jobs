all: jobs views build

jobs views folders build delete:
	honcho run python ./${@}.py

clean: delete
