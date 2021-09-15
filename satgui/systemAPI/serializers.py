from DoS.models import System, Component, Component_State, Component_Property, Transition_Rules
from DoS.models import Environmental_Entity, Environmental_Property, Environmental_State
from rest_framework import serializers
from django.contrib.auth.models import User


# Transition Rules__________________________________________________________
class RulesSerializer(serializers.ModelSerializer):

    link = serializers.HyperlinkedIdentityField(
        view_name='transition_rules-detail', format='html', read_only=True)

    class Meta:
        model = Transition_Rules
        fields = ['name', 'description', 'id','System','link']
        read_only_fields = ['id','link']

# Components__________________________________________________________
class ComponentStateSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name='component_state-detail', format='html', read_only=True)
    class Meta:
        model = Component_State
        fields = ['name', 'description', 'id', 'Component','link']
        read_only_fields = ['id']

class ComponentPropertySerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name='component_property-detail', format='html', read_only=True)
    class Meta:
        model = Component_Property
        fields = ['name', 'description', 'id', 'Component','link']
        read_only_fields = ['id']

class ComponentSerializer(serializers.ModelSerializer):
    properties = ComponentPropertySerializer(
        many=True, required=False, read_only=True)
    states = ComponentStateSerializer(
        many=True, required=False, read_only=True)
    link = serializers.HyperlinkedIdentityField(
        view_name='component-detail', format='html', read_only=True)
    class Meta:
        model = Component
        fields = ['name', 'description', 'id', 'properties', 'states','System','link']
        read_only_fields = ['id', 'properties', 'states','link']

# Environmental Entities__________________________________________________________
class EntityStateSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name='environmental_state-detail', format='html', read_only=True)
    class Meta:
        model = Environmental_State
        fields = ['name', 'description', 'id','Environmental_Entity','link']
        read_only_fields = ['id']

class EntityPropertySerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name='environmental_property-detail', format='html', read_only=True)
    class Meta:
        model = Environmental_Property
        fields = ['name', 'description', 'id', 'Environmental_Entity','link']
        read_only_fields = ['id']

class EntitySerializer(serializers.ModelSerializer):
    properties = EntityPropertySerializer(
        many=True, required=False, read_only=True)
    states = EntityStateSerializer(many=True, required=False, read_only=True)
    link = serializers.HyperlinkedIdentityField(
        view_name='environmental_entity-detail', format='html', read_only=True)
    class Meta:
        model = Environmental_Entity
        fields = ['name', 'description', 'id','properties','states','System','link']
        read_only_fields = ['id', 'properties', 'states']

# System__________________________________________________________
class SystemSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name='system-detail', format='html', read_only=True)
    User = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = System
        fields = ['name', 'description', 'User', 'id','link']
        read_only_fields = ['User','id']

class SystemDetailedSerializer(serializers.ModelSerializer):

    entities = EntitySerializer(many=True, read_only=True)
    components = ComponentSerializer(many=True, read_only=True)
    rules = RulesSerializer(many=True, read_only=True)
    class Meta:
        model = System
        fields = ['name','description','User','id','entities','components','rules']

# User__________________________________________________________
class UserSerializer(serializers.ModelSerializer):
    systems = serializers.HyperlinkedRelatedField(
        many=True, view_name='system-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'systems', 'email']
        read_only_fields = ['id']
