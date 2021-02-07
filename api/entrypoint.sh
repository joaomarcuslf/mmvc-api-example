#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
	echo "[entrypoint.sh] LOG: Waiting for PostgreSQL to start"

	while ! nc -z $SQL_HOST $SQL_PORT; do
		sleep 0.1
	done

	echo "[entrypoint.sh] LOG: PostgreSQL started successfully"
fi

echo "[entrypoint.sh] LOG: Running command create_db"

python run.py create_db

exec "$@"
