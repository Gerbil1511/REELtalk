# Use Cases

## 1. Admin Management
### Use Case - Manage Users:
### Actor: Admin
**View, Create, Edit or Delete Users**: As an admin, I want to view a list of all users in the database. I then want to be able to create, edit or delete user details.

- The admin navigates to the user management section in the admin dashboard.
- The admin can filter users by username, email, status or other criteria.
- The application displays a list of all users with options to add, view, edit, or delete them.
- The admin makes the necessary changes (e.g., updating user information or changing user roles).
- The application asks for confirmation before any deletion.
- The admin confirms the deletion.
- The application updates the user information and displays a confirmation message.

### Use Case - Manage Forum Posts:
### Actor: Admin 
**Moderate Posts**: As an admin, I want to view, create, edit or delete forum posts.

- The admin navigates to the forum posts management section of the admin dashboard.
- The dashboard displays a list of all forum posts with options to add, view, edit, or delete them.
- The admin can filter the posts by movie, author, creation date, or other criteria.
- The admin selects a forum post to view, add, edit or delete.
- The admin makes the necessary changes (e.g., correcting content or removing inappropriate language).
- The application asks for confirmation before any deletion.
- The admin confirms the deletion.
- The application updates the post and displays a confirmation message.


### Use Case - Manage Movies List:
### Actor: Admin
**View and Delete Movies**: As an admin, I want to view and be able to add or delete any movie in the database.

- The admin navigates to the movie management section in the admin dashboard.
- The admin can filter users by genre, date or other criteria.
- The application displays a list of all movies with options to add, view or delete them.
- The admin makes the necessary changes.
- The application asks for confirmation before any deletion.
- The admin confirms the deletion.
- The application updates the user information and displays a confirmation message.
<br>
<br>

## 2. User Functionality:
### Use Case - User Registration:
### Actor: User
**Register**: As a user, I want to register for an account so I can access the app.

- The user navigates to the navbar on the homepage.
- The user clicks on the "Register" button.
- The user fills in the registration form with their username, first and last name, email, and password.
- The user submits the form.
- The user logs in using their credentials.

### Use Case - User Login:
### Actor: User
**Login**: As a user, I want to log in to my account to use the app's features.

- The user navigates to the navbar on the homepage.
- The user clicks on the "Login" button.
- The user fills in their username and password.
- The user submits the form.
- The user is directed to the home page.

### Use Case - User Logout:
### Actor: Logged-in User
**Logout**: As a user, I want to log out of my account for security.
- The user navigates to the navbar on the homepage.
- The user clicks on the "Logout" button.
- The user is asked to confirm they want to logout
- The user confirms logout.
- The user is directed to the home page.

### Use Case - User Profile Management:
### Actor: Logged-in User
**View and Edit User Profile**: As a user, I want to view and edit my profile so that I can update my personal information and customize my profile settings.

- The user clicks on the "Profile" or "My Account" link/button in the website's navigation menu.
- The user reviews personal information displayed on the profile page, such as name, email, bio, and profile picture.
- The user clicks on the "Edit Profile" or "Delete Profile" buttons to access the form for updating profile details or deleting their account.
- The user completes or updates the form fields with the new personal information to be changed (e.g., name, email, bio, profile picture).
- The user clicks the "Save" or "Update" button to submit the changes.
- The application asks for confirmation before any deletion.
- The user confirms the deletion.
- The user see a success message confirming that the profile has been updated or deleted
- The user reviews the updated profile information to ensure the changes have been applied correctly.
- The user is taken to the home page on successful profile deletion.
<br>
<br>

## 3. Movie Functionality
### Use Case - View Top Latest 20 Movies:
### Actor: Logged-in User
**View Top 20 Movies**: As a user, I want to see the Top 20 latest movies on the home page.

- The user logs in to the application.
- The application displays a list of Top 20 latest movies matching in the home template.
- The user clicks on a movie title to view its details.

### Use Case - Search TMDb API Database:
### Actor: Logged-in User
**Search Movie**: As a user, I want to search for a specific movie.

- The user logs in to the application.
- The user enters the movie title or other search criteria (e.g. genre, release date) in the search bar in the navigation bar.
- The user clicks the "Search" button.
- The application displays a list of movie results matching the search criteria.


### Use Case - View Movie Information:
### Actor: Logged-in User
**View Movie Details**: As a user, I want to view details of a specific movie and any forum posts associated with it.

- The user logs in to the application.
- The user searches for a movie in the search box in the navigation bar.
- The user clicks on a movie title from the search results.
- The application displays the movie's details including title, poster, genre, release date, director, and overview.
- The user can view related forum posts or create a forum post about the movie from the movie detail page.


## 4 . Forum CRUD Functionality:
### Use Case - View All Forum Posts:
### Actor: Logged-in User
**View All Posts**: As a user, I want to see all forum posts.

- The user logs in to the application.
- The user navigates to the Forum page by clicking the link in the navigation bar.
- The user clicks on a forum post to view its content.

### Use Case - Create A Forum Post:
### Actor: Logged-in User
**Create Post**: As a user, I want to create a new forum post.

- The user navigates to the movie detail page.
- The user clicks on the "Create New Post" button.
- The user fills in the post form with the title and content.
- The user submits the form.
- The application saves the post and displays it in the forum post list for the movie and displays a success/error message.

### Use Case - Edit A Forum Post:
### Actor: Logged-in User
**Edit Post**: As a user, I want to edit my own forum post.

- The user navigates to their forum post.
- The user clicks on the "Edit Post" button.
- The user updates the post content.
- The user submits the form.
- The application updates the post and displays the edited content and displays a success/error message.

### Use Case - Delte A Forum Post:
### Actor: Logged-in User
**Delete Post**: As a user, I want to delete my own forum post.
Description: A user wants to delete their existing forum post. 

- The user navigates to their forum post.
- The user clicks on the "Delete Post" button.
- The user confirms the deletion.
- The application removes the post from the forum list and displays a success/error message.

### Use Case - View Forum Posts In Movie Detail Page:
### Actor: Logged-in User
**View Post by Movie**: As a user, I want to see forum posts associated with a specific movie.

- The user either:
    - searches for a movie in the search box in the navigation bar, which then provides a list of movies the user can click on, which then displays the forum posts associated with that movie
    - clicks on one of the movies in the top 20 movies list which then displays the movie details and also displays any forum posts associated with it
    - clicks on the forum link in the nagigation bar and surveys the full forum posts list to see if any of the posts display a link to the movie that matches their desired selection.
- The user can view related forum posts or create a forum post about the selected movie 

### Use Case - Voting System:
### Actor: Logged-in User
**Upvote/Downvote Post**: As a user, I want to upvote or downvote a forum post.

- The user navigates to the forum post they wish to upvote or downvote.
- The user clicks on the "Upvote" or "Downvote" button.
- The application updates the upvote or downvote count for the post.
- The updated counts are displayed to all users viewing the post.



## 5. General Application Functionality:
### Use Case - Movie/News Features:
### Actor: Any Site Visitor
**View Latest News**: As a site visitor, I want to see a selection of newly released movies and the latest entertainment/movie news.

- The site visitor navigates to the homepage.
- The application displays a list of the Top 20 latest movies and the latest movie news articles.
- The site visitor clicks on any movie title in the Top 20 latest movies list or any entertainment/movie news article title to read more details.



## 6. Testing and Deployment Framework 
### Use Case - Testing The App
### Actor: Developer
**Testing**: As a developer, I want to ensure the application works correctly at various levels.

- The developer configures the environment for running tests.
- The developer Develops unit tests for individual components.
- The developer creates integration tests for combined components.
- The developer develops end-to-end tests to simulate user interactions.
- The developer executes performance tests to measure application load handling.
- The developer reviews test outcomes to identify and fix issues.
- The developer improves application performance based on test findings.

### Use Case - Deploying The App
### Actor: Developer
**Deployment**: As a developer, I want to be able to deploy the application to a production environment, i.e. Heroku.

- The developer sets up the production environment (e.g., Heroku).
- The developer adjusts settings for successful deployment.
- The developer deploys the application to the production environment.
- The developer checks that the application runs correctly post-deployment.
- The developer continuouslys monitor the application for any issues.








