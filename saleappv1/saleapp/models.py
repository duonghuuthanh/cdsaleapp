from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from saleapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
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
        # db.session.add_all([c1, c2])
        # db.session.commit()
        # db.drop_all()
        db.create_all()