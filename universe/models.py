from django.conf import settings
from django.db import models
from django.utils import timezone

LEVEL_XP = 100
TITLES = [
    'Orzuchi', 'Yulduz izlovchi', 'Oy sayyohi', 'Kometa ovchisi',
    'Galaktika yo\'lboshchisi', 'Yulduz turkumi ustasi', 'Koinot ijodkori',
]


class UserStats(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stats')
    xp = models.PositiveIntegerField(default=0)
    coins = models.PositiveIntegerField(default=0)

    @property
    def level(self):
        return self.xp // LEVEL_XP + 1

    @property
    def progress(self):
        return self.xp % LEVEL_XP

    @property
    def title(self):
        return TITLES[min(self.level - 1, len(TITLES) - 1)]

    def __str__(self):
        return f'{self.user} · Lv {self.level} · {self.xp} XP'


class Mission(models.Model):
    title = models.CharField('Sarlavha', max_length=120)
    description = models.TextField('Topshiriq / savol')
    xp_reward = models.PositiveIntegerField(default=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MissionCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mission_completions')
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    answer = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'mission', 'date')


class Bottle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bottles')
    text = models.TextField('Xabar')
    open_at = models.DateField('Ochilish sanasi')
    created_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['open_at']

    @property
    def is_open(self):
        return timezone.localdate() >= self.open_at

    @property
    def days_left(self):
        return max((self.open_at - timezone.localdate()).days, 0)

    def __str__(self):
        return f'Shisha #{self.pk} ({self.user})'



class Dream(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Barcha uchun ochiq'),
        ('private', 'Faqat o‘zim uchun'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='dreams'
    )
    title = models.CharField('Orzu sarlavhasi', max_length=200)
    text = models.TextField('Orzu haqida')
    visibility = models.CharField(
        'Ko‘rinish',
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default='public'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class DreamImage(models.Model):
    dream = models.ForeignKey(
        Dream,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        'Orzu rasmi',
        upload_to='dreams/images/'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.dream.title} — rasm #{self.pk}'
