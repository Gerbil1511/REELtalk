import os
import django
import random
from faker import Faker
from django.utils.text import slugify
import string

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reeltalk.settings')
django.setup()

from forum.models import ForumPost, PostComment
from movies.models import Movie
from django.contrib.auth.models import User

fake = Faker()

# Sentiments
sentiments = {
    'positive': [
        "Amazing movie! Highly recommend.",
        "Loved every moment of it.",
        "A masterpiece of modern cinema."
        "An outstanding film with brilliant performances and a captivating storyline."
        "A visual masterpiece that keeps you engaged from start to finish."
        "A heartwarming and inspirational movie with exceptional acting."
        "An unforgettable cinematic experience with stunning visuals and a gripping plot."
        "A must-watch film with a perfect blend of humor, drama, and action."
        "The director's vision shines through in this beautifully crafted film."
        "A thoroughly enjoyable movie with well-developed characters and a strong narrative."
        "A masterpiece of storytelling with top-notch performances by the cast."
    ],
    'neutral': [
        "It was okay, not great but not bad.",
        "An average movie, nothing special.",
        "Had some good moments, but overall just fine."
        "A decent film with solid performances, but the plot is somewhat predictable."
        "The visuals are impressive, but the storyline lacks depth."
        "An enjoyable watch, though it doesn't break any new ground."
        "The acting is good, but the pacing can be uneven at times."
        "A respectable film with some memorable moments, but it falls short overall."
        "An interesting concept, but the execution could have been better."
        "The movie has its moments, but it doesn't fully deliver on its potential."
        "A competent film, though it may not appeal to everyone."
        "A solid effort with decent performances, but it lacks the wow factor."
    ],
    'negative': [
        "Didn't enjoy it at all.",
        "A waste of time, very disappointing.",
        "Terrible movie, wouldn't recommend."
        "A disappointing film with a convoluted plot and lackluster performances."
        "The movie fails to engage, with uninspired action sequences and weak dialogue."
        "A forgettable film that lacks originality and depth."
        "The pacing is slow, and the characters are poorly developed."
        "An underwhelming movie that doesn't live up to its potential."
        "The visuals are overdone, and the story is not compelling."
        "A mediocre film with forced humor and a predictable plot."
        "The performances are unconvincing, and the script is weak."
        "A poorly executed film that leaves much to be desired."
    ]
}

# Fetch all users and movies
users = list(User.objects.all())
movies = list(Movie.objects.all())

# Number of posts and comments per movie
NUM_POSTS_PER_MOVIE = 3
NUM_COMMENTS_PER_POST = 3

for movie in movies:
    for _ in range(NUM_POSTS_PER_MOVIE):
        author = random.choice(users)
        sentiment = random.choice(list(sentiments.keys()))
        title = fake.sentence(nb_words=6)
        content = random.choice(sentiments[sentiment])
        
        slug = slugify(title)
        while ForumPost.objects.filter(slug=slug).exists():
            slug = f"{slugify(title)}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}"
        
        post = ForumPost.objects.create(
            movie=movie,
            author=author,
            title=title,
            content=content,
            slug=slug,
            status=1,  # Published
            approved_post=True
        )
        
        for _ in range(NUM_COMMENTS_PER_POST):
            comment_author = random.choice(users)
            comment_content = fake.sentence(nb_words=12)
            
            PostComment.objects.create(
                post=post,
                author=comment_author,
                comment=comment_content,
                approved_comment=True
            )

print("Forum posts and comments have been populated.")