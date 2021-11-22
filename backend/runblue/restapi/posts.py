"""
Posts header.

URLS include:

/api/v1/posts/                  [GET, POST]
/api/v1/posts/<postid>/         [GET]
/api/v1/posts/?user=            [GET]
"""

from flask import jsonify,request
import runblue
import uuid
import pathlib
import json

@runblue.app.route('/api/v1/posts/', methods=["POST"])
def upload_post():
    """Endpoint to upload a post."""
    # Get the file and filename
    file = request.files['file']
    filename = file.filename

    # Compute base name
    uuid_basename = "{stem}{suffix}".format(
        stem=uuid.uuid4().hex,
        suffix=pathlib.Path(filename).suffix
    )

    # Save to disk
    path = runblue.app.config["MEDIA_FOLDER"]/uuid_basename
    file.save(path)

    # Get form data
    caption = request.form["caption"]
    distance = request.form["distance"]
    owner = request.form["owner"]
    time = request.form["time"]

    # Get db connection
    cur = runblue.model.get_db()

    # Insert into posts table
    cur.execute(
        "INSERT INTO posts (postid, filename, caption, created, owner) VALUES (DEFAULT, %s, %s, DEFAULT, %s) RETURNING postid",
        (uuid_basename, caption, owner)
    )

    # Retrieve the id of the post created
    created_postid = cur.fetchone()["postid"]

    # Insert into the workouts table
    cur.execute(
        "INSERT INTO workouts(workoutid, time, distance, created, owner, postid) VALUES (DEFAULT, %s, %s, DEFAULT, %s, %s)",
        (time, distance, owner, created_postid)
    )

    # Return created response
    return runblue.error_code("Post created", 201)

@runblue.app.route('/api/v1/posts/', methods=["GET"])
def get_posts():
    """Endpoint to get a collection of posts."""
    # Get db connection
    cur = runblue.model.get_db()

    # Get the username, if provided
    username = request.args.get("user")
        
    # Setup context for response
    context = {
        "url": "/api/v1/posts/"
    }

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
    """Endpoint to get a post by postid."""
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
