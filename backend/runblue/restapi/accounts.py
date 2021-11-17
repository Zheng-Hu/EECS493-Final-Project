"""
Accounts header.

Note: this is not how an actual user account system would
work, please do not take this as an actual representation
of user authentication. This is simply for prototyping.

URLS include:

/api/v1/accounts/               [POST]
/api/v1/accounts/login/         [POST]
/api/v1/accounts/logout/        [POST]
"""

from flask import jsonify, request
import runblue


@runblue.app.route('/api/v1/accounts/', methods=["POST"])
def create_account():
    """Endpoint for creating an account."""
    # Get username & password from request body
    username = request.json["username"]
    password = request.json["password"]

    # Ensure that username and password aren't null
    if username == "" or username == None or password == "" or password == None:
        return runblue.error_code("Malformed username or password.", 404)

    # Check to see if username has already been used
    cur = runblue.model.get_db()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )
    user = cur.fetchone()

    if user != None:
        return runblue.error_code("User already exists.", 401)

    # Insert into the database
    cur = runblue.model.get_db()
    cur.execute(
        "INSERT INTO users (username, password, created) VALUES (%s, %s, DEFAULT)",
        (username, password)
    )

    # Return success code
    return runblue.error_code("User account created.", 201)

@runblue.app.route('/api/v1/accounts/login/', methods=["POST"])
def user_login():
    """Endpoint for logging in a user."""
    # Get username, password from URL
    username = request.json["username"]
    password = request.json["password"]

    # Get the user from database
    cur = runblue.model.get_db()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )
    user = cur.fetchone()

    # Check if user even exists or wrong password
    if user is None:
        return runblue.error_code("User does not exist.", 404)
    elif password != user["password"]:
        return runblue.error_code("Password is incorrect.", 401)

    # User logged in successfully
    return runblue.error_code("Logged in successfully.", 200)

@runblue.app.route('/api/v1/accounts/logout/', methods=["POST"])
def user_logout():
    """Endpoint for logging in a user."""
    return runblue.error_code("Logged out successfully.", 200)
