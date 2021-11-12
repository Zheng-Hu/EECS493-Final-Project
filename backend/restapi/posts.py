"""REST API for posts."""
import flask
from flask import jsonify,request
import insta485
from functools import wraps
import insta485

class InvalidUsage(Exception):
  status_code = 400
  def __init__(self, message='Bad Request', status_code=None, payload=None):
      Exception.__init__(self)
      self.message = message
      if status_code is not None:
          self.status_code = status_code
      self.payload = payload

  def to_dict(self):
      rv = dict(self.payload or ())
      rv['message'] = self.message
      rv["status_code"] = self.status_code
      return rv
            
@insta485.app.route('/api/v1/', methods = ["GET"])
def api():
  context = {
    "posts": "/api/v1/posts/",
    "url": "/api/v1/"
  }
  return flask.jsonify(**context);

@insta485.app.route('/api/v1/posts/', methods =["GET"])
def posts():
  db = insta485.model.get_db()
  size = flask.request.args.get("size",default=10,type=int)
  page = flask.request.args.get("page",default=0,type=int)

  username = get_username()
    
  url = "/api/v1/posts/"
  context = {
      "url": url
  }
  cur = db.execute(
                   "SELECT p.created AS created, ('/uploads/' || p.filename) AS imgUrl, p.owner AS owner, "
                   "('/uploads/' || u.filename) AS ownerImgUrl, ('/users/' || u.username) AS ownerShowUrl, ('/posts/' || p.postid) AS postShowUrl, "
                   "p.postid AS postid, ('/api/v1/p/' || p.postid || '/') AS url " 
                   "FROM posts AS p JOIN users AS u ON p.owner=u.username "
                   "WHERE p.owner=? OR p.owner IN (SELECT username2 FROM following WHERE username1=?) ORDER BY created DESC, postid DESC LIMIT ? OFFSET ? * ?",\
                   (username,username,size,size,page,))
  
  context['results'] = list(cur.fetchall())
  cur = db.execute( "SELECT * FROM (SELECT CASE likes.owner WHEN ? THEN true ELSE false END lognameLikesThis, "
                     "COUNT (*) AS numLikes FROM likes JOIN posts AS p ON likes.postid = p.postid "
                     "WHERE p.owner=? OR p.owner IN (SELECT username2 FROM following WHERE username1=?) ORDER BY p.created DESC, p.postid DESC LIMIT ? OFFSET ? * ?)"
                     "JOIN "
                     "(SELECT ('/api/v1/likes/' || likes.likeid || '/') AS url "
                     "FROM likes JOIN posts AS p ON likes.owner = ? AND likes.postid = p.postid "
                     "WHERE p.owner=? OR p.owner IN (SELECT username2 FROM following WHERE username1=?) ORDER BY p.created DESC, p.postid DESC LIMIT ? OFFSET ? * ?)",\
                     (username, username,username, size, size, page, username, username,username, size, size, page, ))
  context['likes'] = list(cur.fetchall())
  cur = db.execute("SELECT COUNT(*) AS num FROM posts WHERE owner=? OR "
                   "owner IN (SELECT username2 FROM following WHERE username1=?)", \
                     (username,username,))
  if size*(page+1) >= cur.fetchall()[0]["num"]:
    context['next'] = ''
  else:
    context['next'] = f"/api/v1/p/?size={size}&page={page+1}"
  return flask.jsonify(**context);

@insta485.app.route('/api/v1/posts/<int:postid>/', methods=["GET"])
def get_post(postid):
    db = insta485.model.get_db()
    cur = db.execute("""SELECT p.created AS created, ('/uploads/' || p.filename) AS imgUrl, p.owner AS owner, 
        ('/uploads/' || u.filename) AS ownerImgUrl, ('/users/' || p.owner || '/') AS ownerShowUrl, 
        ('/posts/' || p.postid || '/') AS postShowUrl, p.postid AS postid, ('/api/v1/posts/' || p.postid || '/') AS url
        FROM posts AS p JOIN users AS u ON p.owner=u.username WHERE p.postid=?""",(postid,))
    context = cur.fetchall()[0]
    
    cur = db.execute("SELECT comments.commentid AS commentid, CASE comments.owner WHEN ? THEN true ELSE false END lognameOwnsThis, "
                     "comments.owner AS owner, ('/users/' || comments.owner || '/') AS ownerShowUrl, "
                     "comments.text, ('/api/v1/comments/' || comments.commentid || '/') AS url "
                     "FROM comments JOIN posts ON posts.postid = comments.postid WHERE posts.postid = ?",(username, postid,))
    context["comments"] = list(cur.fetchall())
    
    cur = db.execute("SELECT * FROM (SELECT CASE likes.owner WHEN ? THEN true ELSE false END lognameLikesThis, "
                     "COUNT (*) AS numLikes FROM likes WHERE likes.postid = ?) "
                     "JOIN "
                     "(SELECT ('/api/v1/likes/' || likes.likeid || '/') AS url "
                     "FROM likes WHERE likes.owner = ? AND likes.postid = ?)", (username, postid, username, postid, ))
    
    likes = cur.fetchall()

    if len(likes)== 0:
      context["likes"] = {
        "numLikes": 0,  
        "lognameLikesThis": 0,  
        "url": None,
      }
    else:
      context["likes"] = likes[0]

    return flask.jsonify(**context), 200
  
    
