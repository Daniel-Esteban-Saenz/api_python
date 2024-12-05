from rest_framework import viewsets
from .serializer import ProgrammerSerializer, StudentSerializer
from .models import programer, student

# Create your views here.


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programer.objects.all()
    serializer_class = ProgrammerSerializer
    


class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer