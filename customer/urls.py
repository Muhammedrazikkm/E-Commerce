from django.urls import path
from customer import views
urlpatterns=[
    path("register/",views.SignupView.as_view(),name="signup"),
    path("signin/",views.SignInView.as_view(),name="login"),
    path("home/",views.IndexView.as_view(),name="home"),
    path('products/<int:id>',views.ProductDetailView.as_view(),name="product-detail"),
    path('products/<int:id>/carts/add',views.AddtoCartView.as_view(),name="cart-add"),
    path('customer/carts/all',views.CartListView.as_view(),name="cart-list"),
    path('carts/<int:id>/change',views.CartRemoveView.as_view(),name="cart-change"),
    path('orders/add/<int:id>',views.MakeOrderView.as_view(),name="create-order"),
    path('orders/all',views.MyordersView.as_view(),name="my-orders"),
    path('orders/<int:id>/cancel',views.OrderCancelView.as_view(),name="order-cancel"),
    path('offers/all',views.DiscountProductView.as_view(),name="offer-list"),
    path('reviews/<int:id>/add',views.ReviewCreateView.as_view(),name="review-add"),
    path('logout',views.signout_view,name="signout")
]