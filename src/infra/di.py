""" Dependency Injection """
from src.infra.repositories.user import UserRepository
from src.application.services.user import UserService
from src.infra.controllers.user import UserController
from src.infra.db.mongo import get_database

# db
mongodb = get_database()

# repositories
user_repository = UserRepository(mongodb)

# services
user_service = UserService(user_repository)

# controllers
user_controller = UserController(user_service)
