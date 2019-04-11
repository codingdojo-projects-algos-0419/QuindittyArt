from config import app
from server.controllers import users

app.add_url_rule('/users/new', view_func=users.new, endpoint="users:new")
app.add_url_rule('/users/create', view_func=users.create, endpoint="users:create", methods=['POST'])
app.add_url_rule('/users/login', view_func=users.login, endpoint="users:login", methods=['POST'])
app.add_url_rule('/users/logout', view_func=users.logout, endpoint="users:logout")
app.add_url_rule('/users/<user_id>', view_func=users.users_quotes, endpoint='users:users_quotes')
app.add_url_rule('/users/<user_id>/edit', view_func=users.edit, endpoint='users:edit', methods=['POST','GET'])
app.add_url_rule('/users/<user_id>/editing', view_func=users.editing, endpoint='users:editing', methods=['POST', 'GET'])
