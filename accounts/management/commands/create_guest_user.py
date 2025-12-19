from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()


class Command(BaseCommand):
    help = "Creates read-only guest user for demo"

    def handle(self, *args, **options):
        guest, created = User.objects.get_or_create(
            email="guest@adminita.demo",
            defaults={
                "is_staff": True,
                "is_active": True,
                "first_name": "Guest",
                "last_name": "User",
            },
        )
        guest.set_password("demopassword123")
        guest.save()

        view_perms = Permission.objects.filter(codename__startswith="view_")
        guest.user_permissions.set(view_perms)

        self.stdout.write(
            self.style.SUCCESS(
                f"Guest user ready with {view_perms.count()} view permissions"
            )
        )
        self.stdout.write(f"Login: guest@adminita.demo / demopassword123")
