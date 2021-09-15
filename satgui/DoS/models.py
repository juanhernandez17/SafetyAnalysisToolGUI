from django.db import models
from django.contrib.auth.models import User

class System(models.Model):

	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	date_posted = models.DateTimeField(auto_now_add=True)
	# Foreign Key will delete users system if user is deleted
	User = models.ForeignKey(User, related_name='systems',on_delete=models.CASCADE)
	# systems = models.Manager()

	def __str__(self):  # return System by system name
		return self.name

	def get_owner(self):
		return self.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "User": self.User, "id": self.id}


class Transition_Rules(models.Model):
	name = models.CharField(max_length=500)
	description = models.CharField(max_length=100, blank=True, default='')
	System = models.ForeignKey(
		System, related_name='rules', on_delete=models.CASCADE)

	def __str__(self):  # return System by system name
		return self.name

	def get_owner(self):
		return self.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "System": self.System, "id": self.id}

class Component(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	System = models.ForeignKey(System, related_name='components', on_delete=models.CASCADE)

	def __str__(self):  # return System by system name
		return self.name

	def get_owner(self):
		return self.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "System": self.System, "id": self.id}


class Component_State(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	Component = models.ForeignKey(Component, related_name='states',on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_owner(self):
		return self.Component.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "Component": self.Component, "id": self.id}


class Component_Property(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	Component = models.ForeignKey(Component, related_name='properties',on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Component Properties"

	def __str__(self):
		return self.name

	def get_owner(self):
		return self.Component.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "Component": self.Component, "id": self.id}


class Environmental_Entity(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	System = models.ForeignKey(System, related_name='entities',on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Environmental Entities"

	def __str__(self):
		return self.name

	def get_owner(self):
		return self.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "System": self.System, "id": self.id}


class Environmental_State(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	Environmental_Entity = models.ForeignKey(
		Environmental_Entity, related_name='states',on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_owner(self):
		return self.Environmental_Entity.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "Environmental_Entity": self.Environmental_Entity, "id": self.id}


class Environmental_Property(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True, default='')
	Environmental_Entity = models.ForeignKey(
		Environmental_Entity, related_name='properties', on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Environmental Properties"

	def __str__(self):
		return self.name

	def get_owner(self):
		return self.Environmental_Entity.System.User

	def get_info(self):
		return {"name": self.name, "description": self.description, "Environmental_Entity": self.Environmental_Entity, "id": self.id}
