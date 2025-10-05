import random

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sentence
from .serializers import SentenceSerializer


# Create your views here.
class SentenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

@api_view(['GET'])
def random_sentence(request):
    count = Sentence.objects.count()
    if count == 0:
        return Response({'error': 'No sentences found'}, status=status.HTTP_404_NOT_FOUND)

    random_index = random.randint(0, count - 1)
    sentence = Sentence.objects.all()[random_index]
    serializer = SentenceSerializer(sentence)
    return Response(serializer.data)