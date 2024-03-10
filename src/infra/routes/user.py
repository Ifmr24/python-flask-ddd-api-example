""" User routes module """
from flask import Blueprint, request
from src.infra.di import user_controller

bp = Blueprint('user', __name__)


@bp.route('/api/users', methods=['POST'])
def create_user():
    """ Create a new user endpoint"""
    user_data = request.get_json()
    new_user = user_controller.create_user(user_data)
    return new_user, 201


@bp.route('/api/users', methods=['GET'])
def list_users():
    """ List all users endpoint """
    users = user_controller.list_users()
    return users, 200


@bp.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """ Get a user by id endpoint """
    user = user_controller.get_user(user_id)
    return user, 200


@bp.route('/api/users', methods=['PUT'])
def update_user():
    """ Update a user endpoint """
    user_data = request.get_json()
    updated_user = user_controller.update_user(user_data)
    return updated_user, 200


@bp.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ Delete a user endpoint """
    user_controller.delete_user(user_id)
    return '', 204
