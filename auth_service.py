from Database.db import get_connection
from models import User
import random
import bcrypt

class AuthService:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.current_user = None

    def generate_id(self):
        return str(random.randint(10**11, 10**12 - 1))
    
    def hashed_password(self, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    
    def register_user(self, email, password):
        try:
            user = User(
                id=self.generate_id(),
                email=email,
                password=self.hashed_password(password).decode('utf-8')
            )
            self.cursor.execute(
                "INSERT INTO users (id, email, password) VALUES (%s, %s, %s)",
                (user.id, user.email, user.password)
            )
            self.conn.commit()
            print("User registered successfully")
            print(f"Your login ID is {user.id}")
            print("Please remember this id so as to be able to log in")

        except Exception as e:
            self.conn.rollback()
            print("Error:", e)

    def login(self,user_id, password):
        self.cursor.execute(
            "SELECT password FROM users WHERE id = %s",
            (user_id,)
        )

        result = self.cursor.fetchone()

        if not result:
            print("User not found")
            return False
        
        stored_hash = result[0]

        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            self.current_user = user_id
            print('Login Successful')
            return True
        
        else:
            print("Wrong password")
            return False
        
    def get_user_id_by_email(self, email):
        self.cursor.execute(
            "SELECT id FROM users WHERE email = %s",
            (email,)
        )

        result = self.cursor.fetchone()

        if result:
            print(f"Your user ID is: {result[0]}")
            return result[0]
        else:
            print("Email not found")
            return None
        
    def logout(self):
        if self.current_user:
            print(f"User {self.current_user} logged out")
            self.current_user = None
        
        else:
            print("No user is currently logged in")
        
    def delete_user(self, user_id):
        self.cursor.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )
        self.conn.commit()
        print("User Deleted")
    
    def close(self):
        self.conn.close()