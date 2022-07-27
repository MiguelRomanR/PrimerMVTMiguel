from multiprocessing import context
from django.shortcuts import render
from Family.models import Members
# Create your views here.


def create_members(request):
    new_member = Members.objects.create(
        name='Maria',
        last_name='Roman',
        relation='Prima'
    )
    context = {
        'new_member': new_member
    }
    return render(request, 'new_member.html', context=context)
