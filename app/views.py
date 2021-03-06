from auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token, get_token
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from dateutil import tz, parser
from graph_helper import *

def getnb(request):
  response = None
  context = initialize_context(request)
  context["operation_type"] = "getnb"
  token = get_token(request)
  response = get_notebook(token)
  context["notes_list"] = response['value']
  return render(request, 'front_end/result.html', context,status=204)

def createnb(request):
  response = None
  context = initialize_context(request)
  notebook_name = request.POST['notebook_name']
  print(f"notebook name is {notebook_name}")
  token = get_token(request)
  res = create_notebook(token,notebook_name)
  context["operation_type"] = "create"
  return render(request, 'front_end/result.html', context)

def notebook(request):
  context = initialize_context(request)
  return render(request, 'front_end/notebook.html', context)

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('app:home'))

def sign_in(request):
  # Get the sign-in flow
  flow = get_sign_in_flow()
  # Save the expected flow so we can use it in the callback
  try:
    request.session['auth_flow'] = flow
  except Exception as e:
    print(e)
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(flow['auth_uri'])

def callback(request):
  # Make the token request
  result = get_token_from_code(request)

  #Get the user's profile
  user = get_user(result['access_token'])

  # Store user
  store_user(request, user)
  return HttpResponseRedirect(reverse('app:home'))

def home(request):
  context = initialize_context(request)
  return render(request, 'front_end/home.html', context)

def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context