from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, blank=True, default="")
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python")
    style = models.CharField(choices=STYLE_CHOICES, default="friendly")
    linenos = models.BooleanField(default=False)
    code = models.TextField()
    highlighted = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        use 'pygments' library
        to add highlighted html representation of the code
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}

        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )

        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner}:{self.pk}:{self.code}"

    class Meta:
        ordering = ["created"]
