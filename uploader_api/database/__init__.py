from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from uploader_api.database.models import UploadIntent  # noqa
    # db.drop_all()
    db.create_all()
