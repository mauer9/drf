from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python")
    style = models.CharField(choices=STYLE_CHOICES, default="friendly")
    linenos = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
