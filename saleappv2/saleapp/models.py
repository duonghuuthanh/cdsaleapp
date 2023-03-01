from saleapp import app, db
from sqlalchemy import Column, String, Integer, Text, Float, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id))


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Điện thoại di động')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        db.create_all()