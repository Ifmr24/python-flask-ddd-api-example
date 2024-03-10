""" UserRepository interface """
from abc import ABC, abstractmethod
from src.domain.entities.user import IUser


class IUserRepository(ABC):
    """ User Repository Interface """
    @abstractmethod
    def create_user(self, user: IUser) -> IUser:
        """ Create a new user """

    @abstractmethod
    def list_users(self) -> list[IUser]:
        """ List all users """

    @abstractmethod
    def get_user(self, user_id: str) -> IUser:
        """ Get a user by id """

    @abstractmethod
    def update_user(self, user: IUser) -> IUser:
        """ Update a user """

    @abstractmethod
    def delete_user(self, user_id: str) -> None:
        """ Delete a user """
