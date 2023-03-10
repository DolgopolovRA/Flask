from blog.models import User
from blog.app import app, db


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    admin = User(username="admin", is_staff=True, is_active=True)
    james = User(username="james", is_staff=False, is_active=True)
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
