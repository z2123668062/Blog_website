from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
# 用户退出
def user_logout(request):
    logout(request)
    return redirect("article:article_list")
# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 从表单获取原始密码
            raw_password = user_register_form.cleaned_data['password']
            # 设置密码并保存用户
            new_user.set_password(raw_password)
            new_user.save()

            # 使用 authenticate 获取带 backend 的用户实例再登录
            user = authenticate(request, username=new_user.username, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                # 作为后备（不推荐长期使用），显式指定后端然后登录
                new_user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, new_user)

            return redirect("article:article_list")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
# 删除用户
@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        # 验证登录用户、待删除用户是否相同
        if request.user == user:
            #退出登录，删除数据并返回博客列表
            logout(request)
            user.delete()
            return redirect("article:article_list")
        else:
            return HttpResponse("你没有删除操作的权限。")
    else:
        return HttpResponse("仅接受post请求。")

@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    print("当前请求方法：", request.method)  
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=id)

    if request.method == 'POST':
        print("是否有文件提交：", request.FILES)  # 会显示上传的文件信息
        print("表单字段：", request.POST.keys())  # 显示提交的文本字段
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")
        
        # 关键修改：同时传入 request.POST 和 request.FILES
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
            return redirect("userprofile:edit", id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = { 'profile_form': profile_form, 'profile': profile, 'user': user }
        return render(request, 'userprofile/edit.html', context)
