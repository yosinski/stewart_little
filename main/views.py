from datetime import datetime, timedelta
import os
import random

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat
from django.db.models import Avg
from django.db import models

import settings



def static(request, page):
    return render_to_response(page,
                              RequestContext(request))



def index(request):
    '''Main home page'''

    return render_to_response('main/index.html',
                              context_instance = RequestContext(request))
