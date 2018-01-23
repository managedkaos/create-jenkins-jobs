create delete build:
	python ./${@}_jobs.py

clean: delete

views:
	python ./create_views.py
