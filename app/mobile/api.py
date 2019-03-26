from flask import jsonify, request, current_app, url_for, g
from . import mobile
from .. import db
from ..models import UserData, Permission
from .decorators import permission_required
from .errors import forbidden


@mobile.route('/test/')
def connect_test():
    response = {}
    response.update({"state": "Success login"})
    response.update({"message": "You are success login, {}".format(g.current_user.username)})
    response.update({"data": ""})

    return jsonify(response)


@mobile.route('/data/', methods=['POST'])
@permission_required(Permission.WRITE)
def data_upload():
    post = UserData.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
           {'Location': url_for('mobile.get_data', id=post.id)}


@mobile.route('/data/<int:id>', methods=['GET'])
def get_data(id):
    post = UserData.query.get_or_404(id)
    return jsonify(post.to_get_json())


@mobile.route('/data/<int:id>', methods=['PUT'])
@permission_required(Permission.WRITE)
def data_update(id):
    post = UserData.query.get_or_404(id)
    if g.current_user != post.author and \
            not g.current_user.can(Permission.ADMIN):
        return forbidden('Insufficient permissions')
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())


# @mobile.route('/data/', methods=['GET'])
# def get_all_data():
#     page = request.args.get('page', 1, type=int)
#     pagination = UserData.query.paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     # pagination.author = g.current_user
#     posts = pagination.items
#     prev = None
#     if pagination.has_prev:
#         prev = url_for('mobile.get_all_data', page=page-1)
#     next = None
#     if pagination.has_next:
#         next = url_for('mobile.get_all_data', page=page+1)
#     return jsonify({
#         'posts': [post.to_json() for post in posts],
#         'prev': prev,
#         'next': next,
#         'count': pagination.total
#     })
