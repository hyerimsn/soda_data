from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Log, News

# Create your views here.\\
def home(request):
    return render(request, 'home.html', context)

def log(request):
    logs = Log.objects.all()
    news = News.objects.all()
    q= request.GET.get('q', '')
    n= request.GET.get('n', '')
    d= request.GET.get('d', '')
    if q:
        logs = logs.filter(ment__icontains = q, person__icontains = n)
        news = news.filter(body__icontains = q, date__icontains = d)
    context = {'logs' : logs, 'news': news, 'q' : q}
    return render(request, 'home.html', context)

def detail(request, log_id):
    log_one = get_object_or_404(Log, id=log_id)
    log_before = get_object_or_404(Log, id=log_id-1)
    log_after = get_object_or_404(Log, id=log_id+1)

    return render(request, 'detail.html', {'log_one': log_one, 'log_before': log_before, 'log_after':log_after})