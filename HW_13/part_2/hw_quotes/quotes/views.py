from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Author, Quote, Tag
from .utils import get_mongodb
from .forms import QuoteForm, AuthorForm, TagForm

raw_sql_query_top_tags = """
SELECT quotes_tag.id as id, quotes_tag.name
FROM quotes_quote_tags
join quotes_tag on quotes_tag.id = quotes_quote_tags.tag_id 
group by quotes_tag.name, quotes_tag.id
order by count(quotes_quote_tags.tag_id) desc, quotes_tag.name
limit 10
"""

top_tags = Tag.objects.raw(raw_sql_query_top_tags)


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_about(request, _id):
    print(_id)
    author = Author.objects.get(pk=_id)
    print(author.fullname, type(author))

    return render(request, 'quotes/author.html', context={'author': author})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_quote.html", context={'form': QuoteForm(), "message": "Form not valid"})
    return render(request, "quotes/add_quote.html", context={'form': QuoteForm()})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_author.html",
                          context={'form': AuthorForm(), "message": "Form not valid"})
    return render(request, "quotes/add_author.html", context={'form': AuthorForm()})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_tag.html", context={'form': TagForm(), "message": "Form not valid"})
    return render(request, "quotes/add_tag.html", context={'form': TagForm()})


def find_by_tag(request, _id):
    per_page = 5
    quotes = Quote.objects.filter(tags=_id).all()
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Tag.objects.raw(raw_sql_query_top_tags)
    for tag in top_tags:
        print(tag.id, tag.name)

    return render(request, "quotes/index.html", context={'quotes': page_obj, 'top_tags': top_tags})
