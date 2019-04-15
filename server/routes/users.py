from config import app
from server.controllers import users

app.add_url_rule('/users/login-and-registration', view_func=users.login_and_registration, endpoint="users:login_and_registration")
app.add_url_rule('/users/create', view_func=users.create, endpoint="users:create", methods=['POST'])
app.add_url_rule('/users/login', view_func=users.login, endpoint="users:login", methods=['POST', 'GET'])
app.add_url_rule('/users/logout', view_func=users.logout, endpoint="users:logout")
app.add_url_rule('/users/<user_id>/account_page', view_func=users.account_page, endpoint='users:account_page', methods=['POST','GET'])
app.add_url_rule('/users/<user_id>/editing', view_func=users.editing, endpoint='users:editing', methods=['POST', 'GET'])
