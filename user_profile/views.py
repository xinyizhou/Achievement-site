from django.shortcuts import render_to_response
from django.contrip.auth import User
from user_profile.models import UserProfile
from achievement.models import Achievement, CompletedAchievement

def user_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_score = UserProfile.objects.filter(id=user_id)
    user_complete_achievemenrt = user.complete_achievement.all()
    render_to_response('user_info', locals())
