from config import app
from server.controllers import posts

app.add_url_rule('/posts/creating', view_func=posts.create, endpoint="posts:create", methods=['POST'])
app.add_url_rule('/posts/<quote_id>/like', view_func=posts.like, endpoint='posts:like', methods=['POST', 'GET'])
app.add_url_rule('/posts/<quote_id>/delete', view_func=posts.delete, endpoint='posts:delete', methods=['POST', 'GET'])
