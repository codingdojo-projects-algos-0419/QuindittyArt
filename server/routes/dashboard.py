from config import app
from server.controllers import dashboard

app.add_url_rule('/', view_func=dashboard.dashboard, endpoint="dashboard")
app.add_url_rule('/about_me', view_func=dashboard.about_me, endpoint='about_me')