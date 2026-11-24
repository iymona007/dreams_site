from django import template

from ..models import UserStats

register = template.Library()


@register.inclusion_tag('universe/_level.html')
def level_badge(user, compact=False):
    if not getattr(user, 'is_authenticated', False):
        return {'s': None}
    stats = UserStats.objects.filter(user=user).first() or UserStats(user=user)
    return {'s': stats, 'compact': compact}
