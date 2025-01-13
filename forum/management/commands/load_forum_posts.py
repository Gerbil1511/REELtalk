import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import Movie
from forum.models import ForumPost

class Command(BaseCommand):
    help = 'Generate forum posts for each movie'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = list(User.objects.all())
        movies = Movie.objects.all()[:20]  # Get the top 20 movies

        review_types = {
            'positive': [
                ("Amazing Movie!", "I absolutely loved this movie! The acting was superb and the storyline was captivating."),
                ("Fantastic Film!", "This movie was fantastic! A must-watch for everyone."),
                ("Highly Recommended!", "An amazing film with great performances. Highly recommended!"),
                ("Best thing I've watched in a while!", "This movie  blew my mind. I loved every minute of it."),
                ("Great Movie!", "A great movie with an interesting plot and well-developed characters."),
                ("Loved It!", "I loved this movie! The story was engaging and the acting was top-notch.")
            ],
            'negative': [
                ("Disappointing", "I didn't enjoy this movie at all. The plot was weak and the acting was subpar."),
                ("Waste of Time", "This movie was a waste of time. I wouldn't recommend it."),
                ("Very Boring", "Very disappointing. The story was boring and the characters were uninteresting."),
                ("Not Worth Watching", "This movie was not worth watching. The acting was terrible and the plot was weak."),
                ("Terrible Movie", "I hated this movie. The acting was terrible and the plot was nonsensical."),
                ("Avoid at all costs", "Avoid this movie at all costs. It was a complete waste of time.")
            ],
            'neutral': [
                ("Just Okay", "The movie was okay. Not great, but not terrible either."),
                ("Average Film", "It was an average film. Some parts were good, but others were lacking."),
                ("It Was Fine", "An okay movie. It had its moments, but overall it was just fine."),
                ("Decent Movie", "A decent movie. Not the best, but not the worst either."),
                ("Meh", "Meh. It was an okay movie, but nothing special."),
                ("So-so", "The movie was so-so. It didn't leave much of an impression on me.")
            ]
        }

        for movie in movies:
            num_posts = random.randint(5, 7)
            for _ in range(num_posts):
                user = random.choice(users)
                review_type = random.choice(list(review_types.keys()))
                title, content = random.choice(review_types[review_type])
                ForumPost.objects.create(
                    movie=movie,
                    author=user,
                    title=title,
                    content=content
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated forum posts for each movie'))