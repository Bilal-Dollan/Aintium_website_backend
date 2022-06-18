from rest_framework import generics, mixins, permissions
from .models import *
from .serializers import *
from .permissions import IsOwner


def index(request):
    return None


class GetUser(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        return self.retrieve(request, pk)


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


class GetAiMode(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = AiModel.objects.all()
    serializer_class = AiModelSerializer
    lookup_field = 'pk'
    
    def get(self, request, pk):
        return self.retrieve(request, pk)


class UserEdit(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def post(self, request, pk):
        return self.partial_update(request, pk)
