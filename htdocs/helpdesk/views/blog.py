from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, Context, RequestContext
from django.conf import settings
import os
from helpdesk.hackpad import Hackpad


def index(request):

    temp = Hackpad('tola',settings.HACKPAD_CLIENT_ID,settings.HACKPAD_SECRET)
    my_hackpads = temp.list_all()

    print my_hackpads

    return render_to_response('blog/base.html',RequestContext(request, {'hackpad': my_hackpads}))