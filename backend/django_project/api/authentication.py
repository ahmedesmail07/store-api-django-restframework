from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"


# Just in one line in your command line : python manage.py drf_create_token username
# Remember replace the username in the above with the ur username
# OPEN Shell Then do the following to create your token manually
"""
python manage.py shell 
then do the following
>>> from django.contrib.auth.models import User
>>> from rest_framework.authtoken.models import Token
>>> user = User.objects.get(username='ahmed2')   
>>> token = Token.objects.create(user=user)
>>> print(token.key)
2f90ad9bf5edd84f4a120761f2dc03bda50cc054
"""
