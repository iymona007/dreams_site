from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import BottleForm
from .models import Bottle, MissionCompletion
from .services import XP_BOTTLE_OPEN, award, get_stats, today_mission


@login_required
def mission(request):
    m = today_mission()
    today = timezone.localdate()
    done = bool(m) and MissionCompletion.objects.filter(user=request.user, mission=m, date=today).exists()
    if request.method == 'POST' and m and not done:
        _, created = MissionCompletion.objects.get_or_create(
            user=request.user, mission=m, date=today,
            defaults={'answer': request.POST.get('answer', '').strip()},
        )
        if created:
            award(request.user, m.xp_reward)
            messages.success(request, f'Eshik ochildi! +{m.xp_reward} XP ✨')
        return redirect('mission')
    history = MissionCompletion.objects.filter(user=request.user).select_related('mission').order_by('-date')[:7]
    return render(request, 'universe/mission.html', {
        'mission': m, 'done': done, 'history': history, 'stats': get_stats(request.user),
    })


@login_required
def bottle_list(request):
    return render(request, 'universe/bottle_list.html', {
        'bottles': Bottle.objects.filter(user=request.user).order_by('open_at'),
    })


@login_required
def bottle_create(request):
    form = BottleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        b = form.save(commit=False)
        b.user = request.user
        b.save()
        messages.success(request, f"Shisha dengizga tashlandi 🍾 {b.open_at:%d.%m.%Y} kuni ochiladi.")
        return redirect('bottle_list')
    return render(request, 'universe/bottle_form.html', {'form': form})


@login_required
def bottle_detail(request, pk):
    b = get_object_or_404(Bottle, pk=pk, user=request.user)
    if b.is_open and not b.opened_at:
        b.opened_at = timezone.now()
        b.save(update_fields=['opened_at'])
        award(request.user, XP_BOTTLE_OPEN)
        messages.success(request, f'Shisha ochildi! +{XP_BOTTLE_OPEN} XP 🍾')
    return render(request, 'universe/bottle_detail.html', {'bottle': b})
