from config import app
from server.controllers import posts

app.add_url_rule('/new_post', view_func=posts.new_post, endpoint='posts:new_post')
app.add_url_rule('/posts/creating', view_func=posts.create, endpoint="posts:create", methods=['POST'])
app.add_url_rule('/posts/<post_id>', view_func=posts.view_post, endpoint='posts:view_post')
app.add_url_rule('/posts/<post_id>/like', view_func=posts.like, endpoint='posts:like', methods=['POST', 'GET'])
app.add_url_rule('/posts/<post_id>/delete', view_func=posts.delete, endpoint='posts:delete', methods=['POST', 'GET'])
app.add_url_rule('/posts/<post_id>/comment', view_func=posts.comment, endpoint='posts:comment', methods=['POST', 'GET'])
app.add_url_rule('/posts/<post_id>/comments/<comment_id>/delete', view_func=posts.delete_comment, endpoint='posts:delete_comment')