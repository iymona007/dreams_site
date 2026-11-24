from django.core.management.base import BaseCommand

from universe.models import Mission

MISSIONS = [
    ("Bugungi savol", "Agar hech qanday to'siq bo'lmasa, bir yildan keyin qayerda bo'lishni xohlardingiz? Qisqa yozing."),
    ("Rasm topshirig'i", "Orzuingizni eng yaxshi ifodalaydigan bitta rasm tanlang va nega aynan shu ekanini yozing."),
    ("Kichik qadam", "Orzuingiz sari bugun qila oladigan eng kichik qadam nima? Uni yozing va bajaring."),
    ("Minnatdorchilik", "Orzuingizga yaqinlashtirgan bitta odamni yoki voqeani eslang va nima uchun minnatdorligingizni yozing."),
    ("Uch so'z", "Orzuingizni uchta so'z bilan ta'riflang."),
    ("Xat", "10 yildan keyingi o'zingizdan bitta savol so'rang."),
    ("Qo'rquv", "Orzuingiz yo'lidagi eng katta qo'rquvingiz nima? Uni yengish uchun nima yordam beradi?"),
    ("Ilhom", "Sizni ilhomlantirgan odam yoki asarni va undan nimani o'rganganingizni yozing."),
    ("Rang", "Orzuingiz qaysi rangda va nega? Bir-ikki gap bilan tasvirlang."),
    ("Bir kun", "Orzuingiz amalga oshgan kunning ertalabini tasvirlab bering."),
]


class Command(BaseCommand):
    help = "Kunlik missiyalarni bazaga qo'shadi"

    def handle(self, *args, **opts):
        n = 0
        for title, desc in MISSIONS:
            _, created = Mission.objects.get_or_create(title=title, defaults={'description': desc})
            n += created
        self.stdout.write(self.style.SUCCESS(f"{n} ta yangi missiya qo'shildi"))
