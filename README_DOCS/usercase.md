<div style="text-align: center;"> <h1>REELtalk - USE CASES</h1> </div>
<br>

## 1. Admin Management of Forum Posts and Users

### Use Case 1 - Manage Users:
### Actor: Admin User
Description: An admin wants to manage the users to ensure the community stays healthy and 
follows the guidelines. 
<br>
<br>
_Steps:_

View Users:

- The admin navigates to the user management section in the admin dashboard.

- The application displays a list of all users with options to view, edit, or delete them.

- The admin can filter users by username, email, status or other criteria.


Edit User:

- The admin selects a user to edit.

- The application displays the user details and an editable form.

- The admin makes the necessary changes (e.g., updating user information or changing user roles).

- The admin submits the form.

- The application updates the user information and displays a confirmation message.


Delete User:

- The admin selects a user to delete.

- The application asks for confirmation before deletion.

- The admin confirms the deletion.

- The application removes the user from the database and displays a confirmation message.
<br>
<br>

### Use Case 2 - Manage Forum Posts:
### Actor: Admin User
Description: An admin wants to manage the posts to ensure the community stays healthy and 
follows the guidelines.
<br>
<br>
_Steps:_

View Forum Posts:

- The admin logs into the admin dashboard.

- The admin navigates to the forum posts management section.

- The application displays a list of all forum posts with options to view, edit, or delete them.

- The admin can filter the posts by movie, author, creation date, or other criteria.


Edit Forum Post:

- The admin selects a forum post to edit.

- The application displays the post details and an editable form.

- The admin makes the necessary changes (e.g., correcting content or removing inappropriate language).

- The admin submits the form.

- The application updates the post and displays a confirmation message.


Delete Forum Post:

- The admin selects a forum post to delete.

- The application asks for confirmation before deletion.

- The admin confirms the deletion.

- The application removes the post from the database and displays a confirmation message.
<br>
<br>
<br>
<br>

## 2. User CRUD Functionality

### Use Case 3 - User Registration and Log In
### Actor: New User 
Description: A new user wants to register and log in to the application to access its features. 
<br>
<br>
_Steps:_

- The user navigates to the navbar on the homepage.

- The user clicks on the "Register" button.

- The user fills in the registration form with their username, first and last name, email, and password.

- The user submits the form.

- The user logs in using their credentials.
<br>
<br>

### Use Case 4 - User Searches for Movies
### Actor: Logged-in User 
Description: A user wants to search for movies to find information about them. 
<br>
<br>
_Steps:_

- The user logs in to the application.

- The user enters the movie title or other search criteria (e.g., genre, release date) in the search bar.

- The user clicks the "Search" button.

- The application displays a list of movies matching the search criteria.

- The user clicks on a movie title to view its details.
<br>
<br>

### Use Case 5 -  User Views Movie Details
### Actor: Logged-in User 
Description: A user wants to view detailed information about a specific movie. 
<br>
<br>
_Steps:_

- The user searches for a movie.

- The user clicks on a movie title from the search results.

- The application displays the movie's details, including title, genre, release date, director, and overview.

- The user can navigate to related forum posts from the movie detail page.
<br>
<br>

### Use Case 6 -  User Creates a Forum Post
### Actor: Logged-in User 
Description: A user wants to create a new forum post about a movie.
<br>
<br>
_Steps:_

- The user navigates to the movie detail page.

- The user clicks on the "Create New Post" button.

- The user fills in the post form with the title and content.

- The user submits the form.

- The application saves the post and displays it in the forum post list for the movie and displays a success/error message.
<br>
<br>

### Use Case 7 -  User Edits a Forum Post
### Actor: Logged-in User (Author of the Post) 
Description: A user wants to edit their existing forum post. 
<br>
<br>
_Steps:_

- The user navigates to their forum post.

- The user clicks on the "Edit Post" button.

- The user updates the post content.

- The user submits the form.

- The application updates the post and displays the edited content and displays a success/error message.
<br>
<br>

### Use Case 8 -  User Deletes a Forum Post
### Actor: Logged-in User (Author of the Post) 
Description: A user wants to delete their existing forum post. 
<br>
<br>
_Steps:_

- The user navigates to their forum post.

- The user clicks on the "Delete Post" button.

- The user confirms the deletion.

- The application removes the post from the forum list and displays a success/error message.
<br>
<br>

### Use Case 9 -  User Upvotes/Downvotes a Forum Post
### Actor: Logged-in User
Description: A user wants to upvote or downvote a forum post to express their opinion on its quality or relevance.
<br>
<br>
_Steps:_

- The user navigates to the forum post they wish to upvote or downvote.

- The user clicks on the "Upvote" or "Downvote" button.

- The application updates the upvote or downvote count for the post.

- The updated counts are displayed to all users viewing the post.
<br>
<br>

### Use Case 10 -  User Views Latest Movie News
### Actor: Logged-in User 
Description: A user wants to stay updated with the latest movie news. 
<br>
<br>
_Steps:_

- The user navigates to the homepage or the dedicated news section.

- The application displays a list of the latest movie news articles.

- The user clicks on an article title to read more details.
<br>
<br>

### Use Case 11 -  User Logs Out
### Actor: Logged-in User 
Description: A user wants logout of the application
<br>
<br>
_Steps:_

- The user sees the "Logout" option in the navigation bar when logged in.

- The user clicks the "Logout" button to initiate the logout process.

- The user is redirected to the homepage or login page after logging out.

- A confirmation message is displayed to inform the user that they have been logged out.

- The user's session is terminated, and they must log in again to access restricted features.