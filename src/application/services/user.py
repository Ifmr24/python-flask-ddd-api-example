""" User Service """
from src.domain.entities.user import IUser
from src.domain.services.user import IUserService
from src.domain.repositories.user import IUserRepository


class UserService(IUserService):
    """ User Service """

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, user: IUser) -> IUser:
        """ Create a new user """
        return self.user_repository.create_user(user)

    def list_users(self) -> list[IUser]:
        """ List all users """
        return self.user_repository.list_users()

    def get_user(self, user_id: str) -> IUser:
        """ Get a user by id """
        return self.user_repository.get_user(user_id)

    def update_user(self, user: IUser) -> IUser:
        """ Update a user """
        return self.user_repository.update_user(user)

    def delete_user(self, user_id: str) -> None:
        """ Delete a user """
        return self.user_repository.delete_user(user_id)
