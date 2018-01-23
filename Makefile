all: jobs views build

jobs views build delete:
	python ./${@}.py

clean: delete
