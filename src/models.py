from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    @classmethod
    def create(cls, new_user):
        reg_user = cls(**new_user)
        db.session.add(reg_user)
        
        try:
            db.session.commit()
            return reg_user
        except Exception as error:
            db.session.rollback()
            return None

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }