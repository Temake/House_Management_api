from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets,mixins
from .permissions import IsUserOwnerOrGetandPostOnly,IsProfileOwnerOrGetOnly
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

class UserViewsets(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetandPostOnly]
class ProfileViewsets(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    queryset= Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes= [IsProfileOwnerOrGetOnly]