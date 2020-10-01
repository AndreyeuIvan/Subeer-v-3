from django.shortcuts import render
from .forms import NameForm
from .models import Serial, Episode, Opinion
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
'''I will represent 1.List of Serials, 2.New serials, 3. Popular Serials, 4.Detail of serial 5. New serial and episodes'''


class SerialList(ListView):
	model = Serial
	context_object_name = 'serials'
	paginate_by = 3


class EpisodeDetail(DetailView):
	pass


def detail_episode(request, slug):
	serial = Serial.objects.get(slug=slug)
	episodes = Episode.objects.filter(serial_id=serial.id)
	return render(request, 'subeer/detail_episode.html', {'serial':serial, 'episodes':episodes})


def search(request):
	query = request.GET.get('q')
	if query:
		serials = Serial.objects.filter(
			Q(title__icontains=query)) 
		try:
			return detail_episode(request, slug=serials.values()[0].get('slug'))
		except:
			return render(request, 'subeer/serial_list.html', {'serials':Serial.objects.all()}) #or HttpResponse('<h1>There is no such serial, only following</h1>')


def popular(request):
	'''Func will present popular Serials, according to rating, than likes'''
	serial = Serial.objects.order_by('-is_favorite')
	return render(request, 'subeer/popular.html', {'serials' : serial})


def new_serials(request):
	'''Present new Serials, according to the date'''
	serial = Serial.objects.order_by('-updated')
	return render(request, 'subeer/serial_list.html', {'serials' : serial})


def new_episodes(request):
	'''Present new Episodes, according to date'''
	episodes = Episode.objects.order_by('-updated')
	return render(request, 'subeer/episode_new.html', {'episodes' : episodes})


def get_opinion(request):
	form = NameForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'subeer/episode_new.html')
		else:
			form = NameForm()
	return render(request, 'subeer/form.html', {'form': form})

'''def like(request):
    if request.method == 'GET':
        serial_id = request.GET['serial_id']
        likedserial = Serial.objects.get(id = serial_id )
        m = Like(serial=likedserial)
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")'''

class OpinionList(ListView):
	model = Opinion
	context_object_name = 'opinions'
