from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateBoardForm,EditBoardForm
from .models import Board
from pins.models import Pin
from django.contrib.auth.decorators import login_required
from pins.forms import Save_to_board

# Create your views here.


@login_required
def create_board(request):
    if request.method == 'POST':
        form = CreateBoardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            instance = form.save(commit=False)
            instance.user = request.user
            # to checks if there is any board associated with the user that has the same title.
            check_name = request.user.board_user.filter(title = data['title']).first()
            print(check_name)
            if not check_name:
                print("working fine")
                instance.save()
            return redirect("accounts:profile",request.user)

    return redirect("accounts:profile",request.user)


@login_required
def edit_board(request,board_name,id):
    board = request.user.board_user.get(title=board_name,id=id)
    print(board)
    if request.method == 'POST':
        form = EditBoardForm(request.POST,request.FILES,instance = board )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("accounts:profile",request.user)
    form = EditBoardForm(instance = board )
    return render(request,'edit_board.html',{'form':form,'board':board})



@login_required
def board_detail(request,board_title):
    board = get_object_or_404(Board, title=board_title)
    pins = board.pins.all()
    print(pins)
    return render(request,'board_detail.html',{'board':board,'pins':pins})





@login_required
def save_to_board(request,title):
    pin = Pin.objects.filter(title = title).first()
    pin_detail = request.user.pin_user.filter(title=title).first()
    if request.method == 'POST':
        form = Save_to_board(request.user,request.POST,instance = pin_detail)
        if form.is_valid():
            data = form.cleaned_data
            instnance = form.save(commit = False)
            instnance.user = pin.user
            instnance.title = pin.title
            print('the title is',pin.title)
            instnance.save()
            board = Board.objects.filter(title=data['board']).first()
            board.pins.add(pin)
    return redirect("pins:pin_detail", pin.id)




@login_required
def remove_from_board(request,title,board):
    pin = Pin.objects.filter(title=title).first()
    user_board = request.user.board_user.filter(title=board).first()
    if user_board:
        user_board.pins.remove(pin)     


    return redirect(request.META.get('HTTP_REFERER'))

