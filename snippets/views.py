from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework import decorators, response, relations, generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


@decorators.api_view(["GET"])
def api_root(request, format=None):
    return response.Response(
        {
            "users": relations.reverse("user-list", request=request, format=format),
            "snippets": relations.reverse(
                "snippet-list", request=request, format=format
            ),
        }
    )


class SnippetList(generics.ListCreateAPIView):
    """get all snippets list or create a snippet"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """get, modify, delete snippet by id"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    """get all users list"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """get user by id"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
