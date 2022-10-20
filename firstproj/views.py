""" 
	To render html web pages
"""
import random
from re import A
from django.http import HttpResponse

from django.template.loader import render_to_string
from articles.models import Article

def home_view(request):

	"""
	Take in a request & return Html as a response 
	"""
	name = "Abhi"
	random_id = random.randint(1,4)

	# from the database?
	article_obj = Article.objects.get(id=random_id)
	#my_list = [101, 102, 103, 104, 105]
	article_queryset = Article.objects.all()

	context = {
		#"my_list": my_list,
		"object_list": article_queryset,
		"object": article_obj,
		"title": article_obj.title,
		"id": article_obj.id,
		"content": article_obj.content,
	}
	#Django Templates

	#1 way to call templates
	# tmpl = get_template("home-view.html")
	# tmpl_string = tmpl.render(context=context)
	
	HTML_STRING = render_to_string('home-view.html', context=context)

	# HTML_STRING = """ 
	# 	<h1>{title} (id:{id}!)</h1>
	# 	<p>{content}</p>
	# """.format(**context)
	
	return HttpResponse(HTML_STRING)