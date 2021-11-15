"""
Leaderboard header.

URLS include:

/api/v1/leaderboard/            [GET]
/api/v1/leaderboard/?user=      [GET]
"""

from flask import jsonify, request
import runblue


@runblue.app.route('/api/v1/leaderboard/', methods=["GET"])
def get_leaderboard():
    # Get the username, if provided
    username = request.args.get("user")
    
    # Setup context for response
    context = {
        "url": "/api/v1/leaderboard/"
    }

    # Get db connection
    cur = runblue.model.get_db()

    # Retrieve leaderboard from database
    if (username):
        if runblue.check_no_user(username):
            return runblue.error_code("User could not be found.", 404)

        # Get the user's leaderboard
        cur.execute(
            "SELECT distance, owner, time, workoutid FROM workouts WHERE owner = %s LIMIT 10",
            (username,)
        )
        context['data'] = list(cur.fetchall())
    else:
        cur.execute(
            "SELECT distance, owner, time, workoutid FROM workouts LIMIT 10"
        )
        context["data"] = list(cur.fetchall())

    # Sort by per-mile time
    for workout in context["data"]:
        workout["permiletime"] = workout["time"] / workout["distance"]

    context["data"] = sorted(context["data"], key=lambda i: i["permiletime"])
    
    return jsonify(**context)
