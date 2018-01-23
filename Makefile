all: jobs views build

jobs views build delete:
	honcho run python ./${@}.py

clean: delete
