from django.shortcuts import render_to_response
from cycle.models import Cycle
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required

def hall_of_fame(request):
    leader_score = UserProfile.objects.all().order_by('-score')[0]
    leader = leader_score.user
    return render_to_response('hall_of_fame.html', locals())
        
