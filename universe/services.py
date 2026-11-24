from django.utils import timezone

from .models import Mission, UserStats

XP_NEW_DREAM = 20
XP_ACHIEVED = 100
XP_BOTTLE_OPEN = 15


def get_stats(user):
    stats, _ = UserStats.objects.get_or_create(user=user)
    return stats


def award(user, amount):
    stats = get_stats(user)
    stats.xp += amount
    stats.coins += amount // 2
    stats.save(update_fields=['xp', 'coins'])
    return stats


def today_mission():
    missions = list(Mission.objects.filter(is_active=True).order_by('pk'))
    if not missions:
        return None
    return missions[timezone.localdate().toordinal() % len(missions)]
