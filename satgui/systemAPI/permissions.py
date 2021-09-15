from rest_framework import permissions
from DoS.models import System
from DoS.models import Component, Component_Property, Component_State
from DoS.models import Environmental_Entity, Environmental_Property, Environmental_State
from django.http import QueryDict
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admin to edit it.
    """
    message = 'You dont own that System/Component/Entity'

    def has_permission(self, request, view):
        if request.user.is_staff or request.method == 'GET':  # gives admin edit permission right away or view
            return True
        else:
            name = view.get_view_name() 
        # will get the owner of the parent (system/component/entity) to make sure the user owns it when updating an object
        if name in ['Component Rud', 'Component C', 'Entity C', 'Entity Rud','Rules C','Rules Rud']:
            self.message = 'You dont own that System'
            usr = request.data.get("System")
            if usr is None:
                return True
            sys = System.objects.get(pk=usr)
            if not sys.get_owner() == request.user:
                return False
        elif name in ['Component Srud', 'Component Sc', 'Component Pc', 'Component Prud']:
            self.message = 'You dont own that Component'

            usr = request.data.get('Component')
            if usr is None:
                return True
            sys = Component.objects.get(pk=usr)
            if not sys.get_owner() == request.user:
                return False
        elif name in ['Entity Srud', 'Entity Sc', 'Entity Pc', 'Entity Prud']:
            self.message = 'You dont own that Entity'

            usr = request.data.get('Environmental_Entity')
            if usr is None:
                return True
            sys = Environmental_Entity.objects.get(pk=usr)
            if not sys.get_owner() == request.user:
                return False
        return True

    # makes sure that the requesting user owns the object they are trying to update
    def has_object_permission(self, request, view, obj):

        return obj.get_owner() == request.user or request.user.is_staff


class IsUser(permissions.BasePermission):
    """
    Custom permission to allow regular users to look and update their information from the api view.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
