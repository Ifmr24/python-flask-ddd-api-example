"""  User Controller Module  """
from marshmallow import ValidationError
from src.domain.entities.user import IUser, UserSchema
from src.domain.controllers.user import IUserController
from src.domain.services.user import IUserService


class UserController(IUserController):
    """ User Controller """

    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    def create_user(self, user: IUser) -> IUser:
        """ Create a new user """
        schema = UserSchema()

        try:
            schema.load(user)
        except ValidationError as e:
            return e.messages, 400

        return self.user_service.create_user(user)

    def list_users(self) -> list[IUser]:
        """ List all users """
        return self.user_service.list_users()

    def get_user(self, user_id: str) -> IUser:
        """ Get a user by id """
        return self.user_service.get_user(user_id)

    def update_user(self, user: IUser) -> IUser:
        """ Update a user """
        return self.user_service.update_user(user)

    def delete_user(self, user_id: str) -> None:
        """ Delete a user """
        return self.user_service.delete_user(user_id)
