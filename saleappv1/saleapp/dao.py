from saleapp.models import Category, Product


def get_categories():
    return Category.query.all()


def get_products(kw=None, category_id=None):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))

    return query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)
