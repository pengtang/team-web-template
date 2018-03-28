from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required
from datetime import datetime
from project.extensions import db
from .models import Blogpost


blogs_blueprint = Blueprint(
    'blogs', __name__,
    template_folder='templates'
)


# use decorators to link the function to a url
@blogs_blueprint.route('/blogs', methods=['GET', 'POST'])
@login_required
def blog_home():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('blog_home.html', posts=posts)


@blogs_blueprint.route('/blogs/about')
def about():
    return render_template('about.html')


@blogs_blueprint.route('/blogs/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@blogs_blueprint.route('/blogs/add')
def add():
    return render_template('add.html')


@blogs_blueprint.route('/blogs/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('blogs.blog_home'))
