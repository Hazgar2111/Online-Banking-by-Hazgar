from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path
from blockchain import views
from blockchain.views import *

urlpatterns = [
    re_path('^get_chain$', views.get_chain, name="get_chain"),
    re_path('^mine_block$', views.mine_block, name="mine_block"),
    re_path('^add_transaction$', views.add_transaction, name="add_transaction"),  # New
    re_path('^is_valid$', views.is_valid, name="is_valid"),  # New
    re_path('^connect_node$', views.connect_node, name="connect_node"),  # New
    re_path('^replace_chain$', views.replace_chain, name="replace_chain"),  # New
]