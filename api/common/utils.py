from api import db
from api.database.models import User

product_max = User('Max', 8888,'https://picsum.photos/id/1047/1200/600', '', '')
db.session.add(product_max)
db.session.commit()