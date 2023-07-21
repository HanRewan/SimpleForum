from django.shortcuts import render, get_object_or_404
from .models import Board


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    print(board.name)
    return render(request, 'topic.html', {'board': board})
