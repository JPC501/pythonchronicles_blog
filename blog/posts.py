from flask import Blueprint, render_template, redirect, request, g, flash, url_for
from .auth import login_required
from .models.posts import Posts
from . import db


bp_post = Blueprint('post', __name__, url_prefix='/post')

#create posts
@bp_post.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        info = request.form.get('info')
        url = request.form.get('url')
        url = url.replace(' ', '_')
        content = request.form.get('ckeditor')
        
        
        post = Posts(g.user.id, title, content, info, url, created=None)
        post_url = post.query.filter_by(url=url).first()
        
        error = None
        
        if post_url == None:
            db.session.add(post)
            db.session.commit()
            flash(f'El post {post.title} se registro correctamente')
            return redirect(url_for('auth.profile'))
        else:
            error = 'La url del post ya existe'
        flash(error)
        
    return render_template('authentication/create_post.html')

#edit post
@bp_post.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Posts.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.info = request.form.get('info')
        post.content_post = request.form.get('ckeditor')
        
        db.session.commit()
        flash('El post se actualizo correctamente')
        return redirect(url_for('auth.profile'))
    
    return render_template('authentication/edit_post.html', post=post)


#delete post
@bp_post.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Posts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('auth.profile'))