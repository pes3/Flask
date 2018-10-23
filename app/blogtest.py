from r'\Users\Patrick\githubb\Flask\app' import db
from app.models import User, Post
u = User(username='john', email='john@example.com')
db.session.add(u)
db.session.commit()

u = User.query.get(1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commmit()
