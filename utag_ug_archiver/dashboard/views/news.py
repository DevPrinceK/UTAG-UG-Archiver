from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponseRedirect



from dashboard.models import News

from utag_ug_archiver.utils.decorators import MustLogin

class NewsView(View):
    template_name = 'dashboard_pages/news.html'
    @method_decorator(MustLogin)
    def get(self, request):
        #Get all news
        news = News.objects.all()
        context = {
            'newss' : news
        }
        return render(request, self.template_name, context)
    
class NewsCreateView(View):
    @method_decorator(MustLogin)
    def get(self, request):
        return render(request, self.template_name)
    
    @method_decorator(MustLogin)
    def post(self, request):
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        print(is_published)
        featured_image = request.FILES.get('featured_image')
        if is_published == 'on':
            is_published = True
        else:
            is_published = False
        news = News.objects.create(
            author = user,
            title = title,
            content = content,
            is_published = is_published,
            featured_image = featured_image
        )
        news.save()
        messages.info(request, "News Created Successfully")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
class NewsUpdateView(View):
    @method_decorator(MustLogin)
    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        context = {
            'news' : news
        }
        return render(request, self.template_name, context)
    
    @method_decorator(MustLogin)
    def post(self, request, pk):
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        featured_image = request.FILES.get('featured_image')
        if is_published == 'on':
            is_published = True
        else:
            is_published = False
        news = News.objects.get(pk=pk)
        news.author = user
        news.title = title
        news.content = content
        news.is_published = is_published
        if featured_image:
            news.featured_image = featured_image
        news.save()
        messages.info(request, "News Updated Successfully")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
class NewsDeleteView(View):
    @method_decorator(MustLogin)
    def get(self, request, *args, **kwargs):
        news_id = kwargs.get('news_id')
        news = News.objects.get(pk=news_id)
        news.delete()
        messages.info(request, "News Deleted Successfully")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))