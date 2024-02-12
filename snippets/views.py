from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """get all snippets list or create a snippet"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """get, modify, delete snippet by id"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
