# -*- coding: utf-8 -*-
from collections import OrderedDict
from djangocms_social.models.base import RenderObject


AVAILABLE = OrderedDict((
    ('facebook', 'FacebookLike'),
    ('google', 'GooglePlusOne'),
    ('twitter', 'TwitterTweet',),
    ('pinterest', 'PinterestPin'),
    ('email', 'SendEmail'),
))


class FacebookLike(RenderObject):
    template = 'djangocms_social/plugins/likes/facebook.html'


class GooglePlusOne(RenderObject):
    template = 'djangocms_social/plugins/likes/google.html'


class TwitterTweet(RenderObject):
    template = 'djangocms_social/plugins/likes/twitter.html'


class PinterestPin(RenderObject):
    template = 'djangocms_social/plugins/likes/pinterest.html'


class SendEmail(RenderObject):
    template = 'djangocms_social/plugins/likes/email.html'
