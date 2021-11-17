"""runblue package initializer."""
import flask
from flask_cors import CORS


# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (runblue/config.py)
app.config.from_object('runblue.config')

# Tell the app about api and model
import runblue.restapi
import runblue.model

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Check if a user exists in the database
def check_no_user(username: str) -> bool:
    """Check if username doesn't exist in users table."""
    cur = runblue.model.get_db()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )

    return cur.fetchone() == None

# Returning error codes
def error_code(message, status_code):
    """Return the error with JSON and error code."""
    error = {}
    error["message"] = message
    error["status_code"] = status_code
    return flask.jsonify(**error), status_code

# Serve image files to the frontend
@app.route('/media/<path:filename>', methods=["GET"])
def get_image(filename):
    """Return image requested."""
    return flask.send_from_directory(str(app.config['MEDIA_FOLDER']), 
                                     filename, as_attachment=True)
