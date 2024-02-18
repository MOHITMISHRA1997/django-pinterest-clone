from django.shortcuts import render,redirect
from .forms import Create_Pin_form,Save_to_board
from .models import Pin
from boards.models import Board
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_pin(request):
    if request.method == 'POST':
        form = Create_Pin_form(request.user,request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            board = Board.objects.get(title = data['board']) # get the board
            board.pins.add(instance) # add pin inside the board
        return redirect("boards:board_detail", board.title)
    form = Create_Pin_form(request.user)
    return render(request,'create_pin.html',{'form':form})

@login_required
def pin_detail(request,id):
    pin = Pin.objects.get(id=id)
    pin_detail = request.user.pin_user.filter(id = id).first() #check that this pin is created by request.user
    saved_in_board = Save_to_board(request.user,instance = pin_detail)
    is_following = request.user.followers.filter(following = pin.user).first()
    content = {
        'pin':pin,
        "pin_detail":pin_detail,
        "saved_in_board":saved_in_board,
        "is_following":is_following
    }
    return render(request,'pin_detail.html',content)

