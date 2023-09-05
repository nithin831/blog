from app.models import *
from django import template
from django.db.models import Count

register  = template.Library()

@register.simple_tag()
def count():
	return Post.objects.count()

@register.inclusion_tag("app/latest_blog.html")
def latest_blog():
	latest_blog = Post.objects.order_by("-publish")[:3]
	return {"latest_blog" : latest_blog}

@register.simple_tag()
def more_cmt(count = 3):
	return Post.objects.annotate(total_count = Count("cmt")).order_by("-total_count")[:count]