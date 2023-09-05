from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from app.models import *
from django.views.generic import ListView
from app.forms import *
from django.core.mail import send_mail
from taggit.models import Tag
# cbv
class List_view(ListView):
	model = Post
	paginate_by = 2


# fbv
def list_view(request, tag_slug = None):
	post_list = Post.objects.all()

	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug = tag_slug)
		post_list = post_list.filter(tags__in = [tag])

	page_nk = Paginator(post_list, 2)
	page_no = request.GET.get('page')
	try:
		post_list = page_nk.page(page_no)
	except PageNotAnInteger:
		post_list = page_nk.page(1)
	except EmptyPage:
		post_list = page_nk.page(page_nk.num_pages)

	dict = {"post_list" : post_list, "tag" : tag}
	return render(request = request, template_name = "app/post_list.html", context = dict)


def detail_view(request, year, month, day, slug):
	post = get_object_or_404(Post, slug = slug, status = "published", publish__year = year, publish__month = month, publish__day = day)

	comment = post.cmt.filter(active = True)
	csubmit = False
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit = False)
			new_comment.post = post
			new_comment.save()
			csubmit = True
	else:
		form = CommentForm()

	# page_nk = Paginator(comment, 2)
	# page_no = request.GET.get('page')
	# try:
	# 	comment = page_nk.page(page_no)
	# except PageNotAnInteger:
	# 	comment = page_nk.page(1)
	# except EmptyPage:
	# 	comment = page_nk.page(page_nk.num_pages)

	dict = {"post" : post, "form": form, "comment" : comment, "csubmit" : csubmit}
	return render(request = request, template_name = "app/post_detail.html", context = dict)

def share_mail(request, id):
	post = get_object_or_404(Post, id = id, status = "published")
	sent = False
	if request.method == "POST":
		form = mail(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject = '{}({}) recommends you to read "{}"'.format(cd["name"], cd["mail"], post.title)
			post_url = request.build_absolute_uri(post.get_absolute_url())
			msg = "read the post at :\n{}\n\n{}\'s comments:\n {}".format(post_url,cd["name"], cd["comment"])

			# syntax : send_mail("subject", "msg", "from -> can be anything because it will take from settings.py",["to"])
			# ex : send_mail("blog", "hi da , hw r u", "nkisnithinkumar@gmail.com", [cd["to"]])

			send_mail(subject, msg,"nkisnithinkumar@gmail.com",[cd["to"]])
			sent = True

	else:

		form = mail()

	dict = {"post" : post, "form" : form, "sent": sent} 
	return render(request = request, template_name = "app/share_mail.html", context = dict)
