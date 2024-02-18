from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserSignupForm,UserLoginForm,UserProfileEditForm,UserPasswordchangeForm
from .models import MyBaseUser,Follow
from boards.forms import CreateBoardForm
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from boards.models import Board
from django.http import Http404


from django.contrib import messages


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            get_user = MyBaseUser.objects.filter(Q(username=data['username']) | Q(email = data['email']))
            print(get_user)
            if not get_user:
                user = MyBaseUser.objects.create_user(
                    username=data['username'],email=data['email'],password= data['password']
                )
                print('user created')
    form = UserSignupForm()
    return render(request,'register.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('photo:home')
    form = UserLoginForm()
    return render(request,'login.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("accounts:login")


@login_required
def profile(request,username):
    user = get_object_or_404(MyBaseUser, username=username)

    form = CreateBoardForm()
    boards = user.board_user.all()
    is_following = request.user.followers.filter(following = user).first() # agar ye user request.user ko follow kar raha hai toh
    content ={'user':user,'form':form,'boards':boards,'is_following': is_following}
    return render(request,'profile.html',content)


@login_required
def EditUserProfile(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST,request.FILES,instance = request.user.profile)
        if form.is_valid:
            form.save()
            redirect("accounts:profile",request.user)
    form = UserProfileEditForm(instance = request.user.profile)
    return render(request,'edit_profile.html',{'form':form})





@login_required
def follow(request,username):
    user = get_object_or_404(MyBaseUser,username = username)

    check_user = Follow.objects.filter(follower = request.user,following = user) # 'follow' karne wala and 'following' requet.user ko 

    if user == check_user:
        raise Http404
    if check_user.exists():
        raise Http404
    else:
        follow = Follow.objects.create(follower = request.user,following = user)
        follow.save()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def un_follow(request,username):   
    user = get_object_or_404(MyBaseUser,username = username)
    Follow.objects.filter(follower = request.user,following=user).delete()
    return redirect(request.META.get('HTTP_REFERER')) 




@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordchangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile',request.user)  # Redirect to user profile or any desired page
    else:
        form = UserPasswordchangeForm(request.user)
        messages.error(request, form.errors)
    return render(request, 'change_password.html', {'form': form})