from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from prototype.auth import login_required
from prototype.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
	return list()

def list():
	db = get_db()
	posts = db.execute(
		'SELECT p.id, p.title, p.body, p.created, p.author_id, u.username'
		'  FROM post p, user u'
		' WHERE p.author_id = u.id'
		' ORDER BY created DESC'
	).fetchall()
	return render_template('blog/list.html', posts = posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
	if request.method == 'POST':
		title = request.form['title']
		body = request.form['body']

		if not title:
			flash('Title is required.')
		else:
			db = get_db()
			db.execute(
				'INSERT INTO post (title, body, author_id) '
				'VALUES (?,?,?)', (title, body, g.user['id'])
			)
			db.commit()
			return redirect(url_for('index'))
	return render_template('blog/create.html')

def get_post(id, check_author=True):
	post = get_db().execute(
		'SELECT p.id, p.title, p.body, p.created, p.author_id, u.username'
		'  FROM post p, user u'
		' WHERE p.id = ?',
		(id,)
	).fetchone()

	print(post)
	if post is None:
		abort(404, 'Post id {0} does not exist.'.format(id))

	if check_author and post['author_id'] != g.user['id']:
		abort(403)

	return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
	post = get_post(id)

	if request.method == 'POST':
		title = request.form['title']
		body = request.form['body']

		if not title:
			flash('Title is required.')
		else:
			db = get_db()
			db.execute(
				'UPDATE post SET title = ?, body = ?'
				' WHERE id = ?'
				'   AND author_id = ?',
				(title, body, id, g.user['id'])
			)
			db.commit()
			return redirect(url_for('index'))
	return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('GET', 'POST'))
@login_required
def delete(id):
	if request.method == 'POST':
		get_post(id)
		db = get_db()
		db.execute('DELETE FROM post WHERE id = ?', (id,))
		db.commit()
	print('endend')
	return redirect(url_for('index'))
