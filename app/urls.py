from django.urls import path
from .import views
urlpatterns=[
    path('',views.MytemplateView,name="MytemplateView"),
    # path('',views.MytemplateView.as_view(),name="MytemplateView"),
    path('detailedview/<int:pk>/',views.detailedview,name="detailedview"),
    path('user-login/',views.user_login,name="user-login"),
    path('LogoutView/',views.LogoutView.as_view(),name="LogoutView"),
    path('event/',views.event,name="event"),
    path('CheckPaymentView/',views.CheckPaymentView.as_view(),name="CheckPaymentView"),
    # path('calculate_order_amount',views.calculate_order_amount),
    # path('create_payment',views.create_payment,name="create_payment"),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('successview/', views.successview, name='successview'),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('eventlist',views.eventlist,name="eventlist"),
    path('userevents',views.userevents,name="userevents"),
    path('about',views.about,name="about"),
    # path('detailedview/<int:pk>/add_comment/',views.add_comment(),name="add_comment"),
]