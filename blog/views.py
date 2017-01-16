from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from models import Blog
from django import forms


# Create your views here.
class RegisterForm(forms.Form):
	first_name=forms.CharField()
	last_name=forms.CharField()
	user_name=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

class NewBlog(forms.Form):
	title=forms.CharField()
	content=forms.CharField(widget=forms.Textarea)

def log_or_id(request):
	if request.user.is_authenticated():
		u=User.objects.get(username=request.user.get_username())
		try:
			b=Blog.objects.filter(user_name=u.username)
			return render(request,'user_feed.html',{'name':u.username,'blogs':b})
		except:
			return render(request,'user_feed.html',{'name':u.username})
	else:
		form=RegisterForm()
		return render(request,'sign_or_reg.html',{'form':form})
	
def reg_and_log(request):
	u=User(username=request.POST['user_name'],email=(request.POST['user_name']+'.com'),password=request.POST['password'])
	u.save()
	login(request,u)
	return render(request,'user_feed.html',{'name':u.username})

def new_blog(request):
	b=NewBlog()
	return render(request,'new_blog.html',{'form':b})
	
def save_blog(request):
	v_title=request.POST['title']
	v_content=request.POST['content']
	print title,content
	blog=Blog(user_name=request.user.get_username(),title=v_title,content=v_content)
	blog.save()
	return redirect('log_or_id')
