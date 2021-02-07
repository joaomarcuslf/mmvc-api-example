from flask.cli import FlaskGroup

from models import db

from application import create_app

app = create_app()


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    pass


if __name__ == "__main__":
    cli()
