from config import app, db
from server.routes import quote_list, quotes, users

if __name__ == "__main__":
    app.run(debug=True)