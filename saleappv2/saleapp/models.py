from saleapp import app, db
from sqlalchemy import Column, String, Integer


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Điện thoại di động')
        c2 = Category(name='Máy tính bảng')
        c3 = Category(name='Phụ kiện')
        db.session.add_all([c1, c2, c3])
        db.session.commit()
        # db.create_all()