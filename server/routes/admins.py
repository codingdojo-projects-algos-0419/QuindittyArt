from config import app
from server.controllers import users
from server.controllers import admins

app.add_url_rule('/admin_page', view_func=admins.admin_page, endpoint='admin_page')
app.add_url_rule('/admin_lvl_increase/<user_id>', view_func=admins.admin_lvl_increase, endpoint='admins:admin_lvl_increase')
app.add_url_rule('/admin_lvl_decrease/<user_id>', view_func=admins.admin_lvl_decrease, endpoint='admins:admin_lvl_decrease')
app.add_url_rule('/upload_background', view_func=admins.upload_background, endpoint='admins:upload_background', methods=['POST', 'GET'])
app.add_url_rule('/change_background', view_func=admins.change_background, endpoint='admins:change_background', methods=['POST', 'GET'])
app.add_url_rule('/delete_user/<user_id>', view_func=admins.delete_user, endpoint='admins:delete_user')