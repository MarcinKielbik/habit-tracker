from rest_framework.generics import ListAPIView
from .models import Habit
from .serializers import HabitSerializer


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
