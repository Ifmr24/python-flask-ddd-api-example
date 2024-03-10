""" This module contains the UserRepository class """
import json
from bson import json_util, ObjectId
from src.domain.entities.user import IUser
from src.domain.repositories.user import IUserRepository


class UserRepository(IUserRepository):
    """ User Repository """

    def __init__(self, db):
        self.db = db

    def create_user(self, user: IUser) -> IUser:
        """ Create a new user """
        if user is None:
            raise ValueError("User cannot be None")
        self.db.get_collection('users').insert_one(user)
        return json.loads(json_util.dumps(user))

    def list_users(self) -> list[IUser]:
        """ List all users """
        users = self.db.get_collection('users').find({})
        return json.loads(json_util.dumps(users))

    def get_user(self, user_id: str) -> IUser:
        """ Get a user by id """
        user = self.db.get_collection('users').find_one(
            {"_id": ObjectId(user_id)})

        if user is None:
            raise ValueError("User not found")

        return json.loads(json_util.dumps(user))

    def update_user(self, user: IUser) -> IUser:
        """ Update a user """
        if user is None:
            raise ValueError("User cannot be None")
        user_id = user["_id"]
        del user["_id"]
        self.db.get_collection('users').update_one(
            {"_id": ObjectId(user_id)}, {"$set": user})
        return json.loads(json_util.dumps(user))

    def delete_user(self, user_id: str) -> None:
        """ Delete a user """
        self.db.get_collection('users').delete_one({"_id": ObjectId(user_id)})
