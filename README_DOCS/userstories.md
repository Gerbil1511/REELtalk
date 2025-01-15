# User Stories

## Admin Management
- **User Story 1:** As an admin, I want to access an admin dashboard through Django’s built-in admin interface so that I can manage the app efficiently. 
  - **Acceptance Criteria**: 
    - Admins can log in to the Django admin dashboard. 
    - Admins can navigate between different management sections (users, forum posts, etc.). 
    - Admins have access to all necessary management tools from the admin dashboard. 
  - **Tasks**: 
    - Set up the Django admin interface. 
    - Ensure all relevant models (users, forum posts, movies etc.) are registered with the admin. 
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
    
- **User Story 3:** : As an admin, I want to moderate forum posts using the Django admin dashboard so that I can ensure content quality and adherence to community guidelines. 
  - **Acceptance Criteria**: 
    - Admins can view all forum posts in the Django admin dashboard. 
    - Admins can edit forum posts from the admin dashboard. 
    - Admins can delete forum posts from the admin dashboard. 
  - **Tasks**: 
    - Register the ForumPost model with the Django admin. 
    - Customize the admin interface for forum post management. 
    - Implement filtering and search functionality in the admin dashboard for forum posts.

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


## Movie Search and Display
- **User Story 6:** As a user, I want to search for movies so that I can find information about my favorite movies. Once I select a movie I can also see the forum posts associated with it as well as movie details.
  - **Acceptance Criteria:**
    - Users can see the top 20 movies on the home page.
    - Users can search for specific movies.
    - Users can view detailed information about a movie.
    - Users can see all forum posts relating to the particular movie
  - **Tasks:**
    - Integrate TMDb API.
    - Create a view to display the top 20 movies.
    - Implement search functionality.
    - Design movie detail page that displays movie information and lists all forum posts related to it.
    - Fetch movie details from TMDb API.


## Forum Functionality
- **User Story 7:** As a user, I want to create, edit, and delete my forum posts so that I can share my thoughts and engage with the community.
  - **Acceptance Criteria:**
    - Users can view all forum posts.
    - Users can create new forum posts.
    - Users can edit their own posts.
    - Users can delete their own posts.
  - **Tasks:**
    - Set up database models for forum posts.
    - Create views for listing, creating, editing, and deleting posts.
    - Design forms for creating and editing posts using 'Crispy Forms'.
    - Implement permissions to allow users to edit/delete their own posts only.


## Voting System
- **User Story 8:** As a user, I want to upvote or downvote posts so that I can express my opinion on forum posts.
  - **Acceptance Criteria**
    - Users can upvote a post.
    - Users can downvote a post.
    - Users can vote only once per post.
  - **Tasks**
    - Add vote fields to the forum post model.
    - Create views and buttons for upvoting and downvoting.
    - Implement logic to ensure users can vote only once per post.
    - Display the number of upvotes and downvotes in the templates.


## Success and Error Messages
- **User Story9:** As a user, I want to see success and error messages so that I know the result of my actions.
  - **Acceptance Criteria:**
    - Success and error messages are displayed for actions such as creating, editing, and deleting posts.
  - **Tasks:** 
    - Implement Django's messaging framework.
    - Add success and error messages to views for creating, editing, deleting posts and for upvoting/downvoting.
    - Display messages in the templates.

## News Integration
- **User Story 10:** As a user, I want to view the latest entertainment/movie news so that I can stay informed about current events in the entertainment industry.
  - **Acceptance Criteria:**
    - Users can see the latest entertainment/movie news from various worldwide sources.
  - **Tasks:**
    - Integrate News API.
    - Create a view to display the latest news.
    - Design a latest news section on the home page with pagination.

## User Profile Management
- **User Story 11:** As a user, I want to view and edit my profile so that I can keep my personal information up to date and customize my profile settings. 
  - **Acceptance Criteria:** 
    - Users can view their profile information. 
    - Users can edit their profile information. 
    - Users can save changes to their profile. 
    - Customized profile settings are saved and reflected immediately. 
  - **Tasks:** 
    - Create a view for displaying user profile information. 
    - Design and implement forms for editing profile information. 
    - Ensure form validation and error handling. 
    - Implement backend logic to update user profile information in the database. 
    - Test the profile view and edit functionality to ensure it works correctly.

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