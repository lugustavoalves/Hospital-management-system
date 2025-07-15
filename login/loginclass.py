import sqlite3
import hashlib

class LoginSystem:
    def __init__(self, db_path="login.db"):
        self.db_path = db_path

    def _hash_password(self, password):
        """Hashes a password using SHA256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password, role):
        """Registers a new user."""
        hashed_password = self._hash_password(password)
        roles = ["admin", "doctor", "staff"]
        if role not in roles:
            return f"Error: Role '{role}' is invalid. Valid roles are: {', '.join(roles)}"
        else:
            try:
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                                (username, hashed_password, role))
                    conn.commit()
                    return f"User '{username}' successfully registered!"
            except sqlite3.IntegrityError:
                return f"Error: Username '{username}' is already taken."

    def login_user(self, username, password):
        """Logs in a user if the credentials are correct."""
        hashed_password = self._hash_password(password)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                           (username, hashed_password))
            user = cursor.fetchone()
            if user:
                role = user[-1]
                return f"Welcome, {username}!", role
            else:
                return "Error: Invalid username or password.", None

    def change_password(self, username, old_password, new_password):
        """Changes the user's password after validating the old password."""
        if self.login_user(username, old_password) == f"Welcome, {username}!":
            hashed_new_password = self._hash_password(new_password)
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET password = ? WHERE username = ?", 
                               (hashed_new_password, username))
                conn.commit()
                return f"Password for user '{username}' successfully updated!"
        else:
            return "Error: Old password is incorrect."
