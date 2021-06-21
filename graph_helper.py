import requests
import json

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  # Send GET to /me
  user = requests.get(
    '{0}/me'.format(graph_url),
    headers={
      'Authorization': 'Bearer {0}'.format(token)
    },
    params={
      '$select': 'displayName,mail,mailboxSettings,userPrincipalName'
    })
  # Return the JSON result
  return user.json()

def get_notebook(token):
    notebook = requests.get(
    '{0}/me/onenote/notebooks'.format(graph_url),
    headers={
      'Authorization': 'Bearer {0}'.format(token)
    },)
    return notebook.json()
  
def create_notebook(token,notebook_name):
    new_event = {
    "displayName": notebook_name
    }
    notebook = requests.post(
    '{0}/me/onenote/notebooks'.format(graph_url),
    headers={
      'Authorization': 'Bearer {0}'.format(token)
    },
    params=json.dumps(new_event))
    return notebook.json()