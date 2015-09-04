import requests
import json
from helpdesk.models import Ticket
from django.conf import settings

def get_issue(repo):
    r = requests.get(repo)
    if(r.ok):
        repoItem = json.loads(r.text or r.content)
        print "Django repository created: " + repoItem['created_at']

def new_issue(repo,ticket):

    payload = {}
    labels = ['Tola-Help Ticket']
    payload['title'] = ticket.title
    payload['body'] = ticket.description
    payload['labels'] = labels

    token = settings.GITHUB_AUTH_TOKEN

    header = {'Authorization': 'token %s' % token}
    r = requests.post(repo,json.dumps(payload),headers=header)

    #Update ticket with new github info if created successfully "201" response
    if int(r.status_code) == 201:
        #print r.content
        data = json.loads(r.content)
        github_issue_url = data['html_url']
        github_issue_number = data['number']
        github_issue_id = data['id']


        update_ticket = Ticket.objects.get(id=ticket.id)
        update_ticket.github_issue_url = github_issue_url
        update_ticket.github_issue_number = github_issue_number
        update_ticket.github_issue_id = github_issue_id
        update_ticket.save()

    return r.status_code

def update_issue(repo,ticket,id):

    payload = {}
    labels = ['Tola-Help Ticket']
    payload['title'] = ticket.title
    payload['body'] = ticket.description
    payload['labels'] = labels

    token = settings.GITHUB_AUTH_TOKEN
    repo = repo + "/" + ticket.github_issue_number

    header = {'Authorization': 'token %s' % token}
    r = requests.post(repo,json.dumps(payload),headers=header)
    #Update ticket with new github info if created successfully "201" response
    if int(r.status_code) == 201:
        data = json.loads(r.content)
        github_issue_url = data['html_url']
        github_issue_number = data['number']
        github_issue_id = data['id']

        update_ticket = Ticket.objects.get(id=ticket.id)
        update_ticket.github_issue_url = github_issue_url
        update_ticket.github_issue_number = github_issue_number
        update_ticket.github_issue_id = github_issue_id
        update_ticket.save()

    return r.status_code