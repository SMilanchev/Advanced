from project.user import User


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        self.user_records.remove(user)

        if user in self.rented_books:
            del self.rented_books[user.username]  # NOTE

    def change_username(self, user_id: int, new_username: str):
        user_ids = [user.user_id for user in self.user_records]
        if user_id not in user_ids:
            return f"There is no user with id = {user_id}!"
        user = self.user_records[user_ids.index(user_id)]
        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"
        else:
            user.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

