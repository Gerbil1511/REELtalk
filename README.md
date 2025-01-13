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
  - 
  - 
  - 
  - [Buttons](#buttons)
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

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## PROJECT OUTLINE
Welcome to 'ReelTalk' an interactive, Full-Stack Web application designed for movie enthusiasts.

The idea for this project stems from being one of a family of passionate movie lovers and from the desire to create a dynamic, interactive platform where users can explore and discuss their favorite films (far better than having arguments with family members over differing opinions—no more debates about which Star Wars movie is the best!). 

Inspired by platforms like Letterboxd, the forum aspect of the application allows users to create and manage discussions about movies. Whether it's sharing reviews, debating plot twists, or recommending hidden gems, the forum provides a space for movie enthusiasts to connect and engage with each other. This community-driven feature is designed to promote interaction and create a vibrant online community of movie lovers.

Leveraging Django's robust framework, this project aims to deliver a comprehensive application that encapsulates CRUD (Create, Read, Update, Delete) functionality and custom models.

The application integrates with The Movie Database (TMDb) to provide users with an extensive database of movie information. Users can search for movies, view detailed information, and stay updated with the latest movie news. This feature not only enhances the user experience but also fosters a deeper connection with the world of cinema. It also has a dedicated section for the latest movie news keeps users informed about industry updates, new releases, and film events. By aggregating news from various sources, the application ensures that users have access to the most relevant and up-to-date information.

By combining these elements, the project aims to offer a rich and engaging experience for users, highlighting the importance of both individual exploration and community interaction. Through this application, users can not only discover new movies but also share their insights and connect with like-minded individuals.


<p align="right"><a href="#REELtalk">Back To Top</a></p>

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
| As a player | I want a  so that I can   . |


<br>

### Fonts


<br>

<img src="readmedocs/g" alt="font use" width="40%" height="40%">
<br>




<br>

<img src="readmedocs/jost-font.png" alt="font use" width="60%" height="60%">
<br>

### Images


<br>

<img src="readmedocs/" alt="Lab background image" width="50%" height="50%">

<br>


<br>

<img src="assets/images/FAVICONS.png" alt="favicon image" width="20%" height="20%">

<br>


<br>

<img src="readmedocs/" alt="corrosive a" width="50%" height="50%">


<br>

### Colours



<img src="readmedocs/dark-cyan.png" alt="dark cyan colours" width="50%" height="50%"><img src="readmedocs/orange.png" alt="orange colours" width="50%" height="50%">
<br>

### Wireframes

- Mobile

<img src="readmedocs/.png" alt="Mobile wireframe" width="25%" height="25%">
<br>

- Tablet

<img src="readmedocs/.png" alt="Tablet wireframe" width="30%" height="30%">
<br>

- Desktop

<img src="readmedocs/.png" alt="Desktop wireframe" width="60%" height="60%">
<br>
<br>
<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Features

### Register/Login/Logout

### Movie List


<img src="readmedocs/.png" alt="" width="30%" height="30%">

### Forum



<img src="readmedocs/.png" alt="" width="30%" height="30%">

### Forum Post Detail


<br>


<br>
<img src="readmedocs/.png" alt="r" width="40%" height="40%">

<br>

### Buttons



<img src="readmedocs/s.png" alt="" width="30%" height="30%">

<br>


### Upvotes/DownVotes



<img src="readmedocs/.png" alt="Congratulations alert" width="40%" height="40%">
<br>


### Responsive Design


<br>

<img src="readmedocs/.png" alt="responsive design" width="70%" height="70%">


### Future Features

Looking ahead, we have identified several potential features 


<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Agile Methodology

Throughout this project, our team implemented Agile methodology by using a Kanban board to efficiently manage tasks and ensure a smooth workflow. Utilizing GitHub Project Boards, we set up various user issues, assigning them to team members based on their expertise and availability. This allowed us to visually track the progress of each task, identify bottlenecks, and prioritize work effectively. 

By continuously updating the board and holding regular stand-ups, we maintained clear communication and quickly adapted to any changes, ensuring that we delivered high-quality results in a timely manner. Additionally, the use of GitHub Issues enabled us to document each task with detailed descriptions, acceptance criteria, and labels for easy categorization. This structured approach facilitated clear accountability and enhanced collaboration within the team, helping us achieve our project goals efficiently. 


Effective communication was pivotal to our project's success. Regularly attending huddles and actively using Slack messages ensured that all team members were informed and aligned on our progress and goals. This consistent communication allowed us to quickly address any issues, share updates, and collaborate efficiently. By maintaining open lines of communication, we were able to stay organized, make informed decisions, and ensure that everyone was on the same page, which ultimately led to a smooth and successful development process.

<br>

<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Tech

### Languages 
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

### Frameworks and Libraries
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

### Software and Tools 
![Gimp Gnu Image Manipulation Program](https://img.shields.io/badge/Gimp-657D8B?style=for-the-badge&logo=gimp&logoColor=FFFFFF) ![Microsoft Word](https://img.shields.io/badge/Microsoft_Word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white) ![GitHub Copilot](https://img.shields.io/badge/github_copilot-8957E5?style=for-the-badge&logo=github-copilot&logoColor=white) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)

<br>

<p align="right"><a href="#REELtalk">Back To Top</a></p>

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


<p align="right"><a href="#REELtalk">Back To Top</a></p>

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
<p align="right"><a href="#REELtalk">Back To Top</a></p>

## Testing

During the testing phase of our project, we encountered several bugs that needed to be addressed to ensure the app's functionality and user experience were top-notch. Identifying these issues early allowed us to implement targeted solutions and refine our code, ultimately leading to a more polished and reliable product.

### Bug Log

| Bug Discovered | Solution/Potential Solution |
| -------------- | --------------------------- |
| Bug 1:  | Fixed by  |





<br>


### Validation

Validation is a crucial aspect of the software development process, as it ensures that the product meets the specified requirements and functions as intended. To enhance our validation efforts, we leveraged online validation tools extensively. These tools allowed us to automate testing and quickly identify any discrepancies or errors in our code. By utilizing these tools, we were able to perform rigorous testing and verification, ensuring that each component and feature functioned correctly and met our quality standards. Online validation tools provided real-time feedback and detailed reports, enabling us to address issues promptly and refine our code efficiently.
<br>

#### Lighthouse
The Lighthouse validation results 

<img src="readmedocs/.png" alt="Lighthouse scores" width="70%" height="70%">
<img src="readmedocs/.png" alt="Lighthouse scores" width="70%" height="70%">


#### WAVE


<img src="readmedocs/.png" alt="WAVE validation results" width="40%" height="40%">

#### W3C - HTML


<img src="readmedocs/.png" alt="validation" width="70%" height="70%">

#### W3C- CSS
W3C CSS Validator identified no warnings or errors.

<img src="readmedocs/.png" alt="validation" width="70%" height="70%">

#### JS Hint

#### Python Linter


<img src="readmedocs/.png" alt="responsive design" width="100%" height="100%">

<br>
<p align="right"><a href="#REELtalk">Back To Top</a></p>

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


<p align="right"><a href="#REELtalk">Back To Top</a></p>

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
