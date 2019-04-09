from config import app
from server.controllers import quote_list

app.add_url_rule('/', view_func=quote_list.root, endpoint="root")
app.add_url_rule('/quote_list', view_func=quote_list.quote_list, endpoint="quote_list")
