"""runblue development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies (change for deployment)
SECRET_KEY = b'zRWU\xab\x1b`\x16d`\xea$b\xfb\xbf~\x009\xfc\xde\x84rK\xc7'

# File Upload to var/uploads/
runblue_ROOT = pathlib.Path(__file__).resolve().parent.parent
MEDIA_FOLDER = runblue_ROOT/'uploads'

# Postgres database info
POSTGRESQL_DATABASE_PORT = 5432
POSTGRESQL_DATABASE_USER = "runblue_user"
POSTGRESQL_DATABASE_PASSWORD = "password"
POSTGRESQL_DATABASE_DB = "runblue"
