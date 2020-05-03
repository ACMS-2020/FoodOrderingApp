from django.shortcuts import render,redirect

def homeView(request):
	context={}
	return render(request,'home.html',context)