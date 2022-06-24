from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *


def index(request):
    return None


class GetUserPk(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        return self.retrieve(request, pk)


class GetUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)


class UserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

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
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookmarkList(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(user_id=user)


class TagList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetTag(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'pk'
    
    def get(self, request, pk):
        return self.retrieve(request, pk)


class GetAiModel(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = AiModel.objects.all()
    serializer_class = AiModelSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        return self.retrieve(request, pk)


# TODO
class UserEdit(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def post(self, request, pk):
        return self.update(request, pk)


# TODO
class UserEditPassword:
    pass


class ImageList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RateList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)