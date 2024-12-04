from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programer

# Create your views here.


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programer.objects.all()
    serializer_class = ProgrammerSerializer