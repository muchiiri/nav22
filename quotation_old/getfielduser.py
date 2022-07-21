from django.core import serializers
from accounts.models import *

def not_in_oglclients_group(user):
	if user.groups.filter(name='Ogl Clients').exists():
		return True
	else:
		return False

fielduser_queryset = Account.objects.all()

# serialize queryset
serialized_queryset = serializers.serialize('json', fielduser_queryset)
# import pdb;pdb.set_trace()