from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    # System endpoints
    path('systems/', views.SystemsSet.as_view(), name='system-list'),
    path('system/<int:pk>', views.SystemInfo.as_view(), name='system-basic'),
    path('system/full/<int:pk>',
	    views.SystemDetailed.as_view(), name='system-detail'),
    # Component Create endpoints
    path('component/create/', views.ComponentC.as_view(),),
    path('components/create/', views.ComponentSC.as_view(),),
    path('componentp/create/', views.ComponentPC.as_view(),),
    # Component Read Update Delete endpoints
    path('component/RUD/<int:pk>',
	    views.ComponentRUD.as_view(), name='component-detail'),
    path('components/RUD/<int:pk>',
	    views.ComponentSRUD.as_view(), name='component_state-detail'),
    path('componentp/RUD/<int:pk>',
	    views.ComponentPRUD.as_view(), name='component_property-detail'),
    # Entity Create endpoints
    path('entity/create/', views.EntityC.as_view(),),
    path('entitys/create/', views.EntitySC.as_view(),),
    path('entityp/create/', views.EntityPC.as_view(),),
    # Entity Read Update Delete endpoints
    path('entity/RUD/<int:pk>', views.EntityRUD.as_view(),
	    name='environmental_entity-detail'),
    path('entitys/RUD/<int:pk>', views.EntitySRUD.as_view(),
	    name='environmental_state-detail'),
    path('entityp/RUD/<int:pk>', views.EntityPRUD.as_view(),
	    name='environmental_property-detail'),
	# Rules Create endpoints
    path('rules/create/', views.RulesC.as_view()),
    # Entity Read Update Delete endpoints
    path('rules/RUD/<int:pk>', views.RulesRUD.as_view(),
         name='transition_rules-detail'),

]
urlpatterns = [
    path('', include(format_suffix_patterns(urlpatterns))),
    path('', include(router.urls)),

]
