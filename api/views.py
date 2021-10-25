from rest_framework import generics

from subeer.models import Episode
from .serializers import EpisodeSerializer
'''Тут мы определим классы Эпизод Лист и Эпизод Дитейл, для первого будет Лист креате, для второго РетриевАпдейт'''


class EpisodeList(generics.ListCreateAPIView):
	queryset = Episode.objects.all()
	serializer_class = EpisodeSerializer
	name = 'episode-list'


class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Episode.objects.all()
	serializer_class = EpisodeSerializer
	name = 'episode-list'
