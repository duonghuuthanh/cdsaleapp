from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db
from saleapp.models import Category, Product


admin = Admin(app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
