from GViews.serializers import SampleUser, SampleUserSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny


class UserList(generics.ListAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserRetrieve(generics.RetrieveAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserCreate(generics.CreateAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserUpdate(generics.UpdateAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserDestroy(generics.DestroyAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserListCreate(generics.ListCreateAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]


class UserReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SampleUser.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [AllowAny]
