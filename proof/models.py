from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import models as auth_models

# Create your models here.

class Article(models.Model):
    url = models.URLField(max_length=256,null=True,blank=True,verbose_name=_("URL"),help_text=_("Original URL of the article if present"))
    published = models.DateTimeField(null=True,blank=True,verbose_name=_("Published"),help_text=_("Original publication date/time of the article if present"))
    title = models.CharField(max_length=128,db_index=True,verbose_name=_("Title"),help_text=_("Title of the article"))
    copyright = models.CharField(max_length=64,db_index=True,null=True,blank=True,verbose_name=_("Copyright"),help_text=_("Copyright meta info of the article"))
    keywords = models.TextField(null=True,blank=True,verbose_name=_("Keywords"),help_text=_("Keywords meta info of the article"))
    description = models.TextField(null=True,blank=True,verbose_name=_("Description"),help_text=_("Description meta info of the article"))
    content = models.TextField(null=True,blank=True,verbose_name=_("Content"),help_text=_("Article content"))
    created_by = models.ForeignKey(auth_models.User,verbose_name=_("Created By"),help_text=_("User who has created this article"),related_name="articles")
    created = models.DateTimeField(auto_now_add=True,verbose_name=_("Created"),help_text=_("Date/Time when the article has been created"))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

class Hyperlink(models.Model):
    article = models.ForeignKey(Article,verbose_name=_("Article"),help_text=_("Article to which the hyperlink concerns"))
    url = models.URLField(max_length=256,verbose_name=_("URL"),help_text=_("URL of the link"))
    created_by = models.ForeignKey(auth_models.User,verbose_name=_("Created By"),help_text=_("User who has created this hyperlink"),related_name="hyperlinks")
    created = models.DateTimeField(auto_now_add=True,verbose_name=_("Created"),help_text=_("Date/Time when the URL has been created"))
    kind = models.CharField(max_length=10,choices=(
        ('proof',_("Proof")),
        ('denial',_("Denial")),
        ('details',_("Details")),
    ),verbose_name=_("Kind"),help_text=_("Semantic kind of the hyperlink"))
    title = models.CharField(max_length=128,null=True,blank=True,verbose_name=_("Title"),help_text=_("Title of the article directed by hyperlink"))
    priority = models.IntegerField(null=True,blank=True,verbose_name=_("Priority"),help_text=_("Priority of the hyperlink (TBD)"))
    offset = models.IntegerField(verbose_name=_("Offset"),help_text=_("Offset from the start of the article content"))
    length = models.IntegerField(verbose_name=_("Length"),help_text=_("Length of the content included into hyperlink"))
    moderator = models.ForeignKey(auth_models.User,null=True,blank=True,verbose_name=_("Moderator"),help_text=_("Moderator of the hyperlink who has approved it"),related_name="moderated_hyperlinks")
    is_approved = models.BooleanField(default=False,verbose_name=_("Is Approved"),help_text=_("Whether the hyperlink has been approved by the moderator"))

    class Meta:
        verbose_name = _("Hyperlink")
        verbose_name_plural = _("Hyperlinks")
