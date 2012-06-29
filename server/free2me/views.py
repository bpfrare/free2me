from django.shortcuts import render_to_response, get_object_or_404
from server.free2me.models import User,Resource

def index(request):
    users = User.objects.all()
    resources = Resource.objects.all()
    return render_to_response(  './index.html', {'users':users,'resources':resources})

def user(request,user_name):
    user_found = get_object_or_404(User, name=user_name)
    return render_to_response('./user.html',{'user':user_found})

