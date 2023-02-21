from app import app, db
from preconditions import create_admin_role, create_admin_user


def do_preconditions():
    create_admin_role()
    create_admin_user()


if __name__ == "__main__":
    with app.app_context():
        db.metadata.create_all(db.engine)
    do_preconditions()

    app.run(host="0.0.0.0", port=5005)
