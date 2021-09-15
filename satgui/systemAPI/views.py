from rest_framework import permissions
from DoS.models import System
from DoS.models import Component, Component_Property, Component_State, Transition_Rules
from DoS.models import Environmental_Entity, Environmental_Property, Environmental_State
from .serializers import SystemSerializer, SystemDetailedSerializer, UserSerializer, RulesSerializer
from .serializers import ComponentSerializer, ComponentPropertySerializer, ComponentStateSerializer
from .serializers import EntitySerializer, EntityStateSerializer, EntityPropertySerializer
from rest_framework import generics, viewsets
from .permissions import IsOwner, IsUser
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

# ___________________SYSTEM______________________________________

# Gets List of systems by User has id, name, description
class SystemsSet(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)
        
    def get_queryset(self, *args, **kwargs):
        return System.objects.all().filter(User=self.request.user)

# Can display update and delete a system
class SystemInfo(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return System.objects.all().filter(User=self.request.user)

# Gets all the data of a system by User
class SystemDetailed(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = System.objects.all()
    serializer_class = SystemDetailedSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return System.objects.all().filter(User=self.request.user)

# ___________________COMPONENT______________________________________

# Create Component
class ComponentC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        return Component.objects.all().filter(System__User=self.request.user)

# Read Update Delete Component
class ComponentRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Component.objects.all().filter(System__User=self.request.user)

# ___________________COMPONENT STATE______________________________________

# Create Component State
class ComponentSC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Component_State.objects.all()
    serializer_class = ComponentStateSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Component_State.objects.all().filter(Component__System__User=self.request.user)

# Read Update Delete Component State
class ComponentSRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Component_State.objects.all()
    serializer_class = ComponentStateSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Component_State.objects.all().filter(Component__System__User=self.request.user)

# ___________________COMPONENT PROPERTY______________________________________

# Create Component Property
class ComponentPC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Component_Property.objects.all()
    serializer_class = ComponentPropertySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Component_Property.objects.all().filter(Component__System__User=self.request.user)

# Read Update Delete Component Property
class ComponentPRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Component_Property.objects.all()
    serializer_class = ComponentPropertySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Component_Property.objects.all().filter(Component__System__User=self.request.user)
        
# ___________________ENTITY______________________________________

# Create Env Entity
class EntityC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Environmental_Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Environmental_Entity.objects.all().filter(System__User=self.request.user)

# Read Update Delete Env Entity
class EntityRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Environmental_Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Environmental_Entity.objects.all().filter(System__User=self.request.user)

# ___________________ENTITY STATE______________________________________

# Create Env Entity State
class EntitySC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Environmental_State.objects.all()
    serializer_class = EntityStateSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Environmental_State.objects.all().filter(Environmental_Entity__System__User=self.request.user)

# Read Update Delete Env Entity State
class EntitySRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Environmental_State.objects.all()
    serializer_class = EntityStateSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Environmental_State.objects.all().filter(Environmental_Entity__System__User=self.request.user)

# ___________________ENTITY PROPERTIES______________________________________

# Create Env Entity Property
class EntityPC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Environmental_Property.objects.all()
    serializer_class = EntityPropertySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Environmental_Property.objects.all().filter(Environmental_Entity__System__User=self.request.user)

# Read Update Delete Env Entity Property
class EntityPRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Environmental_Property.objects.all()
    serializer_class = EntityPropertySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Environmental_Property.objects.all().filter(Environmental_Entity__System__User=self.request.user)

# ___________________TRANSITION RULES______________________________________

# Create TRANSITION RULES
class RulesC(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Transition_Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Transition_Rules.objects.all().filter(System__User=self.request.user)

# Read Update Delete TRANSITION RULES
class RulesRUD(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Transition_Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Transition_Rules.objects.all().filter(System__User=self.request.user)

# ___________________User______________________________________

# View, edit, delete user/ if admin show list of users
class UserViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated, IsUser]
        return [permission() for permission in permission_classes]
