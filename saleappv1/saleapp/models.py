from sqlalchemy import Column, String, Integer
from saleapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Điện thoại di động')
        c2 = Category(name='Máy tính bảng')
        db.session.add_all([c1, c2])
        db.session.commit()
        # db.create_all()