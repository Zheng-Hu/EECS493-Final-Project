
# To start DB, PhpMyAdmin, and the RunBlue API locally:
# `make local-start`
# note: after you make any changes to the flask app, run this command again
# to redeploy
#
# To stop all running resources:
# `make local-clean`

docker-build:
	docker build -t RunBlue:latest .

local-clean:
	docker-compose \
		down \
		-v

local-start: docker-build
	docker-compose \
		-f ./docker-compose.yml \
		up \
		--detach
