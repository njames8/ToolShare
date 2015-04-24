"""
file: views.py
language: python3
authors: Andrew Carpenter, Nick James, Ryan Lachacz
description: The view-controller of the MVC design pattern. Determines what
             is shown to the user and translates input from the user to be
			 interpreted my the model.
"""

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import views
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def RegisterView(request):
	"""
	Class: Registerview
	Description: renders the registration page and takes user input
	Arguments: view to render
	Postconditions: user's information is registered to the database
	"""	
	form = RegisterForm()
	if request.POST:
		form = RegisterForm(request.POST) 
		if form.is_valid():
			user = form.save()
			user.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend'

			return HttpResponseRedirect('/')

	return render(request, "register.html", {'form':form})


def UserLogout(request):
	return views.logout_then_login(request, login_url = '/')
	
@login_required(login_url='/')
def home(request):
    """
    Function: home
    Description: renders the homepage
    Arguments: user request
    Postconditions: User is directed to homepage
    """	
    profile = get_object_or_404(UserProfile, pk=request.user.id)
    sheds = []
    numOfSheds = None
    numTools = 0
    numOfUsers = 0
    if len(Shed.objects.filter(location=profile.location)) > 0:
        sheds = Shed.objects.filter(location=profile.location)
        numOfSheds = len(Shed.objects.filter(location=profile.location))
        
        numOfUsers = len(UserProfile.objects.filter(location=profile.location))
        for x in sheds:
            numTools += x.getNumOfTools()
    
    context = {
        'sheds'      :sheds,
        'numOfSheds' :numOfSheds,
        'numTools'   :numTools,
        'numOfUsers' :numOfUsers,
    }
    return render(request,'home.html', context)

@login_required(login_url='/')
def mytools(request):
	"""
	Function: mytools
	Description: renders the mytools page
	Arguments: user request
	Postconditions: User is directed to the mytools page
	"""	
	current_user =request.user
	profile = get_object_or_404(User, pk=current_user.id)
	ownedTools = Tool.objects.filter(owner=profile.id
        ).order_by('-name')
	borrowedTools = Tool.objects.filter(borrower=profile.id).order_by('-name')
	form = ToolCreateForm()
	#messages.info(request, 'Tools n shit', extra_tags='safe')

	if request.POST:
		form = ToolCreateForm(request.POST)
		if form.is_valid():
			tool = form.save(commit=False)
			tool.owner = request.user
			tool.save()
	form = ToolCreateForm()
	context = {
		'ownedTools'	:ownedTools,
		'borrowedTools'	:borrowedTools,
		'form'			:form
	}
	return render(request, 'mytools.html', context)

@login_required(login_url='/')
def mysheds(request):
	"""
	Function: mysheds
	Description: renders the mysheds page
	Arguments: user request
	Postconditions: User is directed to mysheds page
	"""	
	current_user = request.user
	profile = get_object_or_404(UserProfile, pk=current_user.id)
	shed = None
	if profile.shed is not None:
		shed = get_object_or_404(Shed, pk=profile.shed.id)
	sheds = Shed.objects.filter(location=profile.location)
	tools = Tool.objects.filter(shed=shed, inShed=True, availability=True).order_by('-name')
	coordinatedSheds = Shed.objects.filter(coordinator=profile)
	form = ShedCreateForm()
	if request.POST:
		form = ShedCreateForm(request.POST)
		if form.is_valid():
			shed = form.save(commit=False)
			shed.coordinator = request.user
			shed.save()
	context = {
		'request'	:request,
		'shed' 		:shed,
		'tools'		:tools,
		'sheds'		:sheds,
		'form'		:form,
		'coordSheds':coordinatedSheds,
		'profile'   :profile,
	}

	return render(request, 'mysheds.html', context)

@login_required(login_url='/')
def myprofile(request):
	"""
	Function: myprofile
	Description: renders the myprofile page
	Arguments: user request
	Postconditions: User is directed to myProfile page
	"""	
	current_user = request.user
	profile = get_object_or_404(UserProfile, pk=current_user.id)
	form = EditProfileForm(instance=profile)
	if request.POST:
		form = EditProfileForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			profile.first_name = user.first_name
			profile.last_name = user.last_name
			profile.email = user.email
			profile.location= user.location
			profile.save()
			return HttpResponseRedirect('../myprofile')
	

	return render(request, 'myprofile.html', {'form':form})


def about(request):
	"""
	Function: about
	Description: renders the about page
	Arguments: user request
	Postconditions: User is directed to about page
	"""	
	return render_to_response('about.html')

	
def contact(request):
	"""
	Function: contact
	Description: renders the contact page
	Arguments: user request
	Postconditions: User is directed to contact page
	"""	
	return render_to_response('contact.html')
	
@login_required(login_url='/')
def toolCreate(request):
	form = ToolCreateForm()
	print(request.POST)
	if request.POST:
		form = ToolCreateForm(request.POST)
		if form.is_valid():
			tool = form.save(commit=False)
			tool.name=tool.name.capitalize()
			tool.owner = request.user
			tool.save()
	return HttpResponseRedirect('../mytools')

@login_required(login_url='/')
def shedCreate(request):
	"""
	creates a shed
	"""
	form = ShedCreateForm()
	if request.POST:
		form = ShedCreateForm(request.POST)
		if form.is_valid():
			print(form)
			shed = form.save(commit=False)
			shed.name = shed.name.capitalize()
			shed.coordinator = request.user
			shed.save()
			return HttpResponseRedirect('../mysheds')
	return render(request, 'createTemplate.html', {'form':form})
	
def changePassword(request):
	"""
	presents form to change user's password
	"""
	form = PasswordChangeForm(request.user)
	if request.POST:
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('../home')
	return render(request, 'changePassword.html', {'form':form})
	
def requestTool(request, tool_id):
	"""
	Borrows tool
	"""
	tool = get_object_or_404(Tool, pk=tool_id)
	print(tool)
	tool.availability = False
	tool.borrower = request.user
	tool.save()
	print(tool.borrower)
	return HttpResponseRedirect('/mysheds')

def returnTool(request, tool_id):
	"""
	returns a tool to the shed
	"""
	tool = get_object_or_404(Tool, pk=tool_id)
	tool.availability=True
	tool.borrower = None
	tool.save()
	return HttpResponseRedirect('/mytools')
    
def deleteTool(request, tool_id):
	"""
	delets a tool from the db
	"""
	Tool.objects.filter(pk=tool_id).delete()
	return HttpResponseRedirect('/mytools')

def changeShed(request, shed_id):
	"""
	changes the shed the user is a part of
	"""
	shed = get_object_or_404(Shed, pk=shed_id)
	profile = get_object_or_404(UserProfile, pk=request.user.id)
	profile.shed = shed
	profile.save()
	return HttpResponseRedirect('/mysheds')

def editTool(request, tool_id):
    """
    enables user to edit tools
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    form = ToolCreateForm(instance=tool)
    if request.POST:
        form = ToolCreateForm(request.POST)
        updatedTool=form.save(commit=False)
        print(updatedTool.toolCondition)
        tool.name = updatedTool.name.capitalize()
        tool.toolCondition = updatedTool.toolCondition
        tool.description = updatedTool.description
        tool.availability = updatedTool.availability
        tool.inShed = updatedTool.inShed
        tool.shed = updatedTool.shed
        tool.save()
        return HttpResponseRedirect("/mytools")
    return render(request,'createTemplate.html', {'form':form})

def deleteShed(request, shed_id):
	"""
	deletes shed
	"""
	Shed.objects.filter(pk=shed_id).delete()
	return HttpResponseRedirect('/mysheds')

def searchSheds(request):
	"""
	Searched all sheds by zipcode
	"""
	query = request.GET.get('q')
	if query:
		# There was a query entered.
		results = Shed.objects.filter(location=query)
	else:
	 	# If no query was entered, simply return all objects
		results = Shed.objects.all()
	context = {
		'results': results,
		'query'  : query,
	}
	return render(request, 'search_result.html', context)

def searchTools(request):
	"""
	Searches all tools by name. Case specific.
	"""
	query = request.GET.get('q')
	if query:
		# There was a query entered.
		results = Tool.objects.filter(name=query)
	else:
	 	# If no query was entered, simply return all objects
		results = Tool.objects.all()
	profile = get_object_or_404(UserProfile, pk=request.user.id)
	context = {
		'results': results,
		'query'  : query,
		'profile': profile,
	}
	return render(request, 'toolSearch.html', context)
    
def terms(request):
    return render(request, 'Terms.html',{})