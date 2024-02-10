from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, max_length=100, allow_blank=True)
    code = serializers.CharField(style={"base_template": "textarea.html"})
    language = serializers.CharField(choices=LANGUAGE_CHOICES, default="python")
    style = serializers.CharField(choices=STYLE_CHOICES, default="friendly")
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        Snippet.objects.create(**validated_data)
