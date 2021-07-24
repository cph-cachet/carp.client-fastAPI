#!/usr/bin/env bash

USAGE="Usage: bash deployment.sh [production] [up|down|build|logs|rm]"

environment=$1
cmd=$2

if [[ ${cmd} == "up" ]]; then
	cmd="up -d"
fi
if [[ ${cmd} == "rm" ]]; then
	cmd="rm -f"
fi
if [[ ${cmd} == "logs" ]]; then
	cmd="logs -f"
fi
if [[ ${cmd} == "build" ]]; then
	cmd="up -d --build"
fi

## Production
if [[ "$environment" == "production" ]] && [[ "$2" == "down" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "up" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "build" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "logs" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "rm" ]]; then
  docker ps -q --filter "name=carp_client-fastapi" | grep -q . && docker stop carp_client-fastapi || "CARP Client API Fastapi could not be stopped." && docker rm -f carp_client-fastapi > /dev/null 2>&1 && echo 'removed container' || echo 'nothing to remove' && docker rmi -f carp_client-fastapi || echo "There is no carp_client-fastapi container to purge." && docker volume rm -f carp_client-fastapi || echo "The carp_client-fastapi does not exist in volume."

## Local
elif [[ "$environment" == "local" ]] && [[ "$2" == "down" ]]; then
	docker-compose -f docker-compose.local.yml ${cmd}
elif [[ "$environment" == "local" ]] && [[ "$2" == "up" ]]; then
	docker-compose -f docker-compose.local.yml ${cmd}
elif [[ "$environment" == "local" ]] && [[ "$2" == "build" ]]; then
	docker-compose -f docker-compose.local.yml ${cmd}
elif [[ "$environment" == "local" ]] && [[ "$2" == "logs" ]]; then
	docker-compose -f docker-compose.local.yml ${cmd}
elif [[ "$environment" == "local" ]] && [[ "$2" == "rm" ]]; then
  docker ps -q --filter "name=carp_client-fastapi" | grep -q . && docker stop carp_client-fastapi || "CARP Client API Fastapi could not be stopped." && docker rm -f carp_client-fastapi > /dev/null 2>&1 && echo 'removed container' || echo 'nothing to remove' && docker rmi -f carp_client-fastapi || echo "There is no carp_client-fastapi container to purge." && docker volume rm -f carp_client-fastapi || echo "The carp_client-fastapi does not exist in volume."

## Echo USAGE
else
	echo "${USAGE}"

fi