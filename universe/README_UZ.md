# DREAMS Universe: 1-bosqich (XP, Sirli eshik, Orzu shishasi)

1. `universe/` papkasini loyihangiz ildiziga (manage.py yoniga) qo'ying.
2. settings.py: INSTALLED_APPS ga `'universe'` qo'shing.
3. Asosiy urls.py: `path('', include('universe.urls')),`
4. `templates_updated/index.html` va `profile.html` ni o'z shablonlaringiz o'rniga qo'ying
   (index.html: yangi havolalar va universe.css; profile.html: daraja paneli).
5. Terminal:
   python manage.py makemigrations universe
   python manage.py migrate
   python manage.py seed_missions
6. Orzu modeli `dreams.Dream` emas bo'lsa, `universe/signals.py` dagi DREAM_MODEL ni o'zgartiring.
