# from django import template
# from django.contrib.auth.models import Group

# register = template.Library()

# @register.filter(name='has_group')
# def has_group(user, group_name):
#     # import pdb;pdb.set_trace()
#     group = Group.objects.get(name=group_name)
#     print(group)
#     # import pdb;pdb.set_trace()

#     if group_name == 'Admins':
#         print("True")
#         return True
#     else:
#         print("False")
#         return False
#     # return True if group in user.group.all() else False

# register.filter('has_group', has_group)