from django.shortcuts import render_to_response, get_object_or_404, redirect
from achievement.models import Achievement, CompletedAchievement
from cycle.models import Cycle
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required


def homepage(request):
    start_cycle = Cycle.objects.all().order_by('-start_date')[0]
    all_active_achievement = Achievement.objects.filter(status=True, deadline__gt=start_cycle.start_date)
    user_has_completed_achievement = []
    for achievement in all_active_achievement:
        user_has_completed_achievement.append(CompletedAchievement.objects.filter(user=request.user, achievement=achievement).count)
    tuple_active_acievement_and_completed = zip(all_active_achievement, user_has_completed_achievement)
    return render_to_response('homepage.html', locals())

def achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, id=achievement_id)
    witnesses = User.objects.all()
    achievement_duration = achievement.get_duration_display()
    achievement_category = achievement.get_category_display()
    user_has_completed_achievement = CompletedAchievement.objects.filter(user=request.user, achievement=achievement).count
    all_completed_achievements = CompletedAchievement.objects.filter(achievement=achievement)
    competition = []
    for completed_achievement in all_completed_achievements:
        competition.append(completed_achievement.user.username)
    return render_to_response('achievement.html', locals())

def set_completed_achievement(request, achievement_id, witness_id):
    current_cycle = Cycle.objects.filter(is_active=True)[0]
    achievement = get_object_or_404(Achievement, id=achievement_id)
    witness = get_object_or_404(User, id=witness_id)
    completed_achievement = CompletedAchievement(user=request.user, achievement=achievement, witness=witness, cycle=current_cycle)
    user = UserProfile.objects.get(id=request.user.id)
    user.score += achievement.points
    user.save()
    completed_achievement.save()
    return redirect('/')
    
def get_achievement_for_vote(request):
    all_inactive_achievement = Achievement.objects.filter(status=False)
    return render_to_response('vote_list.html', locals())

def vote_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, id=achievement_id)
    achievement_duration = achievement.get_duration_display()
    achievement_category = achievement.get_category_display()
    return render_to_response('vote_achievement.html', locals())

def vote_for(request, achievement_id):
     achievement = get_object_or_404(Achievement, id=achievement_id)
     all_user = User.objects.all().count()
     achievement.user_vote.add(request.user)
     if achievement.user_vote.count()/all_user >= 0.5:
         achievement.status = True
     achievement.save()
     all_inactive_achievement = Achievement.objects.filter(status=False)
     return redirect('/vote_list/')

