#!/usr/bin/env bash
if [ $(ps -elf | grep docker | wc -l) -gt 0 ];
then
    docker pull jenkins/jenkins:lts
    docker run --detach --publish 49000:8080 --name jenkins jenkins/jenkins:lts
    echo -n "Waiting for Jenkins process to start ."
    until [ $(curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://127.0.0.1:49000) -eq 403 ]; do echo -n '.'; sleep 1; done
    echo
    echo -n "Here's the admin password!   "
    docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
    echo "Browse to http://localhost:49000"
else
    echo "Can't find any docker processes.  Is Docker really running? :/"
fi
