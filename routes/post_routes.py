from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from extensions import db
from models.post import Post


post = Blueprint("post", __name__)


@post.route("/posts")
def posts():

    all_posts = Post.query.order_by(
        Post.created_at.desc()
    ).all()

    return render_template(
        "posts.html",
        posts=all_posts
    )


@post.route(
    "/posts/create",
    methods=["GET", "POST"]
)
@login_required
def create_post():

    if request.method == "POST":

        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:

            flash(
                "Title and content are required."
            )

            return redirect(
                url_for("post.create_post")
            )

        new_post = Post(
            title=title,
            content=content,
            user_id=current_user.id
        )

        db.session.add(new_post)
        db.session.commit()

        flash(
            "Post created successfully!"
        )

        return redirect(
            url_for("post.posts")
        )

    return render_template(
        "create_post.html"
    )


@post.route("/posts/<int:post_id>")
def view_post(post_id):

    blog_post = Post.query.get_or_404(
        post_id
    )

    return render_template(
        "post_detail.html",
        post=blog_post
    )


@post.route(
    "/posts/<int:post_id>/edit",
    methods=["GET", "POST"]
)
@login_required
def edit_post(post_id):

    blog_post = Post.query.get_or_404(
        post_id
    )

    if blog_post.user_id != current_user.id:

        flash(
            "You are not allowed to edit this post."
        )

        return redirect(
            url_for("post.posts")
        )

    if request.method == "POST":

        blog_post.title = request.form[
            "title"
        ].strip()

        blog_post.content = request.form[
            "content"
        ].strip()

        db.session.commit()

        flash(
            "Post updated successfully!"
        )

        return redirect(
            url_for(
                "post.view_post",
                post_id=blog_post.id
            )
        )

    return render_template(
        "edit_post.html",
        post=blog_post
    )


@post.route(
    "/posts/<int:post_id>/delete",
    methods=["POST"]
)
@login_required
def delete_post(post_id):

    blog_post = Post.query.get_or_404(
        post_id
    )

    if blog_post.user_id != current_user.id:

        flash(
            "You are not allowed to delete this post."
        )

        return redirect(
            url_for("post.posts")
        )

    db.session.delete(blog_post)
    db.session.commit()

    flash(
        "Post deleted successfully!"
    )

    return redirect(
        url_for("post.posts")
    )