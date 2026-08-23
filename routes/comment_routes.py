from flask import (
    Blueprint,
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
from models.comment import Comment
from models.post import Post


comment = Blueprint(
    "comment",
    __name__
)


@comment.route(
    "/posts/<int:post_id>/comments",
    methods=["POST"]
)
@login_required
def add_comment(post_id):

    blog_post = Post.query.get_or_404(
        post_id
    )

    content = request.form[
        "content"
    ].strip()

    if not content:

        flash(
            "Comment cannot be empty."
        )

        return redirect(
            url_for(
                "post.view_post",
                post_id=post_id
            )
        )

    new_comment = Comment(
        content=content,
        user_id=current_user.id,
        post_id=blog_post.id
    )

    db.session.add(new_comment)
    db.session.commit()

    flash(
        "Comment added successfully!"
    )

    return redirect(
        url_for(
            "post.view_post",
            post_id=post_id
        )
    )


@comment.route(
    "/comments/<int:comment_id>/delete",
    methods=["POST"]
)
@login_required
def delete_comment(comment_id):

    user_comment = Comment.query.get_or_404(
        comment_id
    )

    post_id = user_comment.post_id

    if user_comment.user_id != current_user.id:

        flash(
            "You are not allowed to delete this comment."
        )

        return redirect(
            url_for(
                "post.view_post",
                post_id=post_id
            )
        )

    db.session.delete(user_comment)
    db.session.commit()

    flash(
        "Comment deleted successfully!"
    )

    return redirect(
        url_for(
            "post.view_post",
            post_id=post_id
        )
    )