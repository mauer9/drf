from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "id",
            "url",
            "owner",
            "title",
            "language",
            "style",
            "linenos",
            "code",
            "highlight",
            "created",
        ]


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "snippets",
        ]
