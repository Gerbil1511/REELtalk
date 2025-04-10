![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# REELTalk

![responsive devices image](readme_docs/images/reeltalk-responsive-devices.png)

<p align="center">
| <a href="https://reel-talk-app-9059e75acb3d.herokuapp.com/" target="_blank">Live Project</a> |
</p>


## Introduction

ReelTalk is a movie-centric full-stack platform that combines the excitement of discovering new films with the interactive experience of a community forum. It aims to provide users with an engaging comprehensive resource for movie information, discussions, and the latest industry news. This project was developed as part of the High Performance Code Institute Full-Stack Software Development For The AI Augmented Developer Bootcamp and was developed as my final individual Full-Stack Project submission.


## Table Of Contents

* [REELTalk](#ReelTalk)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
* [UX Design Process](#ux-design-process)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton - Wireframes](#skeleton---wireframes)
  - [Surface Design](#surface-design)
* [Agile Methodology](#agile-methodology)
  - [GitHub Project Board](#github-project-board)
  - [GitHub Issues](#github-issues)
  - [MoSCoW](#moscow)
* [Tech](#tech)
  - [Languages](#languages)
  - [Frameworks and Libraries](#libraries-and-frameworks)
  - [Software and Tools](#software-and-tools)
* [Testing](#testing)
  - [Testing](#testing)
  - [Validation](#validation)
* [Deployment](#deployment)
* [AI Reflection](#ai-reflection)
  - [Development Process](#development-process)
  - [Generating Code](#generating-code)
  - [Debugging Code](#debugging-code)
  - [Optimizing Code](#optimizing-code)
  - [Testing Code](#testing-code)
  - [Reflections on AI](#reflections-on-ai)
* [Credits and Acknowledgements](#credits-and-acknowledgements)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## UX Design Process

### *Strategy Plane*
The strategy of the Reeltalk app is to provide a platform where users can easily browse a database of movies, access relevant information, and engage with a community of fellow movie enthusiasts. The app aims to offer a space where users can share their opinions, comment on discussions, and stay updated with the latest entertainment news. The primary goal is to create an engaging and informative experience that encourages interaction while ensuring ease of use for all users.


<details>
  <summary>Click to expand Epics and Milestones details</summary>

## Epics and Milestones

## Target Audience
- Movie enthusiasts who want to explore and discuss movies.
- Users looking for a platform to share their movie reviews and opinions.
- Individuals interested in staying updated with the latest movie news.

## Epics
1. **Admin Management**: Implementing admin features to manage users and content.
2. **User Authentication**: Implementing login, registration, and logout functionality.
3. **Movie Search and Display**: Integrating TMDb API to search and display movies.
4. **Forum Functionality**: Creating a forum for movie discussions using Posts and comments with CRUD capabilities.
5. **Voting System**: Implementing upvote and downvote functionality for forum posts.
6. **News Integration**: Integrating News API to display the latest movie news.
7. **User Profile Management**: Implementing features for users to manage their profiles, including viewing, editing, and customizing their personal information and settings.
8. **Testing and Deployment Framework Implementation**: Establishing a comprehensive testing framework and a streamlined deployment process to ensure the quality and reliability of the application.


## Milestones
1. **Admin Management Milestone**
   - Implement user management (view, edit, delete users)
   - Implement content moderation (edit, delete forum posts/movies)
   - Create admin dashboard

2. **User Authentication Milestone**
   - Complete user registration
   - Complete user login and logout
   - Integration with Django Allauth

3. **Movie Search and Display Milestone**
   - Display Latest Popular and Top Rated movies from Movie Model
   - Implement movie search functionality
   - Create movie detail page

4. **Forum Functionality Milestone**
   - Create forum page to list all posts
   - Add comments to forum Posts
   - Implement CRUD for forum posts/comments
   - Add voting options to forum posts

5. **Voting System Milestone**
   - Implement upvote and downvote functionality
   - Ensure users can only vote once per post

6. **News Integration Milestone**
   - Fetch and display latest movie news from News API

7. **User Profile Management Milestone** 
   - Implement profile view functionality. 
   - Implement profile edit functionality. 
   - Add user profile customization options. 
   - Ensure profile settings are saved and updated correctly. 

8. **Testing and Deployment Milestone**
   - Set up the testing environment. 
   - Implement unit, integration, and end-to-end tests. 
   - Conduct performance testing. 
   - Deployment to production environment.
   - </details>

   <details>
  <summary>Click to expand Use Cases</summary>
  
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
- The developer continuouslys monitor the application for any issues.  </details>
<br>

### *Scope Plane*
The scope of the REEltalk app includes:

**Features:**
- User Authentication: Registration, login, and logout functionality using Django Allauth.
- Movie Search and Display: Integration of a search bar to search and display movies.
- Movie Detail Page: Detailed information about each movie, including title, overview, release date, poster, vote average, and popularity.
- Community Forum: Users can create, edit, delete forum posts related to movies. Users can also create, edit, delete comments related to posts.
- Voting System: Users can upvote or downvote forum posts.
- Latest Movie News: Integration with a News API to display the latest movie news.

**Future Features**
- Ensuring users are able to fully manage their profile including username, password, email, profile image, see a full list of their posts and comments with functionality to edit and delete them.


**Functional Requirements:**
- Secure user authentication and session management.
- Integration with external News API for entertainment news.
- CRUD functionality for forum posts and comments.
- Responsive design for seamless user experience across devices.
<br>

### *Structure Plane*

**Information Architecture:**
- Home Page: Introduction to the platform, latest movie news, and navigation links.
- Movies Page: Search bar and list of movies with options to view details.
- Movie Detail Page: Detailed information about the selected movie and a create a forum post form.
- Community Forum: List of forum posts with options to create new posts and obtain further information on an individual forum post.
- Forum Post Detail Page: Detailed information about the selected forum post and related comments.
- User Profile: User-specific information, including their posts and comments.

**Interaction Design:**
- Navigation: Clear and intuitive navigation menu with links to Home, Movies, Community Forum, and User Authentication. Clearly defined and labeled buttons for navigation around the site.
- Forms: User-friendly forms for registration, login, creating/editing posts, and commenting.
- Feedback: Success and error messages for user actions (e.g., post creation, comment submission).
<br>

ERD DIangram to show relationships between Users, Movie, Community Forum (Posts and Comments)
![Reeltalk App ERD diagram](readme_docs/images/reeltalk_erd.png)

### *Skeleton Plane*

**Wireframes and Mockups:**
- Home Page: Hero section with a call-to-action, latest movie news, and navigation links.
- Movies Page: Search bar at the top, followed by a grid of movie cards with titles, posters, and "More Details" buttons.
- Movie Detail Page: Movie poster, title, overview, release date, and user reviews/comments.
- Community Forum: List of forum posts with titles, authors, votes and comment counts. Buttons for creating new posts and viewing post details and voting.
- Forum Post Detail Page: Movie poster, post author, title, content, timestamp, and user reviews/comments.
- User Profile: User information, list of user's posts and comments, and options to edit/delete posts.

*Mobile Wireframe*
![Mobile Wireframe](readme_docs/images/mobile_wireframe.png)
<br>

*Tablet Wireframe*
![Tablet Wireframe](readme_docs/images/tablet_wireframe.png)
<br>

*Desktop Wireframe*
![Desktop Wireframe](readme_docs/images/desktop_wireframe.png)
<br>

**Layout**
- Header: Logo, navigation menu, and user authentication links (login/logout).
- Main Content: Dynamic content based on the selected page (e.g., movie list, movie details, forum posts, etc).
- Footer: Links to social media, contact information, and copyright notice.

![Mobile navigation](readme_docs/images/mob_nav.png) ![Desktop Navigation](readme_docs/images/desktop_nav.png) ![Footer section](readme_docs/images/Footer.png)
<br>

### *Surface Plane*

**Visual Design:**
- Color Scheme: A cohesive color palette that aligns with the theme of movies and entertainment. Influenced by using applications such as GitPod regularly, I believe I have been subliminally influenced to select the colurs that I did. Apps like Netflix and Letterbod'd use the dark theme to great effect and therefore as an homage to that I opted for the following colour scheme

![Colour scheme](readme_docs/images/colour_chart.png)
<br>

- Typography: Readable and aesthetically pleasing fonts for headings, body text, and buttons.

![Typography](readme_docs/images/font_details.png)
![Typography](readme_docs/images/example_font.png)
<br>

- Imagery: High-quality movie posters, icons, and graphics to enhance the visual appeal.

![Hero image](readme_docs/images/hero.jpg)
![No photo image](readme_docs/images/no_image.webp)
![Reeltalk Logo](static/images/reeltalk_logo.png)
![Favicon](static/images/apple-touch-icon.png)
<br>

- Buttons and Forms: Consistent Bootstrap styling for buttons and forms to ensure a unified look and feel.

![Site Navigation Buttons](readme_docs/images/site_nav_btn.png) ![Search Buttons](readme_docs/images/searchbtn.png) ![Pagination Buttons](readme_docs/images/pagination_buttons.png) ![More Details Buttons](readme_docs/images/movie_detail_btn.png) ![Movie List Carousel Controls](readme_docs/images/carousel_controls.png)
<br>

**Responsive Design:**
- Mobile: Optimized layout for smaller screens with collapsible navigation and touch-friendly elements.
- Tablet: Adaptive design that adjusts the layout for medium-sized screens.
- Desktop: Full-featured layout with ample space for displaying content and navigation.

![Responsive images](readme_docs/images/responsive_image.png) 
<br>

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Agile Methodology

Throughout the development of ReelTalk, I implemented Agile methodology to ensure a flexible and iterative approach to project management. This methodology suits me well as a "planner" and allowed me to adapt to changes quickly, prioritize tasks effectively, and deliver a high-quality product.

**GitHub Issue and User Stories**
I used the MoSCoW prioritization technique to prioritize user stories. This technique categorizes tasks into four groups:

- Must Have: Essential features that are critical to the project's success.
- Should Have: Important features that add significant value but are not critical.
- Could Have: Desirable features that enhance the user experience but are not essential.
- Won't Have: Features that are not planned for this release but may be considered in the future.

I used GitHub issue templates to systematically develop and manage my user stories, ensuring consistency and clarity in task descriptions and acceptance criteria.

<u>Issues Template</u>

![GitHub Issues Template](readme_docs/images/issues_template.png)

<u>User Stories</u>

<details>
  <summary>Click to expand</summary>
  
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
- **User Story 7:** As a user, I want to search for movies so that I can find information about my favourite movies. 
  - **Acceptance Criteria:**
    - Users can see the latest popular and top rated movies on the Movie page.
    - Users can search for specific movies.
    - Users can view detailed information about a movie.
    - **Tasks:**
    - Utilise the TMDb API to add records to the Movie model database.
    - Create a view to display the latest popular and top rated movies.
    - Implement search functionality, and ensure it displays appropriate results.
    - Design movie detail page that displays movie information.
   

## Forum Functionality - Forum Posts
- **User Story 8:** As a Logged-in user, I want to create, edit, and delete my forum posts so that I can share my thoughts and engage with the community.
  - **Acceptance Criteria:**
    - Users can view all forum posts.
    - Logged-in Users can create new forum posts.
    - Logged-in Users can edit their own posts.
    - Logged-in Users can delete their own posts.
  - **Tasks:**
    - Set up ForumPost models for forum posts.
    - Create views for listing, creating, editing, and deleting posts.
    - Design forms for creating and editing posts using 'Crispy Forms'.
    - Implement permissions to allow users to edit/delete their own posts only.
    - Add URL routing for the forum post submission.


## Forum Functionality - Comments
- **User Story 9:** I want to comment on an existing movie forum post so that I can share my thoughts and create/engage in discussions.
  - **Acceptance Criteria:**
    - Users can see comments associated with each forum post in the forum post detail page.
    - Logged-in Users can submit a comment using the form. The comment is saved and will be displayed under the forum post detail.
    - Logged-in Users can edit their own comments in the forum post detail page.
    - Logged-in Users can delete their own comments from the forum post detail page.
  - **Tasks:**
    - Set up PostComment model for forum posts and comments.
    - Create a view to handle comment submission and save the comment to the database.
    - Update the forum post detail template to display ist of comments and the comment form using 'Crispy Forms'.
    - Implement permissions to allow users to edit/delete their own posts/comments only.
    - Display the number of comments on the forum post in the forum post list page.
    - Add URL routing for the comment submission.


## Voting System
- **User Story 10:** As a Logged-in user, I want to upvote or downvote posts so that I can express my opinion on forum posts.
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
- **User Story 11:** As a user, I want to see success and error messages so that I know the result of my actions.
  - **Acceptance Criteria:**
    - Success and error messages are displayed for user actions.
  - **Tasks:** 
    - Implement Django's messaging framework.
    - Add success and error messages to views for creating, editing, and deleting posts/comments, editing/deleting user profile or sign up/login/logout.s and for upvoting/downvoting.
    - Display messages in the templates.


## Latest Entertainment/Movie News
- **User Story 12:** As a user, I want to view the latest entertainment/movie news so that I can stay informed about current events in the entertainment industry.
  - **Acceptance Criteria:**
    - Users can see the latest entertainment/movie news from various worldwide sources.
  - **Tasks:**
    - Integrate News API.
    - Create a view to display the latest news.
    - Design a latest news section on the home page with pagination.


## Testing and Deployment Framework
- **User Story 13:** As a developer, I want to set up a comprehensive testing environment and deploy the application to a production environment so that I can ensure the application works correctly at various levels and is accessible to users.
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

</details>
<br>
<br>

<u>MoSCoW Prioritization</u>

![MoSCoW prioritization](readme_docs/images/moscow.png)
![MoSCoW prioritization](readme_docs/images/wont_have.png)


**GitHub Project Boards**
I utilized GitHub Project Boards so that I could visually manage and track the progress of my tasks. The board was divided into columns representing different stages of the workflow, such as "Backlog", "To Do," "In Progress," and "Done." This setup provided a clear overview of the project's status and helped me to stay organized and to manage the development of REELtalk effectively.

![GitHub Project Board](readme_docs/images/project_board.png)

**Sprints**
Although I did not officially utilize sprints, I followed the concept of breaking my project into blocks over the three week schedule. This included developing the ERD, initializing the project, getting the MVP done by the first week and a half, then focusing on back-end functionality such as API development and AllAuth setup. Following this, I moved on to front-end development, and finally, testing and documentation.


<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Tech
Throughout the development of REELtalk I utilised the following:

## Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Frameworks & Libraries
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![Django Allauth](https://img.shields.io/badge/Django%20Allauth-092E20?style=for-the-badge&logo=django&logoColor=white)
![Crispy Forms](https://img.shields.io/badge/Crispy%20Forms-00A3E0?style=for-the-badge&logo=django&logoColor=white)
![Summernote](https://img.shields.io/badge/Summernote-000000?style=for-the-badge&logo=summernote&logoColor=white)
![Font Awesome](https://img.shields.io/badge/Font%20Awesome-339AF0?style=for-the-badge&logo=font-awesome&logoColor=white)

## Software & Tools
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![TMDb API](https://img.shields.io/badge/TMDb-01D277?style=for-the-badge&logo=themoviedatabase&logoColor=white)
![News API](https://img.shields.io/badge/News%20API-000000?style=for-the-badge&logo=news&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Whitenoise](https://img.shields.io/badge/Whitenoise-000000?style=for-the-badge&logo=whitenoise&logoColor=white)
![Microsoft Copilot](https://img.shields.io/badge/Microsoft%20Copilot-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Balsamiq](https://img.shields.io/badge/Balsamiq-000000?style=for-the-badge&logo=balsamiq&logoColor=white)
![Lucidchart](https://img.shields.io/badge/Lucidchart-F28D1A?style=for-the-badge&logo=lucidchart&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-00A67E?style=for-the-badge&logo=openai&logoColor=white)
![CDN Fonts](https://img.shields.io/badge/CDN%20Fonts-000000?style=for-the-badge&logo=google-fonts&logoColor=white)


<p align="right"><a href="#REELtalk">Back To Top</a></p>

### Testing
I tested the app using the following test cases:

### Forum App Test Cases

#### Forms

- **TestForumPostForm**: Tests for the `ForumPostForm`.
  - `test_form_is_valid`: Ensures the form is valid with correct data.
  - `test_form_is_invalid_without_title`: Ensures the form is invalid without a title.
  - `test_form_is_invalid_without_content`: Ensures the form is invalid without content.

- **TestPostCommentForm**: Tests for the `PostCommentForm`.
  - `test_form_is_valid`: Ensures the form is valid with correct data.
  - `test_form_is_invalid_without_comment`: Ensures the form is invalid without a comment.

#### Views

The `forum/tests/test_views.py` file contains test cases for the views in the `forum` app. It ensures that the views render the correct templates and handle data correctly.

- **TestForumViews**: Tests for the forum views.
  - `test_forum_post_list_view`: Ensures the `forum_post_list` view renders correctly.
  - `test_forum_post_detail_view`: Ensures the `forum_post_detail` view renders correctly.
  - `test_create_post_view`: Ensures the `create_post` view handles post creation correctly.
  - `test_edit_post_view`: Ensures the `edit_post` view handles post editing correctly.
  - `test_delete_post_view`: Ensures the `delete_post` view handles post deletion correctly.

### Movies App Test Cases

#### Forms

The `movies/tests/test_forms.py` file contains test cases for the forms in the `movies` app. It ensures that the forms are validated correctly with both valid and invalid data.

- **TestMovieForm**: Tests for the `MovieForm`.
  - `test_form_is_valid`: Ensures the form is valid with correct data.
  - `test_form_is_invalid`: Ensures the form is invalid with missing required fields.
  - `test_form_is_invalid_without_title`: Ensures the form is invalid without a title.
  - `test_form_is_invalid_without_content`: Ensures the form is invalid without content.


#### Views

The `movies/tests/test_views.py` file contains test cases for the views in the `movies` app. It ensures that the views render the correct templates and handle data correctly.

- **TestMovieViews**: Tests for the movie views.
  - `test_list_movies_view`: Ensures the `list_movies` view renders correctly.
  - `test_movie_detail_view`: Ensures the `movie_detail` view renders correctly.
  - `test_movie_detail_view_post`: Ensures the `movie_detail` view handles post creation correctly.


  ### Test Results

| Test Case                         | Test Method                          | Description                                           | Result  |
|-----------------------------------|--------------------------------------|-------------------------------------------------------|---------|
| **TestForumPostForm**             | `test_form_is_valid`                 | Ensures the form is valid with correct data.          | Passed  |
|                                   | `test_form_is_invalid_without_title` | Ensures the form is invalid without a title.          | Passed  |
|                                   | `test_form_is_invalid_without_content`| Ensures the form is invalid without content.          | Passed  |
| **TestPostCommentForm**           | `test_form_is_valid`                 | Ensures the form is valid with correct data.          | Passed  |
|                                   | `test_form_is_invalid_without_comment`| Ensures the form is invalid without a comment.        | Passed  |
| **TestForumViews**                | `test_forum_post_list_view`          | Ensures the `forum_post_list` view renders correctly. | Passed  |
|                                   | `test_forum_post_detail_view`        | Ensures the `forum_post_detail` view renders correctly.| Passed  |
|                                   | `test_create_post_view`              | Ensures the `create_post` view handles post creation correctly.| Passed  |
|                                   | `test_edit_post_view`                | Ensures the `edit_post` view handles post editing correctly.| Passed  |
|                                   | `test_delete_post_view`              | Ensures the `delete_post` view handles post deletion correctly.| Passed  |
| **TestMovieForm**                 | `test_form_is_valid`                 | Ensures the form is valid with correct data.          | Passed  |
|                                   | `test_form_is_invalid`               | Ensures the form is invalid with missing required fields.| Passed  |
|                                   | `test_form_is_invalid_without_title` | Ensures the form is invalid without a title.          | Passed  |
|                                   | `test_form_is_invalid_without_content`| Ensures the form is invalid without content.          | Passed  |
| **TestMovieViews**                | `test_list_movies_view`              | Ensures the `list_movies` view renders correctly.     | Passed  |
|                                   | `test_movie_detail_view`             | Ensures the `movie_detail` view renders correctly.    | Passed  |
|                                   | `test_movie_detail_view_post`        | Ensures the `movie_detail` view handles post creation correctly.| Passed  |


**Reflections on AI**
The use of AI tools in the testing process has significantly boosted my efficiency and effectiveness. As a newcomer to testing applications I made use of AI to generate test cases, create test skeletons, and identify edge cases, I ensured comprehensive test coverage and robust functionality. This AI-driven approach allowed me to focus on refining my application and delivering a high-quality product.
<br>


### Validation
To ensure the highest quality and accessibility of ReelTalk, I used the following validation tools throughout the development process.

 **Lighthouse**
 I used Lighthouse to audit the performance, accessibility, best practices, and SEO of the web application. Some of the issues identified related to optimizing images to improving load times however as the images were being pulled in from an API , I had not control over this aspect.

 <u>Mobile Score</u>

 ![Lighthouse validation score - mobile](readme_docs/images/lighthouse_mobile.png)

 <u>Desktop Score</u>

  ![Lighthouse validation score - mobile](readme_docs/images/lighthouse_desktop.png)
 
 <br>

 **WAVE Accessibility**
 I used this tool to identify and fix accessibility issues, ensuring that the application is usable by individuals with disabilities. Although the score indicated no errors, there were some areas of concern in low contrast errors relating to the buttons used throughout the site and alerts related to text and suspicious links, however these were related to the News API content which I have no control over.

 ![WAVE Accessibility score - mobile](readme_docs/images/wave_score.png)
 
 <br>
 
 **The WebAIM and WCAG Contrast Checkers**
 I used these tools to verify that the color contrast between text and background met the WCAG guidelines, ensuring readability for users with visual impairments. Although there was some issues with colour contrast for small text, the two main colours used throughout the application passed.

![WebAIM contrast score](readme_docs/images/web_aim_score.png)![WCAG contrast score](readme_docs/images/wcag_contrast-check.png)

<br>
  
 **W3C HTML and CSS validators**
 These were used to check for any markup and styling errors, ensuring that the code adhered to web standards. 

 <u>HTML</u>
 I utilised the text input format initially however it was not accepting the Django Template Language and returned them as errors, however on validating via the application address, the result was that no errors were found.

 ![W3C HTML validation](readme_docs/images/html1_validation.png)
 ![W3C HTML validation](readme_docs/images/html2_validation.png)

 <u>CSS</u>
 No errors were found.

![W3C CSS validation](readme_docs/images/css_test_validation.png)
 
 <br>

 **JSHint**
 JSHint showed one warning and one undefined variable but no other errors.

![JSHint validation](readme_docs/images/JSHint.png)

**Python Linter from Code Institute**
- (https://pep8ci.herokuapp.com/) Used the linter to ensure that all codes meet PEP8 guidelines.
 
I would like to address these issues during further development to ensure that ReelTalk is not only performant and visually appealing but also as fully accessible and standards-compliant as possible.

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Deployment

#### Prerequisites

1. **Heroku Account:** Ensure you have a Heroku account. If not, sign up at [Heroku](https://signup.heroku.com/).
2. **Heroku CLI:** Install the Heroku CLI from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
3. **Git:** Ensure Git is installed on your local machine. If not, download and install it from [Git](https://git-scm.com/).

#### Step-by-Step Deployment

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/reeltalk.git
   cd reeltalk
   ```

2. **Create a Virtual Environment and Install Dependencies:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create a Heroku App:**
   ```sh
   heroku create reeltalk-app-name
   ```

4. **Set Up Environment Variables:**
   Set the necessary environment variables on Heroku. You can do this via the Heroku dashboard or using the Heroku CLI.
   ```sh
   heroku config:set SECRET_KEY='your_secret_key'
   heroku config:set TMDB_API_KEY='your_tmdb_api_key'
   heroku config:set NEWS_API_KEY='your_news_api_key'
   heroku config:set CLOUDINARY_URL='your_cloudinary_url'
   ```

5. **Add Heroku Postgres Add-on:**
   ```sh
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. **Configure Django Settings for Heroku:**
   Ensure your `settings.py` is configured to use the database URL provided by Heroku and to serve static files using Whitenoise.
   ```python
   import dj_database_url

   DATABASES = {
       'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
   }

   # Static files (CSS, JavaScript, Images)
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

   # Whitenoise configuration
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',
       # ... other middleware ...
   ]

   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

7. Ensure DEBUG Mode is Turned Off: In your settings.py, ensure that DEBUG mode is turned off for the deployed application.
   ```python
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   ```
   Set the DEBUG environment variable on Heroku to False:
   ```python
   heroku config:set DEBUG=False
   ```

8. **Create a Procfile:**
   Create a Procfile in the root directory of your project to specify the commands that are executed by the app on startup.
   ```Procfile
   web: gunicorn reeltalk.wsgi
   ```

9. **Commit Changes and Push to Heroku:**
   ```sh
   git add .
   git commit -m "Prepare for Heroku deployment"
   git push heroku main
   ```

10. **Run Migrations:**
    ```sh
    heroku run python manage.py migrate
    ```

11. **Create a Superuser:**
    ```sh
    heroku run python manage.py createsuperuser
    ```

12. **Collect Static Files:**
    ```sh
    heroku run python manage.py collectstatic
    ```

13. **Open the App:**
    ```sh
    heroku open
    ```

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## AI Reflection

### Development Process
During the development of ReelTalk, AI tools have been instrumental in boosting my efficiency and productivity. Utilizing AI allowed me to streamline different aspects of the development process, from code generation to debugging and optimization. This integration enabled me to work more effectively, minimize manual labor, and focus on delivering a top-notch application.

To generate the user stories for my project, AI helped me establish a structured process to identify the needs and objectives of various stakeholders, including administrators and users. I crafted my prompts specifically for user stories in a format that clearly expressed the desired outcomes and motivations: "As a ..., I want to..., so that I can..." and asked for these requirements to be turned into acceptance criteria and tasks. This approach ensured that each story was centered around the user and aligned with the overall project goals.

As I progressed through the user stories, I refined my prompts as needed to maintain clarity and specificity. This iterative process allowed me to pinpoint the exact requirements and steps necessary to achieve my UX design objectives and Agile goals, resulting in detailed and actionable user stories. By refining my prompts, I was able to better capture the unique needs of each user and keep the development process focused and aligned with the desired outcomes.

This comprehensive and systematic method enabled me to create a detailed roadmap for developing the movie app. It ensured the app was engaging, efficient, and catered to the needs of the users.
<br>

### Generating Code
AI tools like GitHub Copilot were invaluable in generating code for this project. With its intelligent code suggestions and auto-completions, it felt like having a knowledgeable assistant by my side. When I tackled the search and API system, Copilot provided relevant code snippets for various functionalities, including smooth, dynamic interactions with a focus on DOM manipulation. This significantly reduced the time required for manual coding.

As someone who's relatively new to Python and Django, these tools were like having a personal mentor on standby. They guided me through the complexities with handy code examples and best practices. This support was crucial in helping me overcome challenges and build a high-quality application efficiently.

However, the journey wasn't always smooth. There were times when AI didn't respond to my refined prompts as expected, which led to frustration. In those moments, I had to turn to other sources for help, including online resources, my facilitator, and course coding experts. Their advice and support were invaluable in navigating these obstacles and ensuring the project's success.

Thanks to the combination of AI tools and expert guidance, I could focus on delivering a top-notch user experience without getting bogged down by the intricacies of new technologies.


<br>

### Debugging Code
AI tools was also invaluable in debugging my code. Throughout the development process, I utilized AI to continuously analyze various aspects of my code, identify potential issues, and provide suggestions for resolving them. This included detecting syntax errors, reference errors, and type errors, as well as optimizing code performance. For example, AI-driven insights helped me fine-tune my Django views and models, resulting in a more efficient and error-free application.

<br>

### Optimizing Code
The role of AI in optimizing my code cannot be overstated. AI tools provided recommendations for improving code performance and enhancing the user experience. By analyzing my codebase, AI identified areas where optimizations could be made, such as reducing redundant operations, improving database queries, and enhancing the responsiveness of the user interface. These optimizations contributed to a smoother and more efficient application.


<br>

### Testing Code
As stated previouslyAI tools also played a crucial role in testing my code. I used AI to generate automated unit tests for key functionalities, ensuring comprehensive test coverage. By leveraging AI, I was able to quickly create test cases for various components. This automated testing approach allowed me to identify and address issues early in the development process, resulting in a more robust and reliable application.


<br>

### Reflections on AI
On reflection, the integration of AI into my project development process has brought about a paradigm shift. AI tools has enabled me to speed up my workflow, work smarter, and more efficiently by automating mundane tasks, providing intelligent code suggestions, and offering real-time debugging and optimization. The strategic use of AI allowed me to deliver a polished and high-quality application that meets the needs of my users. Overall, AI tools have significantly impacted my development process, enhancing my productivity and ensuring the success of the ReelTalk project.
<br>

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Credits and Acknowledgements


### README

- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [README file generator/editor](https://www.readme.so)
- [Code Institute readme tutorial ](https://www.youtube.com/watch?si=YlDWOkkzvTBjbgs3&v=l1DE7L-4eKQ&feature=youtu.be)
- [README.md example](https://github.com/TheRickyroy/astronauts-for-autism/blob/main/README.md#tools-and-programs)
- [Badges](https://github.com/Ileriayo/markdown-badges)
<br>

### FONTS

- CDN Fonts 
[Inclusive Sans 2 font](https://www.cdnfonts.com/inclusive-sans-2.font) 
[Olivia King Designer](https://www.oliviaking.com/)
<br>

### IMAGERY

- Hero image - (https://wallpapercave.com/w/wp10615935) by [Tramon1](https://wallpapercave.com/u/tramon1)
- REELtalk logo and Favicon - [Luke Beck](https://lukebeck.substack.com) - My wonderful son!
- No poster image - [Image by Gerd Altmann/geralt from Pixabay](https://pixabay.com/users/geralt-9301/)
- Movie Posters/News article Images - Supplied through the TMDB API and NEWS API
<br>

### RESPONSIVE DEVICE IMAGES

- [Am I Responsive](https://ui.dev/amiresponsive)
<br>

### Acknowledgements

 - A huge thank you to Dillon, Mark, Roo, and John and everyone at Code Institute for their support and help, I truly appreciate it!

 - Special thanks go out to all my cohort on the Bootcamp as, you are all amazing and talented and supportive and I definitely am grateful I met you all!
 
 - Super special thanks go to Joanna, Amanda, Maebh and Maja - you are all absolute legends!

 - And to my family and friends who tested my deployments and gave great feeback, love you all, thank you so much!


<p align="right"><a href="#REELtalk">Back To Top</a></p>
