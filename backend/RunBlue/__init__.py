"""runblue package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (runblue/config.py)
app.config.from_object('runblue.config')

# Tell the app about api and model
import runblue.restapi
import runblue.model

# Serve image files to the frontend
@app.route('/media/<path:filename>', methods=["GET"])
def get_image(filename):
    """Return image requested."""
    return flask.send_from_directory(str(app.config['MEDIA_FOLDER']), 
                                     filename, as_attachment=True)
