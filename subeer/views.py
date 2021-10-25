from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import NameForm
from .models import Serial, Episode, Opinion
from action.utils import create_action

from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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
	#file = 
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


@login_required
@require_POST
def serial_like(request):
	"""Здесь мы используем два декоратора для функции. Декоратор login_required
    не даст неавторизованным пользователям доступ к этому обработчику. Деко-
    ратор require_POST возвращает ошибку HttpResponseNotAllowed (статус ответа 405),
    если запрос отправлен не методом POST. Таким образом, обработчик будет вы-
    полняться только при POST-запросах. В Django также реализованы декоратор
    required_GET, запрещающий любые методы, кроме GET, и декоратор require_http_
    methods, принимающий список разрешенных методов в качестве аргумента.
    В этом обработчике мы используем два POST-параметра:
      image_id – ID изображения, для которого выполняется действие;
      action – действие, которое хочет выполнить пользователь (строковое
    значение like или unlike).
    Мы используем менеджер отношения «многие ко многим» users_like моде-
    ли Image, чтобы добавлять и удалять пользователей с помощью методов add()
    и remove() соответственно. Если вы вызываете add() и передаете в него поль-
    зователя, который уже связан с текущей картинкой, дубликат не будет создан.
    Аналогично при вызове remove() и попытке удалить пользователя, который не
    связан с изображением, ошибка не появится. Еще один полезный метод ме-
    неджера «многие ко многим» – clear(). Он удаляет все отношения.
    В конце обработчика используем объект JsonResponse, который возвращает
    HTTP-ответ с типом application/json и преобразует объекты в JSON."""
	serial_id = request.POST.get('id')
	action = request.POST.get('action')
	if serial_id and action:
		try :
			serial = Serial.objects.get(id=serial_id)
			if action == 'like':
				serial.users_like.add(request.user)
				create_action(request.user, 'likes', serial)
			else:
				serial.users_like.remove(request.user)
			return JsonResponse({'status':'ok'})
		except:
			pass
	return JsonResponse({'status':'ok'})


class OpinionList(ListView):
	model = Opinion
	context_object_name = 'opinions'
