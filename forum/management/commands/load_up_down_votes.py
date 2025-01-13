import random
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import ForumPost

class Command(BaseCommand):
    help = 'Generate random upvotes and downvotes for existing forum posts'

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        total_users = len(users)
        posts = ForumPost.objects.all()

        for post in posts:
            # Generate random upvotes and downvotes
            num_upvotes = random.randint(0, total_users)
            num_downvotes = random.randint(0, total_users)
            upvoters = random.sample(users, min(num_upvotes, total_users))
            downvoters = random.sample(users, min(num_downvotes, total_users))

            for upvoter in upvoters:
                post.upvotes.add(upvoter)

            for downvoter in downvoters:
                post.downvotes.add(downvoter)

        self.stdout.write(self.style.SUCCESS('Successfully generated random upvotes and downvotes for existing forum posts'))