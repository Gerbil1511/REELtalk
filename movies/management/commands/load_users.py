from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generate 20 fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()  # Corrected this line

        for _ in range(20):
            username = fake.user_name()
            email = fake.email()
            password = 'password123'  # You can set a default password for all fake users

            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=False
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 20 fake users'))