# User Stories

## Admin Management
- **User Story 1:** As an admin, I want to access an admin dashboard through Django’s built-in admin interface so that I can manage the app efficiently. 
  - **Acceptance Criteria**: 
    - Admins can log in to the Django admin dashboard. 
    - Admins can navigate between different management sections (users, forum posts, etc.). 
    - Admins have access to all necessary management tools from the admin dashboard. 
  - **Tasks**: 
    - Set up the Django admin interface. 
    - Ensure all relevant models (users, forum posts, comments, movies) are registered with the admin. 
    - Customize the dashboard layout for ease of use.
   
- **User Story 2:** As an admin, I want to view, edit, and delete users via the Django admin dashboard so that I can manage user accounts efficiently.
  - **Acceptance Criteria**: 
    - Admins can access the Django admin dashboard. 
    - Admins can view a list of all users. 
    - Admins can edit user details from the admin dashboard. 
    - Admins can delete users from the admin dashboard. 
  - **Tasks**: 
    - Configure the Django admin site. 
    - Register the User model with the Django admin. 
    - Customize the admin interface for user management.
    
- **User Story 3:** : As an admin, I want to moderate forum posts and comments using the Django admin dashboard so that I can ensure content quality and adherence to community guidelines. 
  - **Acceptance Criteria**: 
    - Admins can view all forum posts and comments in the Django admin dashboard. 
    - Admins can edit forum posts and comments from the admin dashboard. 
    - Admins can delete forum posts and comments from the admin dashboard. 
  - **Tasks**: 
    - Register the ForumPost and PostComment model with the Django admin. 
    - Customize the admin interface for forum post/comment management. 
    - Implement filtering and search functionality in the admin dashboard for forum posts/comments.

- **User Story 4:** As an admin, I want to manage movies through the Django admin interface so that I can easily add and delete movie records. 
  - **Acceptance Criteria**: 
    - Admins can add new movie records. 
    - Admins can delete movie records. 
  - **Tasks**: 
    - Register the Movie model with the Django admin. 
    - Customize the admin interface for movie management. 
    - Test the movie management functionality in the admin dashboard.  


## User Authentication
- **User Story 5:** As a user, I want to register, log in, and log out of the app so that I can access my account securely.
  - **Acceptance Criteria:**
    - Users can register for an account.
    - Users can log in with their credentials.
    - Users can log out securely.
  - **Tasks:**
    - Set up Django Allauth.
    - Create registration, login, and logout views.
    - Design user registration and login forms using 'Crispy Forms'.
    - Implement session management for user authentication.
    - Add URL routing for the registration, login and logout pages.
    - Test the registration, login and logout processes to ensure users can sign up, login and logout. i.e., ensure that the registration and login options are available to all site visitors and that the logout option is visible to logged in users only.


## User Profile Management
-- **User Story 6:** As a Logged-in user, I want to view and edit my profile so that I can keep my personal information up to date and customise my profile settings.
  - **Acceptance Criteria:**
    - The user can access their profile page by clicking on the "Profile" or "My Account" link/button.
    - The profile page displays the user's name, email, bio, profile picture, and a list of created posts/comments.
    - The user can access the edit profile form by clicking on the "Edit Profile" button.
    - The edit profile form allows the user to update their name, email, bio, and profile picture.
    - The user can submit the form to save changes.
    - The application displays a success message if the profile is updated successfully.
    - The application displays an error message if the profile update fails.
    - The user can access the delete profile option by clicking on the "Delete Profile" button.
    - The application asks for confirmation before deleting the profile.
    - The user confirms the deletion.
    - The application deletes the user's profile and all associated data.
    - The application displays a success message if the profile is deleted successfully.
    - The user is redirected to the home page after successful profile deletion.
  - **Tasks:**
    - Add a link/button in the navigation menu to access the profile page.
    - Create a profile page template view to fetch and display the user's profile information.
    - Implement a view to handle the submissions to update/delete the user's profile.
    - Design an edit profile form template using 'Crispy Forms' and add validation for the form fields.
    - Display success/error messages based on the form submission result.
    - Create a delete profile confirmation dialog.
    - Implement a view to handle profile deletion.
    - Ensure that all associated data (posts/comments) are deleted.
    - Display success/error messages based on the deletion result.
    - Redirect the user to the home page after successful deletion.


## Movie Search and Display
- **User Story 7:** As a user, I want to search for movies so that I can find information about my favorite movies. 
  - **Acceptance Criteria:**
    - Users can see the latest popular and top rated movies on the Movie page.
    - Users can search for specific movies.
    - Users can view detailed information about a movie.
    - **Tasks:**
    - Utilise the TMDb API to add records to the Movie model database.
    - Create a view to display the latest popular and top rated movies.
    - Implement search functionality.
    - Design movie detail page that displays movie information.
   

## Forum Functionality
- **User Story 8:** As a Logged-in user, I want to create, edit, and delete my forum posts and comments so that I can share my thoughts and engage with the community.
  - **Acceptance Criteria:**
    - Users can view all forum posts/comments.
    - Logged-in Users can create new forum posts/comments.
    - Logged-in Users can edit their own posts/comments.
    - Logged-in Users can delete their own posts/comments.
  - **Tasks:**
    - Set up ForumPost and PostComment models for forum posts and comments.
    - Create views for listing, creating, editing, and deleting posts/comments.
    - Design forms for creating and editing posts/comments using 'Crispy Forms'.
    - Implement permissions to allow users to edit/delete their own posts/comments only.
    _ Display the number of comments on the forum post in the forum post list page.


## Voting System
- **User Story 9:** As a Logged-in user, I want to upvote or downvote posts so that I can express my opinion on forum posts.
  - **Acceptance Criteria**
    - Logged-in Users can upvote a post.
    - Logged-in Users can downvote a post.
    - Logged-in Users can vote only once per post.
  - **Tasks**
    - Add vote fields to the ForumPost model.
    - Create views and buttons for upvoting and downvoting.
    - Implement logic to ensure logged-in users can vote only once per post.
    - Display the number of upvotes and downvotes in the templates.


## Success and Error Messages
- **User Story 10:** As a user, I want to see success and error messages so that I know the result of my actions.
  - **Acceptance Criteria:**
    - Success and error messages are displayed for user actions.
  - **Tasks:** 
    - Implement Django's messaging framework.
    - Add success and error messages to views for creating, editing, and deleting posts/comments, editing/deleting user profile or sign up/login/logout.s and for upvoting/downvoting.
    - Display messages in the templates.

## Latest Entertainment/Movie News
- **User Story 11:** As a user, I want to view the latest entertainment/movie news so that I can stay informed about current events in the entertainment industry.
  - **Acceptance Criteria:**
    - Users can see the latest entertainment/movie news from various worldwide sources.
  - **Tasks:**
    - Integrate News API.
    - Create a view to display the latest news.
    - Design a latest news section on the home page with pagination.


## Testing and Deployment Framework
- **User Story 12:** As a developer, I want to set up a comprehensive testing environment and deploy the application to a production environment so that I can ensure the application works correctly at various levels and is accessible to users.
  - **Acceptance Criteria:**
    - A testing environment is set up. 
    - Unit, integration, and end-to-end tests are implemented. 
    - Performance tests are conducted and results are recorded. 
    - The application is successfully deployed to the production environment (e.g., Heroku). 
    - All necessary deployment configurations are in place. 
    - Deployment is verified to ensure the application is running correctly
  - **Tasks:**
    - Set up the testing environment. 
    - Write unit, integration, and end-to-end tests. 
    - Set up and execute performance tests. 
    - Analyze performance test results and optimize the application. 
    - Prepare the deployment environment and configure deployment settings. 
    - Deploy the application to the production environment and verify deployment.