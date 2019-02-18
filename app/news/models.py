from wagtail.core.models import Page

from core.mixins import ImagesMixin, ArticleMixin, MenuMixin


class NewsModel(MenuMixin, ImagesMixin, ArticleMixin, Page):

    content_panels = (
        Page.content_panels + ArticleMixin.content_panels + ImagesMixin.content_panels
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels
