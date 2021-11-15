"""
Posts header.

URLS include:

/api/v1/posts/                  [GET, POST]
/api/v1/posts/<postid>/         [GET]
/api/v1/posts/?user=            [GET]
"""

from flask import jsonify,request
import runblue


@runblue.app.route('/api/v1/posts/', methods =["GET"])
def posts():
    # Get the username, if provided
    username = request.args.get("user")
        
    # Setup context for response
    context = {
        "url": "/api/v1/posts/"
    }

    # Get db connection
    cur = runblue.model.get_db()

    # Retrieve posts from database
    if (username):
        # Check if user exists
        if runblue.check_no_user(username):
            return runblue.error_code("User could not be found.", 404)

        cur.execute(
            "SELECT caption, created, filename AS imageurl, owner, postid FROM posts WHERE owner = %s",
            (username,)
        )
        context["data"] = list(cur.fetchall())
    else:
        cur.execute(
            "SELECT caption, created, filename AS imageurl, owner, postid FROM posts"
        )
        context["data"] = list(cur.fetchall())

    # Get workout for each post
    for post in context["data"]:
        # Get the workout data from db
        cur.execute(
            "SELECT distance, time FROM workouts where postid = %s",
            (post["postid"],)
        )
        workout = cur.fetchone()

        # Add workout data to this post
        post["distance"] = workout["distance"]
        post["time"] = workout["time"]

    return jsonify(**context)

@runblue.app.route('/api/v1/posts/<int:postid>/', methods=["GET"])
def get_post(postid):
    # Setup context for response
    context = {
        "url": "/api/v1/posts/" + str(postid) + "/"
    }

    # Get db connection, execute query to get post
    cur = runblue.model.get_db()
    cur.execute(
        "SELECT caption, created, filename AS imageurl, owner, postid FROM posts WHERE postid = %s",
        (postid,)
    )
    context["data"] = cur.fetchone()

    # Check this post exists
    if context["data"] == None:
        return runblue.error_code("Post could not be found.", 404)

    # Get the workout data from db
    cur.execute(
        "SELECT distance, time FROM workouts where postid = %s",
        (postid,)
    )
    workout = cur.fetchone()

    # Add workout data to response
    context["data"]["distance"] = workout["distance"]
    context["data"]["time"] = workout["time"]

    return jsonify(**context)
