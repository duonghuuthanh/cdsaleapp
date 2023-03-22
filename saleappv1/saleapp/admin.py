from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db, dao
from saleapp.models import Category, Product
from flask_admin import BaseView, expose


class ProductView(ModelView):
    column_list = ['id', 'name', 'price', 'category_id']


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html', data=dao.revenue_by_product())


admin = Admin(app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name='Stats'))
