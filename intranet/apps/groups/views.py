import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def groups_view(request):
    context = {"user": request.user,
               "page": "groups"
              }
    return render(request, "groups/groups.html", context)
