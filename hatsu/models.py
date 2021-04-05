from hatsu import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(int(user_id))


class Scraped(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    thumblist = db.Column(db.Text, unique=True, nullable=False)
    titlelist = db.Column(db.Text, unique=True, nullable=False)
    coverimg = db.Column(db.Text, unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"scrape('{self.thumblist}','{self.titlelist}','{self.coverimg}','{self.description}')"


class Register(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"Register('{self.email}','{self.password}')"

class Fan(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"FanFiction('{self.title}','{self.content}')"