from flask import Blueprint, request, jsonify

from flask_login import (
    login_required,
    current_user
)

from extensions import db
from models.post import Post
from models.comment import Comment


api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


def post_to_dict(post):

    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
        "user_id": post.user_id,
        "created_at": (
            post.created_at.isoformat()
            if post.created_at
            else None
        ),
        "updated_at": (
            post.updated_at.isoformat()
            if post.updated_at
            else None
        )
    }


def comment_to_dict(comment):

    return {
        "id": comment.id,
        "content": comment.content,
        "author": comment.author.username,
        "user_id": comment.user_id,
        "post_id": comment.post_id,
        "created_at": (
            comment.created_at.isoformat()
            if comment.created_at
            else None
        )
    }


# GET all posts
@api.route("/posts", methods=["GET"])
def get_posts():

    posts = Post.query.order_by(
        Post.created_at.desc()
    ).all()

    return jsonify([
        post_to_dict(p)
        for p in posts
    ])


# GET one post
@api.route(
    "/posts/<int:post_id>",
    methods=["GET"]
)
def get_post(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    return jsonify(
        post_to_dict(post)
    )


# CREATE post
@api.route(
    "/posts",
    methods=["POST"]
)
@login_required
def create_api_post():

    data = request.get_json()

    if not data:

        return jsonify({
            "error": "JSON body required"
        }), 400

    title = data.get("title", "").strip()
    content = data.get("content", "").strip()

    if not title or not content:

        return jsonify({
            "error": "Title and content are required"
        }), 400

    new_post = Post(
        title=title,
        content=content,
        user_id=current_user.id
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify(
        post_to_dict(new_post)
    ), 201


# UPDATE post
@api.route(
    "/posts/<int:post_id>",
    methods=["PUT"]
)
@login_required
def update_api_post(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    if post.user_id != current_user.id:

        return jsonify({
            "error": "Not authorized"
        }), 403

    data = request.get_json()

    if "title" in data:
        post.title = data["title"].strip()

    if "content" in data:
        post.content = data["content"].strip()

    db.session.commit()

    return jsonify(
        post_to_dict(post)
    )


# DELETE post
@api.route(
    "/posts/<int:post_id>",
    methods=["DELETE"]
)
@login_required
def delete_api_post(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    if post.user_id != current_user.id:

        return jsonify({
            "error": "Not authorized"
        }), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({
        "message": "Post deleted successfully"
    })


# GET comments
@api.route(
    "/posts/<int:post_id>/comments",
    methods=["GET"]
)
def get_comments(post_id):

    Post.query.get_or_404(post_id)

    comments = Comment.query.filter_by(
        post_id=post_id
    ).order_by(
        Comment.created_at.desc()
    ).all()

    return jsonify([
        comment_to_dict(c)
        for c in comments
    ])


# CREATE comment
@api.route(
    "/posts/<int:post_id>/comments",
    methods=["POST"]
)
@login_required
def create_api_comment(post_id):

    Post.query.get_or_404(post_id)

    data = request.get_json()

    if not data:

        return jsonify({
            "error": "JSON body required"
        }), 400

    content = data.get(
        "content",
        ""
    ).strip()

    if not content:

        return jsonify({
            "error": "Comment cannot be empty"
        }), 400

    new_comment = Comment(
        content=content,
        user_id=current_user.id,
        post_id=post_id
    )

    db.session.add(new_comment)
    db.session.commit()

    return jsonify(
        comment_to_dict(new_comment)
    ), 201