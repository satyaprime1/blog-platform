from datetime import datetime

from extensions import db


class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey("posts.id"),
        nullable=False
    )

    author = db.relationship(
        "User",
        backref=db.backref(
            "comments",
            lazy=True
        )
    )

    post = db.relationship(
        "Post",
        backref=db.backref(
            "comments",
            lazy=True,
            cascade="all, delete-orphan"
        )
    )