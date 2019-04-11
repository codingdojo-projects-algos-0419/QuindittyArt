from config import app
from server.controllers import users

app.add_url_rule('/admin_page', view_func=users.admin_page, endpoint='admin_page')
app.add_url_rule('/admin_lvl_increase/<user_id>', view_func=users.admin_lvl_increase, endpoint='admins:admin_lvl_increase')
app.add_url_rule('/admin_lvl_decrease/<user_id>', view_func=users.admin_lvl_decrease, endpoing='admins:admin_lvl_decrease')
app.add_url_rule('/upload_background', view_func=admins.upload_background, endpoint='admins:upload_background')