from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db, dao
from saleapp.models import Category, Product
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__('ADMIN')


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class ProductView(AdminView):
    column_list = ['id', 'name', 'price', 'category_id']


class StatsView(AuthenticatedView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html',
                           data=dao.revenue_by_product(),
                           cates=dao.count_products_by_cate())


class LogoutView(AuthenticatedView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


admin = Admin(app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(AdminView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name='Stats'))
admin.add_view(LogoutView(name='Logout'))
