"""RunBlue development configuration."""

import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
SECRET_KEY = b'FIXME SET THIS WITH: $ python3 -c '
'"import os; print(os.urandom(24))" '
SESSION_COOKIE_NAME = 'login'
# File Upload to var/uploads/
RunBlue_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = RunBlue_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
# Database file is var/RunBlue.sqlite3
DATABASE_FILENAME = RunBlue_ROOT/'var'/'RunBlue.sqlite3'
