
# Project Overview
The project, "ReelTalk," is a movie-centric full-stack web application designed for movie enthusiasts.
It combines the excitement of discovering new films with the interactive experience of a community forum. 
Users can explore detailed movie information, participate in discussions, and stay updated with the latest movie news.


Key Features

1. TMDB and News API Integration:
The application integrates The Movie Database (TMDb) API to enable users to search a 
database of movie information.
Users can search for movies, view curated movie lists, detailed information, and stay updated with the latest movie news.

2. Community Forum:
Users can create and manage discussions about movies in the forum.
The forum allows users to share reviews, comment and vote on posts, debate plot twists, and recommend hidden gems.
Only the author can edit or delete their posts/comments, ensuring content integrity and user accountability.

3. User Authentication:
The application uses Django Allauth for user authentication, allowing users to sign up, log in, 
and logout.
Users must be logged in to create, edit, delete or vote on forum posts/comments.
Users can update/delete their profile information.


User Experience

1. Home Page:
The home page displays a selection of the latest Entertainment news and a hero image with a CTA button.


2. Movies Page:
Clicking on a movie title returned from a search or from the curated lists takes the user to the movie detail page, which displays further information about the movie.
Users are encouraged to post a review or share their thoughts about the movie with a link to the forum page.

4. Forum:
The forum page displays a list of all forum posts.
Users can click on a post to view its details, including the author, content, associated movie details (i.e. movie poster and name) number of comments and up/downvotes.
Logged-in users can create new posts/comments, edit their existing posts/comments, delete their posts/comments and up/downvote on their posts and others only once.

5. Post Creation and Management:
Users can create new forum posts/comments by filling out a form with the post title and content.
Only the author of a post can edit or delete it. If a user tries to edit or delete a post 
they do not own, they will see an error message.

6. User Profile:
Logged-in users can update or delete their profiles and can see a list of all their posts and comments which they can also edit/delete.


Technical Details

1. Models:
The Movie model stores information about movies, including title, slug, TMDb ID, overview, release date, poster path, vote average, vote count and genre IDs.
The ForumPost model stores information about forum posts, including the related movie, post author, 
title, content, created_at/updated_at timestamps and upvotes/downvotes.
The PostComment model stores information about the comments on forum posts inlcuding the comemtn auhor, title, content.

2. Views:
The views handle the logic for displaying movie information, forum posts, comments and managing post/comment creation, editing, and deletion.


3. Templates:
The templates define the HTML structure for the pages, including the home page, movies page and 
community forum page.
The templates use HTML, CSS, Bootstrap 5.3.3, Django template tags and javascript to dynamically display content and handle form submissions.

Conclusion
Overall, "ReelTalk" provides a comprehensive and engaging platform for movie enthusiasts to 
explore movie information and participate in community discussions. The application ensures a 
smooth responsive user experience with features like user authentication, post management, and integration 
with the TMDb and News APIs.
