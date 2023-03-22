from server.src.services.user import User

class Admin(User):
    def __init__(self) -> None:
        super().__init__()

    # def set_permission(self, other, perm):
    #     db.set(self.id, other.id, perm)
