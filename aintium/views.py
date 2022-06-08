from rest_framework import generics, mixins, permissions, authentication
from .models import *
from .serializers import *
from .mixins import IsStaffEditorPermissionMixin, IsOwnerPermissionMixin
from .permissions import IsOwner


def index(request):
    return None


class UserList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AiModelList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = AiModel.objects.all()
    serializer_class = AiModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RequestList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookmarkList(permissions.BasePermission, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsOwner]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TagList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
