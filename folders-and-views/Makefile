PORT = 8080
NAME = jenkins-folders-and-views

down stop:
	docker-compose $(@)

up detach:
	docker-compose up -d
	../scripts/jenkins_on_docker.sh $(NAME)

open:
	open http://localhost:$(PORT)

password:
	docker exec $(NAME) cat /var/jenkins_home/secrets/initialAdminPassword

health:
	docker inspect --format='{{json .State.Health}}' $(NAME)

exec:
	docker exec -it $(NAME) bash

nuke:
	docker-compose down --volumes --rmi local

