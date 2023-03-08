class UserBase:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def check_password(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

    def get_user(self, username):
        return {"username": username}