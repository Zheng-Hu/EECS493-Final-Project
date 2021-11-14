import flask
from flask import jsonify,request
import RunBlue


@RunBlue.app.route('/api/v1/posts/', methods =["GET"])
def posts():
  db = RunBlue.model.get_db()
  size = flask.request.args.get("size",default=10,type=int)
  page = flask.request.args.get("page",default=0,type=int)
    
  url = "/api/v1/posts/"
  context = {
      "url": url
  }
  username = request.args.get("user")
  if (username):
    cur = db.execute(
                    "SELECT posts.postid AS created, posts.owner AS owner, posts.time AS time, posts.distance AS distance, "
                    "posts.caption AS caption, posts.created AS created " 
                    "FROM posts WHERE posts.owner = ? ORDER BY created DESC",\
                    (username,)
                    )
    context['data'] = list(cur.fetchall())
    return flask.jsonify(**context);
  else:
    cur = db.execute(
                      "SELECT posts.postid AS created, posts.owner AS owner, posts.time AS time, posts.distance AS distance, "
                      "posts.caption AS caption, posts.created AS created " 
                      "FROM posts ORDER BY created DESC")
                    #  "ORDER BY created DESC, postid DESC LIMIT ? OFFSET ? * ?",\
                    #  (size,size,page,))
    context['data'] = list(cur.fetchall())
    # if size*(page+1) >= cur.fetchall()[0]["num"]:
    #   context['next'] = ''
    # else:
    #   context['next'] = f"/api/v1/p/?size={size}&page={page+1}"
    return flask.jsonify(**context);

@RunBlue.app.route('/api/v1/posts/<int:postid>/', methods=["GET"])
def get_post(postid):
  url = "/api/v1/posts/" + str(postid) + "/"
  context = {
      "url": url
  }
  db = RunBlue.model.get_db()
  cur = db.execute("SELECT posts.postid AS created, posts.owner AS owner, posts.time AS time, posts.distance AS distance, "
                   "posts.caption AS caption, posts.created AS created " 
                   "FROM posts WHERE posts.postid=?",(postid,))
  context['data'] = list(cur.fetchall())
  return flask.jsonify(**context);


@RunBlue.app.route('/api/v1/leaderboard/', methods=["GET"])
def leaderboard():
  username = request.args.get("user")
  db = RunBlue.model.get_db()
  if (username):
    url = "/api/v1/leaderboard/"
    context = {"url": url}
    cur = db.execute("SELECT workout.workoutid AS workoutid, workout.time AS time, workout.distance AS distance, workout.owner AS owner "
                  "FROM workout WHERE workout.owner = ? ORDER BY created DESC",\
                    (username,)
                  )
    context['data'] = list(cur.fetchall())
    return flask.jsonify(**context); 
  else:
    url = "/api/v1/leaderboard/"
    context = {"url": url}
    cur = db.execute("SELECT workout.workoutid AS workoutid, workout.time AS time, workout.distance AS distance, workout.owner AS owner "
                  "FROM workout ORDER BY created DESC")
    context['data'] = list(cur.fetchall())
    return flask.jsonify(**context); 
  
