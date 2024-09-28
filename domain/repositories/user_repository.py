# persistence/repositories/user_repository.py

from sqlalchemy.orm import Session
from domain.entities.users.user import User
from domain.repositories.i_base_repository import IBaseRepository

class UserRepository(IBaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int):
        return self.session.query(User).filter(User.id == id).first()

    def add(self, entity: User):
        self.session.add(entity)
        self.session.commit()

    def update(self, entity: User):
        self.session.merge(entity)
        self.session.commit()

    def delete(self, id: int):
        entity = self.get_by_id(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
