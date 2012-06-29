from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from server.free2me.models import User,Resource,Relationship,Using,Waiting

def index(request):
    users = User.objects.all()
    resources = Resource.objects.all()
    return render_to_response(  './index.html', {'users':users,'resources':resources})

def user(request,user_name):
    user_found = get_object_or_404(User, name=user_name)
    relationship = get_list_or_404(Relationship, user=user_found)
    return render_to_response('./user.html',{'user':user_found,'relationship':relationship})

def resource(request,resource_name):
    resource_found = get_object_or_404(Resource, name=resource_name)
    relationship = get_list_or_404(Relationship, resource=resource_found)
    return render_to_response('./resource.html',{'resource':resource_found,'relationship':relationship})

def using(request):
    using = Using.objects.all()
    return render_to_response(  './using.html', {'using':using})

def waiting(request):
    waiting = Waiting.objects.all()
    return render_to_response(  './waiting.html', {'waiting':waiting})

