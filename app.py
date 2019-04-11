from config import app, db
from server.routes import dashboard, posts, users, admins

if __name__ == "__main__":
    app.run(debug=True)