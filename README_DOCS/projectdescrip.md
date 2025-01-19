Based on the provided context and the structure of your project, here's a description of how 
your project is working from a user's perspective:

Project Overview
Your project, "ReelTalk," is a movie-centric full-stack web application designed for movie enthusiasts.
It combines the excitement of discovering new films with the interactive experience of a community forum. 
Users can explore detailed movie information, participate in discussions, and stay updated with the latest 
movie news.


Key Features

1. Movie Database Integration:
The application integrates with The Movie Database (TMDb) API to provide users with an extensive 
database of movie information.
Users can search for movies, view detailed information, and stay updated with the latest movie news.

2. Community Forum:
Users can create and manage discussions about movies in the forum.
The forum allows users to share reviews, debate plot twists, and recommend hidden gems.
Only the author of a post can edit or delete their posts, ensuring content integrity and user 
accountability.

3. User Authentication:
The application uses Django Allauth for user authentication, allowing users to sign up, log in, 
and logout.
Users must be logged in to create, edit, delete or vote on forum posts.


User Experience

1. Home Page:
The home page displays a selection of top 20 movies fetched from the TMDb API.
Users can search for movies using the search bar.

2. Movie Detail Page:
Clicking on a movie title returned from a search or from the top 20 selection takes the user to the movie detail page, which displays further information about the movie.
Users can see a list of forum posts related to the movie and logged in users can participate in discussions.

4. Forum:
The forum page displays a list of all forum posts.
Users can click on a post to view its details, including the author, content, associated movie details (i.e. movie poster and name) and up/downvotes.
Logged-in users can create new posts, edit their existing posts, delete their posts and up/downvote on otheir post and others only once.

5. Post Creation and Management:
Users can create new forum posts by filling out a form with the post title and content.
Only the author of a post can edit or delete it. If a user tries to edit or delete a post 
they do not own, they will see an error message.


Technical Details

1. Models:
The Movie model stores information about movies, including title, slug, TMDb ID, overview, release date, 
poster path, vote average, vote count and genre IDs.
The ForumPost model stores information about forum posts, including the related movie, post author, 
title, content, created_at/updated_at timestamps and upvotes/downvotes.

<!-- 2. Views: NEEDS ALTERING TO REFLECT THE NEW VIEWS -->
<!-- The views handle the logic for displaying movie information, forum posts, and managing post 
creation, editing, and deletion.
The forum_post_list view displays a list of all forum posts.
The forum_post_detail view displays the details of a specific forum post and handles post 
editing and deletion.
The create_or_edit_post view handles the creation and editing of forum posts. -->

3. Templates:
The templates define the HTML structure for the pages, including the home page, movie detail page, 
forum post list, and forum post detail page.
The templates use Django template tags and javascript to dynamically display content and handle form submissions.

Conclusion
Overall, "ReelTalk" provides a comprehensive and engaging platform for movie enthusiasts to 
explore movie information and participate in community discussions. The application ensures a 
smooth responsive user experience with features like user authentication, post management, and integration 
with the TMDb and News APIs.



# User Case for ReelTalk

## Overview
ReelTalk is a movie-centric full-stack web application designed for movie enthusiasts. It combines the excitement of 
discovering new films with the interactive experience of a community forum. Users can explore detailed movie 
information, participate in discussions, and stay updated with the latest movie news.

## Key Features

1. **Movie Database Integration**:
   - Integration with The Movie Database (TMDb) API.
   - Users can search for movies, view detailed information, and stay updated with the latest movie news.

2. **Community Forum**:
   - Users can create and manage discussions about movies.
   - Only the author of a post can edit or delete their posts.

3. **User Authentication**:
   - Uses Django Allauth for user authentication.
   - Users must be logged in to create, edit, or delete forum posts.

## User Experience

1. **Home Page**:
   - Displays a list of movies fetched from the TMDb API.
   - Users can search for movies using the search bar.

2. **Movie Detail Page**:
   - Clicking on a movie title takes the user to the movie detail page, which displays detailed 
   information about the movie.
   - Users can see a list of forum posts related to the movie and participate in discussions.

3. **Forum**:
   - The forum page displays a list of all forum posts.
   - Users can click on a post to view its details, including the author, content, and comments.
   - Logged-in users can create new posts, edit their existing posts, and delete their posts.

4. **Post Creation and Management**:
   - Users can create new forum posts by filling out a form with the post title and content.
   - Only the author of a post can edit or delete it. If a user tries to edit or delete a 
   post they do not own, they will see an error message.