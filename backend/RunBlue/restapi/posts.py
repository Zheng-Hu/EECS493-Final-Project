import flask
import RunBlue


@RunBlue.app.route('/')
def show_index():
    """Display / route."""

    # Connect to database
    connection = RunBlue.model.get_db()

    # Query database
    cur = connection.execute(
        "SELECT username "
        "FROM users"
    )
    users = cur.fetchall()

    # Add database info to context
    context = {"users": users}
    return flask.jsonify(**context)