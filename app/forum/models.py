from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from core.mixins import AttachmentsMixin, MenuMixin


class ForumModel(MenuMixin, Page):

    text = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("text")]

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"


class ThreadModel(MenuMixin, AttachmentsMixin, Page):

    text = RichTextField()

    content_panels = (
        Page.content_panels + AttachmentsMixin.content_panels + [FieldPanel("text")]
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"


class MessageModel(MenuMixin, AttachmentsMixin, Page):

    text = RichTextField()

    content_panels = (
        Page.content_panels + AttachmentsMixin.content_panels + [FieldPanel("text")]
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
