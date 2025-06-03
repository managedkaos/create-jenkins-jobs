#!/bin/bash

while read line;
do
	echo "working with ${line}"
	mkdir -p ${line}
	#docker cp CONTAINER:/var/logs/app.log - | tar x -O | grep "ERROR"
	docker cp jenkins:/var/jenkins_home/jobs/${line}/config.xml ./${line}/config.xml
done < ./jobs.txt
