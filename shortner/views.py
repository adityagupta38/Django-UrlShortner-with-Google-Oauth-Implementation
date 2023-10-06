import uuid
import datetime
from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Urls
# Create your views here.


def profile(request):
    form = UrlForm()
    if request.method == 'POST':
        link = request.POST['link']
        shorturl = str(uuid.uuid4())[:5]
        url = Urls(link= link, uuid=shorturl)
        url.save()
        url_list = Urls.objects.all()
        return render(request, 'profile.html', {'form': form, 'urls_list': url_list})
    url_list = Urls.objects.all()
    return render(request, 'profile.html', {'form': form, 'urls_list': url_list})


def go(request, pk):
    url = Urls.objects.get(uuid=pk)
    url.click_count = url.click_count + 1
    url.last_clicked = datetime.datetime.now()
    url.save()
    return redirect(url.link)


def delete_url(request, pk):
    url = Urls.objects.get(uuid=pk)
    url.delete()
    return redirect('/')




