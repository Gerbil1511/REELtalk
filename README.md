![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# REELTalk

<img src="readmedocs/" alt="live site image" width="40%" height="40%">

<p>
| <a href="https://gerbil1511.github.io/ReelTalk/" target="_blank">Live Project</a> |
</p>


## Introduction

ReelTalk is a movie-centric full-stack platform that combines the excitement of discovering new films with the interactive experience of a community forum. It aims to provide users with an engaging comprehensive resource for movie information, discussions, and the latest industry news. This project was developed as part of the High Performance Code Institute Full-Stack Software Development For The AI Augmented Developer Bootcamp and was developed as my final individual Full-Stack Project submission.

## Author

- [Geraldine Edwards](https://www.github.com/Gerbil1511)



## Table Of Contents

* [REELTalk](#ReelTalk)
  - [Introduction](#introduction)
  - [Authors](#author)
  - [Table of Contents](#table-of-contents)
  - [Project Ouline](#project-outline)
* [Project Planning](#project-planning)
  - [UX Design](#ux-design)
  - [User Stories](#user-stories)
  - [Fonts](#fonts)
  - [Images](#images)
  - [Colours](#colours)
  - [Wireframes](#wireframes)
* [Features](#features)
  - [Navigation](#navigation)
  - [Game Board](#game-board)
  - [Game Cards](#game-cards)
  - [Buttons](#buttons)
  - [Inputs](#inputs)
  - [Scores](#scores)
  - [Footer](#footer)
  - [Responsive Design](#responsive-design)
  - [Future Features](#future-features)
* [Agile Methodology](#agile-methodology)
* [Tech](#tech)
  - [Languages](#languages)
  - [Frameworks and Libraries](#libraries-and-frameworks)
  - [Software and Tools](#software-and-tools)
* [AI Tools](#ai-tools)
  - [Development Process](#development-process)
  - [Generating Code](#generating-code)
  - [Debugging Code](#debugging-code)
  - [Reflections on AI](#reflections-on-ai)
* [Deployment](#deployment)
* [Testing](#testing)
  - [Bug Log](#bug-log)
  - [Validation](#validation)
* [Credits and Acknowledgements](#credits-and-acknowledgements)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## PROJECT OUTLINE
Welcome to 'ReelTalk' an interactive, Full-Stack Web application designed for movie enthusiasts.

The idea for this project stems from being one of a family of passionate movie lovers and from the desire to create a dynamic, interactive platform where users can explore and discuss their favorite films (far better than having arguments with family members over differing opinions—no more debates about which Star Wars movie is the best!). 

Inspired by platforms like Letterboxd, the forum aspect of the application allows users to create and manage discussions about movies. Whether it's sharing reviews, debating plot twists, or recommending hidden gems, the forum provides a space for movie enthusiasts to connect and engage with each other. This community-driven feature is designed to promote interaction and create a vibrant online community of movie lovers.

Leveraging Django's robust framework, this project aims to deliver a comprehensive application that encapsulates CRUD (Create, Read, Update, Delete) functionality and custom models.

The application integrates with The Movie Database (TMDb) to provide users with an extensive database of movie information. Users can search for movies, view detailed information, and stay updated with the latest movie news. This feature not only enhances the user experience but also fosters a deeper connection with the world of cinema. It also has a dedicated section for the latest movie news keeps users informed about industry updates, new releases, and film events. By aggregating news from various sources, the application ensures that users have access to the most relevant and up-to-date information.

By combining these elements, the project aims to offer a rich and engaging experience for users, highlighting the importance of both individual exploration and community interaction. Through this application, users can not only discover new movies but also share their insights and connect with like-minded individuals.


<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## PROJECT PLANNING

### UX Design

ReelTalk is designed with the user experience at its core, ensuring accessibility, responsiveness, and visual appeal. The interface adheres to WCAG guidelines, making the application usable for individuals with varying abilities. Extensive research on existing forums provided valuable insights into user expectations, shaping the app's features and functionalities. The design process began with detailed wireframes and mockups, serving as blueprints for the final layout, ensuring all elements are logically placed and aesthetically pleasing.

The responsive design of ReelTalk ensures a seamless experience across various devices, from desktops to mobile phones, using CSS media queries, Flexbox, Grid, and Bootstrap. A cohesive design language is maintained across the application, utilizing a consistent color scheme, typography, and component styles. Clear and intuitive navigation guides users effortlessly through the app, while interactive elements like forms and buttons enhance user interaction.

User-centric features, such as movie ratings, comments, and real-time notifications, enrich the user experience and foster engagement. Forms are designed with validation logic to ensure accurate user input, providing immediate feedback messages for errors or successful submissions. This enhances usability and ensures a smooth interaction for users. By focusing on accessibility, responsiveness, consistency, usability, and thorough research, ReelTalk offers a delightful and inclusive environment for all movie enthusiasts.
<br>
 
### User Stories

User stories are short, simple descriptions of a feature from the perspective of the end-user or stakeholder. They help to define the desired outcomes and provide a clear understanding of the user's needs and goals. In our project, user stories guided the development process, ensuring that each feature was designed with the user in mind.


| User Role  | User Story |
|------------|------------|
| As a player | I want a clear and easy-to-understand game structure so that I can focus on learning rather than figuring out how to play. |
| As a student | I want the game to be responsive so that I can study on different devices like my phone, tablet, or computer. |
| As a teacher | I want the design to be visually appealing and engaging so that it attracts and retains students' interest. |
| As a player | I want a shuffle function for the cards so that I am learning definitions and not just memorising card locations. |
| As a player | I want to see a start button so that I can begin the game when I am ready. |
| As a player | I want to see a grid of cards face down so that I can start matching pairs. |
| As a player | I want to click on a card to flip it over so that I can see the image or definition on the other side. |
| As a player | I want to see the cards flip back over if they do not match so that I can try again to find a matching pair. |
| As a player | I want to see the cards stay face up if they match so that I know I have found a correct pair. |
| As a player | I want to see a message when I have matched all pairs so that I know I have completed the game. |
| As a player | I want to see a timer counting up so that I can see how long it takes me to complete the game. |
| As a player | I want to see a counter for the number of attempts I have made so that I can track my progress and try to improve. |
| As a player | I want to see a reset button so that I can restart the game at any time. |
| As a player | I want to have different levels so that the game remains challenging and educational. |
| As a player | I want to have access to instructions, so that it’s easy to understand how to play the game. |

<br>

### Fonts

Choosing the right font is a critical aspect of UX design, as it greatly impacts readability and overall user experience. In the initial stages of our project, we selected the Google Font "Bangers" for its fun,  bold and eye-catching style. However, upon reflection, we realized that "Bangers" was limited to uppercase letters, which could hinder readability, especially for younger audiences. This limitation prompted us to explore alternative fonts that would enhance the readability for users of all ages.

<br>

<img src="readmedocs/bangers-font.png" alt="font use" width="40%" height="40%">
<br>


After experimenting with several fonts, including "Poppins," "Figtree," and "Jost." Each font was evaluated for its clarity, legibility, and visual appeal. After thorough testing and consideration, we ultimately settled on "Jost." This font provided the perfect balance of readability and style, ensuring that our game remained accessible and engaging for Key Stage 3 students. Our careful selection process highlights the importance of choosing the right font to create an inclusive and effective user experience.

<br>

<img src="readmedocs/jost-font.png" alt="font use" width="60%" height="60%">
<br>

### Images

When selecting the background image for our game, we carefully considered various science-themed visuals to ensure they aligned with the educational and aesthetic goals of our project. We evaluated numerous images, focusing on those that would effectively convey the theme of science lab safety. After thorough consideration, we decided on a laboratory image that would be both appealing and fun for a younger audience. It was important to choose an image that was engaging without being overly childish, so we opted for a vector-based cartoon style graphic. This choice was made to reflect the core concept of the game, which revolves around understanding and identifying laboratory safety hazards. The laboratory image provides an appropriate context for the game's content, helping to immerse students in a realistic and relevant environment. This thoughtful selection process underscores our commitment to creating an engaging and educational experience for Key Stage 3 students.

<br>

<img src="readmedocs/labbackground.webp" alt="Lab background image" width="50%" height="50%">

<br>

During the design process, we realized the importance of a unique and recognizable favicon to represent our game. After exploring various options, we found that there wasn't anything suitable that truly captured the essence of our project. As a result, we decided to create our own custom favicon. This allowed us to design a favicon that was perfectly aligned with our theme and aesthetic goals, ispecifically by adding a graphic of a pair of cards and the game initials. Our custom favicon not only enhances the visual identity of our game but also adds a professional touch to the overall user experience. The process of creating our own favicon ensured that we had a distinctive and memorable icon that stands out in users' browser tabs and bookmarks.

<br>

<img src="assets/images/FAVICONSS.png" alt="favicon image" width="20%" height="20%">

<br>

The selection of game cards was a critical part of our design process, ensuring that the content was both educational and engaging for students. We based our game cards on an image resource that depicted a grid of common science lab hazards. This comprehensive visual reference allowed us to choose relevant and recognizable hazards to include in the game. To enhance the learning experience, we decided to incorporate a "study first" modal, which would present the grid of hazards to students before they began playing. This modal provided a brief overview of the hazards, giving students an opportunity to memorise and familiarize themselves with the content and better understand what they would encounter on the game cards. Additionally, the card images would reflect the level of difficulty that the player selected, with the pairings varying based on the chosen difficulty level. By using this approach, we aimed to create an informative and interactive game that reinforces important lab safety concepts in an accessible and enjoyable way. Having different levels of difficulty meant that the game could appeal to older students who needed a more challenging study revision tool, catering to their advanced learning needs.
<br>

<img src="readmedocs/paired-cards.png" alt="corrosive a" width="50%" height="50%">


<br>

### Colours

When selecting the color scheme for our game, we began with our vibrant background image as the starting point. We wanted colors that would complement the fun and engaging theme while providing sufficient contrast for readability. After careful consideration, we chose dark cyan (rgba(0, 139, 139, 0.85)) and orange (#FF8400), alongside black and white. The dark cyan and orange provided a striking yet harmonious contrast that stood out against the colorful backdrop. Black and white were used to ensure clarity and legibility without straying too far from the chosen color palette. This thoughtful selection of colors ensured that the game was visually appealing, easy to read, and cohesive with the overall design theme, enhancing the user experience for our players.

<img src="readmedocs/dark-cyan.png" alt="dark cyan colours" width="50%" height="50%"><img src="readmedocs/orange.png" alt="orange colours" width="50%" height="50%">
<br>

### Wireframes

- Mobile

<img src="readmedocs/Hazards-Match-Mobile-Wirefame.png" alt="Mobile wireframe" width="25%" height="25%">
<br>

- Tablet

<img src="readmedocs/Hazards-Match-Tablet- Wireframe.png" alt="Tablet wireframe" width="30%" height="30%">
<br>

- Desktop

<img src="readmedocs/Hazards-Match-Desktop-Wirefame.png" alt="Desktop wireframe" width="60%" height="60%">
<br>
<br>
<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Features

To ensure our educational card matching game is engaging, intuitive, and beneficial for Key Stage 3 students, we have incorporated a range of essential features based upon the study of user needs. These features are designed to enhance the overall user experience while aligning with the educational objectives of the game. We prioritized creating a clear and easy-to-understand game structure, making sure the game is responsive and visually appealing across various devices.

Key functionalities include a shuffle function to randomize cards, a new game button for player control, and a grid of face-down cards to begin the matching process. We also included interactive elements such as a card flip function and feedback mechanisms like cards staying face-up when matched, a timer, a congratulatory alert when all pairs were matched, and a moves counter for tracking (and improving) progress. At the final review it was decided that we would add a "glow" to each card the user hovered over to aid in identifying which card was about to be selected, and once a pair had been matched both cards would be given a coloured border so that on completion of the game the player could visually identify all the matches. Additionally, the game offers different levels of difficulty, and accessible instructions to cater to diverse learning needs. These features collectively contribute to a fun, educational, and user-friendly game that effectively aids students in learning about science lab hazards.
<br>

### Instructions/Study First 

To enhance the educational value of our game, we introduced a "study first" modal that players can access before starting the card game. This modal presents an infographic, allowing players to familiarize themselves with the content and know what to expect. This preparation step helps reinforce the learning objectives by giving students a chance to review the hazards beforehand. Additionally, we incorporated detailed instructions to guide players on how to navigate and play the game effectively. To further support their learning, we provided a link to the BBC Bitesize website, a valuable resource for additional revision. These features collectively ensure that players are well-prepared and supported throughout their learning journey.
<br>

<img src="readmedocs/instructions-new-font.png" alt="instructions modal" width="30%" height="30%">

### Game board

When deciding the format of the game board, we prioritized ease of navigation and user familiarity. After considering various options, we opted for a 4x4 layout, which is intuitive and straightforward for players of all ages. This format ensures that the game remains accessible and engaging without overwhelming the user. Additionally, we adopted a tablet-first design approach to cater to the growing number of students using this go-to device school laboratories. This strategy ensured that the game board was optimized for touch interactions and provided a seamless experience across different devices. 
<br>

<img src="readmedocs/screenshot-hazards-game.png" alt="gameboard image" width="30%" height="30%">

### Game Cards
The selection and design of our game cards were central to creating an educational and engaging experience for players. They consisted of 3 game cards that correspond as follows:
Group a – symbols of hazards.
Group b – the name (label) of each hazard symbol.
Group c – the description of the risk posed by this hazard.

The game offers 3 levels of difficulty and the pairing combinations vary dependant upon each level: 
Easy – Match the ‘Symbol’ to its corresponding ‘Label’.
Medium – Match the ‘Symbol’ to the ‘Description of the risk’.
Hard – Match the ‘Label’ to the ‘Description of the risk’.

Subtle features added in the later stages of development includied: on hovering over a card (as well as the cursor change), a card a "glow" is visible to aid in identifying the current card that the player is selecting; and once a pair had been matched, both cards would be given a coloured border.

<br>
<img src="assets/images/hazards/corrosive-a.png" alt="corrosive a" width="20%" height="20%">
<img src="assets/images/hazards/corrosive-b.png" alt="corrosive b" width="20%" height="20%">
<img src="assets/images/hazards/corrosive-c.png" alt="corrosive c" width="20%" height="20%">
<img src="assets/images/question-mark-green.png" alt="green question mark back-face" width="20%" height="20%">

<br>

Subtle features added in the later stages of development includied: on hovering over a card (as well as the cursor change), a card a "glow" is visible to aid in identifying the current card that the player is selecting; and once a pair had been matched, both cards would be given a coloured border.

<br>
<img src="readmedocs/card-glow.png" alt="Card glow on hover" width="40%" height="40%">
<img src="readmedocs/coloured-pairs.png" alt="Coloured border card pairs" width="50%" height="50%">
<br>

### Buttons

To enhance usability and streamline the game experience, we strategically placed centrally located buttons that served multiple functional purposes. These buttons included options to trigger a new game, allowing players to easily restart if needed. We also incorporated a level selection button, enabling users to choose different difficulty levels and tailor their experience to their learning needs. Additionally, we added a "study first" button, providing players with an opportunity to review the educational content before starting the game. By positioning these buttons centrally, we ensured that key functions were readily accessible and intuitive to use, contributing to a smooth and enjoyable user experience.

<img src="readmedocs/difficulty-levels.png" alt="difficulty drop down menu" width="30%" height="30%">
<img src="readmedocs/buttons.png" alt="Card glow on hover" width="70%" height="70%">
<br>


### Scores
To facilitate a more engaging and educational experience, we implemented several key features to help students monitor their progress and performance. We introduced counters to track the number of attempts and moves made by the players, as well as a timer to measure the time taken to complete the game. These metrics allow students to gauge their improvement over time and strategize more effectively, aiming to reduce errors with each playthrough and improve their speed while maintaining accuracy.


<img src="readmedocs/Scores-bar.png" alt="scores bar" width="60%" height="60%">
<br>


Additionally, we added an alert to congratulate the player when they correctly match all pairs. This alert not only celebrates their achievement but also displays their stats, providing a motivating and rewarding element to the game. This combination of features creates a motivating and interactive learning environment where students can set personal goals and continually strive to better their previous records.


<img src="readmedocs/Screenshot 2024-12-02 at 16.39.15.png" alt="Congratulations alert" width="40%" height="40%">
<br>


### Responsive Design

This card matching game was initially designed with tablet devices in mind, as it was primarily intended for use by school children as an interactive study guide. The layout and interface elements have been optimized for tablet screen sizes to ensure an engaging and user-friendly experience on these devices. While the game is functional on laptop screens, we acknowledge that the responsiveness for larger displays could be improved. Given more development time, our next priority would be to enhance the game's adaptability to laptop and desktop screen sizes, ensuring a seamless experience across a wider range of devices.
<br>

<img src="readmedocs/Responsive-design.png" alt="responsive design" width="70%" height="70%">


### Future Features

Looking ahead, we have identified several potential features to further enhance the Hazards-Match game and broaden the scope of the Science-Shuffle product.

The Hazards-Match game could have minimal future features such as:
1 – a time-out feature – the game times-out when (for example) 5 minutes has elapsed – a message would pop up to let the player know that the game has timed-out and give the player the option to restart.

2 – a field to enter the players name so that
a - their name could be added to the ‘congratulations!’ message that appears when all matches in one game are complete
b – a leaderboard feature could be added.

The Science-Shuffle product could include many other games based on Scientific concepts, such as:

Periodic-table-Match (11-14yrs): match the (a) element name to the (b) element symbol with atomic number and atomic mass number group to the (c) properties of the group

Laboratory-equipment-Match (11-14yrs): match the (a) diagram of apparatus (b) name of the apparatus to the (c) description of its use.


<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Agile Methodology

Throughout this project, our team implemented Agile methodology by using a Kanban board to efficiently manage tasks and ensure a smooth workflow. Utilizing GitHub Project Boards, we set up various user issues, assigning them to team members based on their expertise and availability. This allowed us to visually track the progress of each task, identify bottlenecks, and prioritize work effectively. 

By continuously updating the board and holding regular stand-ups, we maintained clear communication and quickly adapted to any changes, ensuring that we delivered high-quality results in a timely manner. Additionally, the use of GitHub Issues enabled us to document each task with detailed descriptions, acceptance criteria, and labels for easy categorization. This structured approach facilitated clear accountability and enhanced collaboration within the team, helping us achieve our project goals efficiently. 


Effective communication was pivotal to our project's success. Regularly attending huddles and actively using Slack messages ensured that all team members were informed and aligned on our progress and goals. This consistent communication allowed us to quickly address any issues, share updates, and collaborate efficiently. By maintaining open lines of communication, we were able to stay organized, make informed decisions, and ensure that everyone was on the same page, which ultimately led to a smooth and successful development process.

<br>

<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Tech

### Languages 
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

### Frameworks and Libraries
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

### Software and Tools 
![Gimp Gnu Image Manipulation Program](https://img.shields.io/badge/Gimp-657D8B?style=for-the-badge&logo=gimp&logoColor=FFFFFF) ![Microsoft Word](https://img.shields.io/badge/Microsoft_Word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white) ![GitHub Copilot](https://img.shields.io/badge/github_copilot-8957E5?style=for-the-badge&logo=github-copilot&logoColor=white) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)

<br>

<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## AI Tools

### Development Process

To help generate the user stories for our project, AI produced a structured process to identify the needs and goals of different stakeholders, such as students and teachers. We crafted our prompts specifically for user stories in a format that clearly articulated the desired outcomes and motivations: "As a ..., I want to..., so I can..." and requested these needs to be processed into acceptance criteria and tasks. This approach ensured that each story was user-centric and aligned with the overall project objectives.

As we worked through the user stories we refined our prompts as necessary to ensure clarity and specificity.
This iterative process allowed us to hone in on the exact requirements and steps needed to meet our UX design goals, and Agile performances, resulting in comprehensive and actionable user stories. By refining our prompts, we could better capture the nuances of each user's needs and ensure that the development process remained focused and aligned with the desired outcomes.

This thorough and systematic method enabled us to create a detailed roadmap for developing the educational card pairing game. It ensured the game was engaging, effective, and tailored to the needs of its users, ultimately enhancing the learning experience for Key Stage 3 students.
<br>

### Generating Code

We utilized AI tools to assist in the initial code generation for our card matching game. By leveraging AI, we were able to quickly establish the foundation of our application using HTML, CSS, Bootstrap, and JavaScript. This strategic use of AI enabled us to generate responsive layouts and interactive elements efficiently, ensuring that our code adhered to best practices and standards. For instance, the AI tools helped us create the card pairing game interface, which included smooth, dynamic interactions with a focus on DOM-manipulation, significantly reducing the time required for manual coding.
<br>

### Debugging Code

AI tools were also instrumental in debugging our code. Throughout development, we utilized AI to continuously analyze various aspects of our code which enabled us to identify and correct code issues promptly through providing suggestions for resolving them. This included detecting syntax errors, reference errors, type errors, etc, and optimizing code performance. For instance, AI-driven optimizations helped us fine-tune the HTML, CSS and JavaScript, resulting in a smooth,  more error-free, engaging gameplay experience for our target audience.
<br>


### Reflections on AI

On reflection, the integration of AI into our project development process has essentially brought about a paradigm shift. It enabled us to speed up our workflow, work smarter and more efficiently by automating mundane tasks, providing intelligent code suggestions, and offering real-time debugging and optimization; In summary, AI tools have supported us in delivering a polished, educational web app game aimed at Science Key Stage ???? students. 
<br>


<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Deployment

The deployment process was coordinated to ensure the website was hosted on the GitHub platform without any issues. To ensure the website was functioning correctly and providing a seamless user experience, we implemented a process of regular deployments to our live environment. These frequent deployments allowed us to continuously monitor the site for any issues and promptly address them. By deploying updates incrementally, we could verify that new features and fixes were working as expected in a real-world setting. This proactive approach helped us maintain the site's performance and stability, ensuring that our educational tool remained reliable and effective for students and teachers alike.

To deploy this project, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/science-shuffle.git
   cd science-shuffle
   ```

2. **Install Dependencies:**
   Make sure you have Node.js and npm installed. Then, run:
   ```sh
   npm install
   ```

3. **Build the Project:**
   ```sh
   npm run build
   ```

4. **Deploy to GitHub Pages:**
   ```sh
   npm run deploy
   ```

5. **Access the Live Site:**
   After deployment, you can access your project at `https://your-username.github.io/science-shuffle/`.

<br>
<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Testing

During the testing phase of our project, we encountered several bugs that needed to be addressed to ensure the game's functionality and user experience were top-notch. Identifying these issues early allowed us to implement targeted solutions and refine our code, ultimately leading to a more polished and reliable product.

### Bug Log

| Bug Discovered | Solution/Potential Solution |
| -------------- | --------------------------- |
| Bug 1: If user flips a card, they should not be able to unflip it, and they currently can, and it puts the card out of play! | Fixed by adding more code like lockbox |
| Bug 2: Card game visibility in the viewport - responsivity | This was worked on EXTENSIVELY, and some responisve issues remain, however we are satisfied with the tablet view as this is primarily the device used in schools labs. |
| Bug 3: Images not displaying in the grid or flipping in their current position | Resolved by adjusting sizing and added the correct flexbox properties, styling properties and correct file-paths |
| Bug 4: When the game was restarted before cards were unflipped, they first shuffled and then unflipped, giving away the new locations of the cards. | Added a time delay to the restart button so that the cards could unflip before being shuffled |
| Bug 5: Timer doesn't stop when the game is finished | Added the clearInterval function to the matchCounter function so that the timer stops when all the cards are matched |
| Bug 6: The 'congrats! you've matched all the cards!' alert appears as the last card is clicked but BEFORE it flips front-face up | Added a set timeout function to allow the user to click the final card before the alert appears |
| Bug 7: No resetting of game once changing levels | Added reset button to function that changes levels|
| Bug 8: Difficulty level dropdown selector buttons not linking to the Javascript eventlisteners and correct game-set | Javascript code amended from 'block' to 'grid' to match css class |




<br>


### Validation

Validation is a crucial aspect of the software development process, as it ensures that the product meets the specified requirements and functions as intended. To enhance our validation efforts, we leveraged online validation tools extensively. These tools allowed us to automate testing and quickly identify any discrepancies or errors in our code. By utilizing these tools, we were able to perform rigorous testing and verification, ensuring that each component and feature functioned correctly and met our quality standards. Online validation tools provided real-time feedback and detailed reports, enabling us to address issues promptly and refine our code efficiently.
<br>

#### Lighthouse
The Lighthouse validation results proved to be pleasing - it recommended that our site served images in next-gen formats therefore reducing unused CSS.

<img src="readmedocs/Screenshot 2024-12-02 at 16.33.45.png" alt="Lighthouse scores" width="70%" height="70%">
<img src="readmedocs/lighthouse-desktop.png" alt="Lighthouse scores" width="70%" height="70%">


#### WAVE
The results from the WAVE validation were pleasing, and suggested that there were no major contrast errors.

<img src="readmedocs/Screenshot 2024-12-02 at 16.28.23.png" alt="WAVE validation results" width="40%" height="40%">

#### W3C - HTML
W3C Validator identified errors that where then corrected and finally zero errors but 5 ‘Warnings’ remain - these all refer to not having a heading in the section – it was agreed that headings are not required in the sections.

<img src="readmedocs/W3C-validation-no-errors-5-warnings.png" alt="validation" width="70%" height="70%">

#### W3C- CSS
W3C CSS Validator identified no warnings or errors.

<img src="readmedocs/W3C-CSS-validation-no-errors.png" alt="validation" width="70%" height="70%">

### JS Hint
There were a few warnings in JSHint, primarily related to the use of let or arrow function syntax. These modern JavaScript features are sometimes unsupported or behave inconsistently in older browsers, such as certain versions of Mozilla Firefox. While these warnings highlight potential compatibility issues, they do not impact the core functionality of the game, as most modern browsers fully support these syntactical elements. 

<img src="readmedocs/jshint-screenshot.png" alt="responsive design" width="100%" height="100%">

<br>
<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Credits and Acknowledgements


### Credits

### README
<br>

- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [README file generator/editor](https://www.readme.so)
- [Code Institute readme tutorial ](https://www.youtube.com/watch?si=YlDWOkkzvTBjbgs3&v=l1DE7L-4eKQ&feature=youtu.be)
- [README.md example](https://github.com/TheRickyroy/astronauts-for-autism/blob/main/README.md#tools-and-programs)
- [Badges](https://github.com/Ileriayo/markdown-badges)
<br>

### FONTS
<br>

- Font readability -https://fonts.google.com/knowledge/readability_and_accessibility/how_type_influences_readability
- Some example font pairings, such as Prompt, Cabin, Raleway, etc - https://www.figma.com/google-fonts
<br>

### COLOURS
<br>

- https://colorhunt.co/palettes/kids
- https://coolors.co/palettes/popular/kids
- https://colorkit.co/background-maker/1982c4-8ac926/
- https://www.freepik.com/author/jcomp
<br>

### IMAGERY
<br>

- Interactive periodic table - https://artsexperiments.withgoogle.com/periodic-table/
- 118-element-infographics-RSC https://www.rsc.org/iypt/iypt-elements/?utm_source=rsc-periodic-table-site&utm_medium=referral&utm_content=iypt-banner
- https://www.istockphoto.com/ images of atoms - Todd Helmenstine. Todd Helmenstine is the physicist/mathematician who creates most of the images found on sciencenotes.org. The graphics are created in Adobe Illustrator, Fireworks and Photoshop.
- Question mark cards attribution line “Designed by Freepik” www.freepik.com
- Periodic-table-KS3.jpg – www.pintrest.com
- Image compressor - https://www.freeconvert.com/image-compressor
- https://www.vecteezy.com Vectors by Vecteezy
- https://image.online-convert.com/convert/word-to-svg converts graphics produced on MS Word into svg
- http://www.cloudinary.com
- https://inkscape.org/release/inkscape-1.3.2/
- https://www.freepik.com/free-vector/science-lab-flat-style_7431195.htm#fromView=keyword&page=1&position=52&uuid=fcd0cba6-7fb7-486b-ace7-8e7999b3cc9f
- https://www.freepik.com/author/brgfx


### RESPONSIVE DEVICE IMAGES

- https://ui.dev/amiresponsive
- https://websitemockupgenerator.com


### Acknowledgements

 A huge thank you to Mark, John and Dillon at Code Institute for their support and help, we truly appreciate it!
 And to our family and friends who tested our deployments and gave great feeback, thank you so much!
 Thank you to Sarah H for reaching out with a fix to one of our sizing problems, it was a huge help!


<p align="right"><a href="#science-shuffle">Back To Top</a></p>

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.
