from  extensions import db
from passlib.hash import bcrypt, bcrypt_sha256 
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    __tablename__= 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def set_password(self, password: str):
        print("SELF",self)
        if len(password.encode('utf-8')) > 72:
            password = password[:72]
            raise ValueError("La contraseña no puede exceder 72 bytes")
        #self.password = bcrypt_sha256.hash(password)
        self.password = pbkdf2_sha256.hash(password)
    
    def check_password(self, password : str) -> bool:
        print("SELF VALUE")
        print(self)
        #ret
        return pbkdf2_sha256.verify(password, self.password)

    def to_dict(self):
        return{
            'id': self.id,
            'username':self.username,
             'email': self.email,
        }
                      


