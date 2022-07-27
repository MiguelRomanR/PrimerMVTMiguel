from multiprocessing import context
from django.shortcuts import render
from Family.models import Members
# Create your views here.


def create_members(request):
    new_member = Members.objects.create(
        name='Ana',
        last_name='Roman',
        relation='Hermana'
    )
    context = {
        'new_member': new_member
    }
    return render(request, 'new_member.html', context=context)


def list_members(request):
    members = Members.objects.all()
    context = {
        'members': members
    }
    return render(request, 'family_members.html', context=context)
