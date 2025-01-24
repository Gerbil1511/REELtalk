# Use Cases

## 1. Admin Management
### <u>Use Case - Manage Users:</u>
### Actor: Admin
**View, Create, Edit or Delete Users**: As an admin, I want to view a list of all users in the database. I then want to be able to create, edit or delete user details.

- The admin navigates to the user management section in the admin dashboard.
- The admin can filter users by username, email, status or other criteria.
- The application displays a list of all users with options to add, view, edit, or delete them.
- The admin makes the necessary changes (e.g., updating user information or changing user roles).
- The application asks for confirmation before any deletion.
- The admin confirms the deletion.
- The application updates the user information and displays a confirmation success/error message.

### <u>Use Case - Manage Forum Posts/Comments:</u>
### Actor: Admin 
**Moderate Posts/Comments**: As an admin, I want to view, create, edit or delete forum posts/comments.

- The admin navigates to the forum posts or comments management section of the admin dashboard.
- The dashboard displays a list of all forum posts or comments with options to add, view, edit, or delete them.
- The admin can filter the posts by various criteria.
- The admin selects a forum post or comment to view, add, edit or delete.
- The admin makes the necessary changes (e.g., correcting content or removing inappropriate language).
- The application asks for confirmation before any deletion.
- The admin confirms the deletion.
- The application updates the post/comment and displays a confirmation success/error message.


### <u>Use Case - Manage Movies List:</u>
### Actor: Admin
**View and Delete Movies**: As an admin, I want to view and be able to add or delete any movie in the database.

- The admin navigates to the movie management section in the admin dashboard.
- The admin can filter the moviesby various criteria.
- The application displays a list of all movies with options to add, view or delete them.
- The admin makes the necessary changes.
- The application asks for confirmation before any deletion.
- The admin confirms the deletion.
- The application updates the movie information and displays a confirmation success/error message.
<br>
<br>

## 2. User Functionality:
### <u>Use Case - User Registration:</u>
### Actor: User
**Register**: As a user, I want to register for an account so I can access the app.

- The user navigates to the navbar on the homepage.
- The user clicks on the "Sign Up" button.
- The user fills in the registration form with their username, first and last name, email, and password.
- The user submits the form.
- The user receives a success/error confirmation message.
- The user logs in using their credentials.

### <u>Use Case - User Login:</u>
### Actor: User
**Login**: As a user, I want to log in to my account to use the app's features.

- The user navigates to the navbar on the homepage.
- The user clicks on the "Login" button.
- The user fills in their username and password.
- The user submits the form.
- The user receives a success/error confirmation message.
- The user is directed to the home page.

### <u>Use Case - User Logout:</u>
### Actor: Logged-in User
**Logout**: As a user, I want to log out of my account for security.

- The user navigates to the navbar on the homepage.
- The user clicks on the "Logout" button.
- The user is asked to confirm if they want to logout
- The user confirms logout.
- The user receives a success/error confirmation message.
- The user is directed to the home page.

### <u>Use Case - User Profile Management:</u>
### Actor: Logged-in User
**View and Edit User Profile**: As a user, I want to view and edit my profile so that I can update my personal information and customize my profile settings.

- The user clicks on the "Profile" or "My Account" link/button in the website's navigation menu.
- The user reviews personal information displayed on the profile page, such as name, email, bio, profile picture and a list of created posts/comments.
- The user clicks on the "Edit Profile" or "Delete Profile" buttons to access the form for updating profile details or deleting their account.
- The user completes or updates the form fields such as new personal information to be changed (e.g., name, email, bio, profile picture), or edits/deletes created posts/comments.
- The user clicks the "Save" or "Update" button to submit the changes.
- The application asks for confirmation before any deletion.
- The user confirms the deletion.
- The user see a success/error message confirming that the profile has/has not been updated or deleted
- The user reviews the updated profile information to ensure the changes have been applied correctly.
- The user is taken to the home page on successful profile deletion.
<br>
<br>

## 3. App Functionality
### <u>Use Case - View Movies Lists:</u>
### Actor: User
**View Latest Popular/Top Rated Movies**: As a user, I want to see the latest popular/top rated movies on the Movies page.

- The user navigates to Movies on the navbar.
- The application displays a list of the latest popular/top rated movies as carousels in the template which the user can click on for further information if desired.

### <u>Use Case - Search Movie Database:</u>
### Actor: User
**Search Movie**: As a user, I want to search for a specific movie and view it's details.

- The user navigates to Movies on the navbar.
- The user enters the movie title in the search bar on the page.
- The user clicks the "Search" button.
- The application either displays a list of movie results as cards matching the search criteria or displays a "no movies found matching your search criteria".
- The user clicks on the 'view more details' button on a movie card and is directed to the movie details page.

### <u>Use Case - Access The News API:</u>
### Actor: User
**View Latest Entertainment News Articles** As a user I want to see the latest entertainment/movie news so that I can stay informed about current events in the entertainment industry.

- The user lands on the Home page or navigates to the Home page on the navbar from another page.
- The application displays a list of the latest entertainment news in the template.
- The user can click on a news article for further information if desired where they will be directed to the original source page of the news story.

### <u>Use Case - View All Forum Posts:</u>
### Actor: User
**View All Posts**: As a user, I want to see all forum posts.

- The user navigates to the Community page by clicking the link in the navigation bar.
- The user sees a paginated list of all posts in the forum.

### <u>Use Case - View All Comments On All Forum Posts:</u>
### Actor: User
**View All Posts**: As a user, I want to see all comments on all forum posts.

- The user navigates to the Community page by clicking the link in the navigation bar.
- The user sees the forum posts list and clicks on a forum post to view it's content.
- The user reads the forum post and it's comments.
<br>
<br>

## 4. Forum CRUD Functionality:
### <u>Use Case - Create A Forum Post:</u>
### Actor: Logged-in User
**Create Post**: As a user, I want to create a new forum post.

- The user navigates to the Community page.
- The user clicks on the "Create New Post" button.
- The user fills in the post form with the title and content.
- The user submits the form.
- The application saves the post and displays displays a success/error/awaiting approval message.

### <u>Use Case - Edit My Own Forum Post:</u>
### Actor: Logged-in User
**Edit Post**: As a user, I want to edit my own forum post.

- The user navigates to their forum post on the Community page (or in their profile settings).
- The user clicks on the "Edit" button.
- The user updates the post content.
- The user submits the form.
- The application saves the updated post and displays a success/error/awaiting approval message.

### <u>Use Case - Delete My Own Forum Post:</u>
### Actor: Logged-in User
**Delete Post**: As a user, I want to delete my own forum post.
 
- The user navigates to their forum post.
- The user clicks on the "Delete" button.
- The user receives an "are you sure message?" and either confirms or rejects the deletion.
- The application remains on the page if rejected or removes the post from the forum list if confirmed and displays a success/error message.

### <u>Use Case - Create A Comment On A Forum Post:</u>
### Actor: Logged-in User
**Create Post**: As a user, I want to create a new comment on a forum post.

- The user navigates to the Community page.
- The user sees the forum posts list and clicks on a forum post to view it's content/comments.
- The user clicks on the "Add a comment:" button.
- The user fills in the post form with the title and content.
- The user submits the form.
- The application saves the post and displays displays a success/error/awaiting approval message.

### <u>Use Case - Edit My Own Comment On A Forum Post:</u>
### Actor: Logged-in User
**Edit Post**: As a user, I want to edit my own comment on a forum post.

- The user navigates to the required forum post (or navigates to their profile settings).
- The user clicks the "Edit" button on their comment.
- The user updates the comment content.
- The user submits the form.
- The application updates the post and displays the edited content and displays a success/error message.

### <u>Use Case - Delete My Own Comment On A Forum Post:</u>
### Actor: Logged-in User
**Delete Post**: As a user, I want to delete my own forum post.

- The user navigates to the required forum post (or navigates to their profile settings).
- The user clicks on the "Delete" button.
- The user receives an "are you sure message?" and either confirms or rejects the deletion.
- The application remains on the page if rejected or removes the post from the forum list if confirmed and displays a success/error message.

### <u>Use Case - Voting System:</u>
### Actor: Logged-in User
**Upvote/Downvote Post**: As a user, I want to upvote or downvote a forum post.

- The user navigates to the forum post they wish to upvote or downvote.
- The user clicks on the "Upvote" or "Downvote" button.
- The application updates the upvote or downvote count for the post.
- The updated counts are displayed to all users viewing the post.
<br>
<br>

## 5. Testing and Deployment Framework 
### <u>Use Case - Testing The App</u>
### Actor: Developer
**Testing**: As a developer, I want to ensure the application works correctly at various levels.

- The developer configures the environment for running tests.
- The developer Develops unit tests for individual components.
- The developer creates integration tests for combined components.
- The developer develops end-to-end tests to simulate user interactions.
- The developer executes performance tests to measure application load handling.
- The developer reviews test outcomes to identify and fix issues.
- The developer improves application performance based on test findings.

### <u>Use Case - Deploying The App</u>
### Actor: Developer
**Deployment**: As a developer, I want to be able to deploy the application to a production environment, i.e. Heroku.

- The developer sets up the production environment (e.g., Heroku).
- The developer adjusts settings for successful deployment.
- The developer deploys the application to the production environment.
- The developer checks that the application runs correctly post-deployment.
- The developer continuouslys monitor the application for any issues.








