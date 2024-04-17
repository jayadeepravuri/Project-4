# [AGAPE](https://wild-swim-scotland-47f727d45ac1.herokuapp.com/ "take you to the Agape's Deployed Page")

![am-i-responsive-image](documentation/readme%20images/am%20i%20responsive.png)

# Introduction

The platform was built utilizing Django, boasting comprehensive CRUD operations and an intuitive user interface to facilitate volunteering for agape-related tasks. Users receive alerts in the form of notification boxes for any updates to their accounts or bookings. Administrators enjoy additional privileges, such as the ability to search for volunteers and their selected tasks based on dates and usernames.


[Live Site Here](https://wild-swim-scotland-47f727d45ac1.herokuapp.com/ "take you to the Wild Swim Deployed Page")

# Table of Contents

- [Key Project Goals](#key-project-goals)
- [Agile Development](#agile-development)
- [User Stories](#user-stories)
- [User Experience](#user-experience)
    - [Web Templates](#web-templates)
    - [Database Schema](#database-schema)
    - [Typography](#typography)
    - [Colour Palette](#colour-palette)
    - [Logo](#logo)
    - [Design Choices](#design-choices)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Non logged in user](#non-logged-in-user)
            - [The Landing page And General Site Content](#the-landing-page-and-general-site-content)
            - [Login](#login)
            - [Register](#register)
        - [Logged in User](#logged-in-user)
            - [Logout](#logout)
            - [Your Upcoming Swims](#your-upcoming-swims)
        - [Staff User](#staff-user)
            - [Add Swim](#add-swim)
            - [Edit and Delete buttons](#edit-and-delete-buttons)
            - [Delete Swims](#delete-swim)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Deploying on GitHub Pages](#deploying-on-github-pages)
    - [The ElephantSQL Database](#the-elephantsql-database)
- [Credits](#credits)
    - [Content](#content)
        - [Images](#images)
    - [Education](#education)
- [Acknowledgements](#acknoledgements)

[Back to Top](#agape)

# Key Project Goals

The goals of the sites functionality are:

- List View: users will get introduced about agape and can view the tasks they can volunteer
- Register: users can register to the site so that they can use the sites functionality 
- Logged In: users have the ability to volunteer for a task in agape and can edit/cancel their volunteering
- Logged Out: users are asked if they wish to sign out of the site
- Admin: can view the tasks that are volunteered and can also volunteer himself in one of the available tasks, Also, admin can search volunteerings and confirm them.

# Agile Development

A Kaban board was used in GitHub to create the agile development process – see the board [here]( https://github.com/users/sarahgoodwin93/projects/3 "Kaban board for Wild Swim Scotland Project")

User stories were labelled using the MoSCoW method.

[Back to Top](#agape)

# User Stories

4 Epics were created broken down into user stories, the epics included:

1. Admin
2. Staff
3. Site Access
4. User Functions

The user stories are as follows:

## Epic - Admin

### Create staff users

- As an admin, I can use the Django admin panel to create new tasks,search volunteerings, view volunteerings and confirm them.
    - AC1 - Admin can access the Django admin panel
    - AC2 - Admin can create tasks.
    - AC3 - Admin can search volunteerings, view volunteerings and confirm them.

Assignment
- Create a specific volunteer home page for admin, so he can search and view all the volunteerings
- create a volunteer detail page , where the admin can confirm the volunteerings or delete them.


## Epic - User

### Volunteer for tasks

- As a user, I should be able to volunteer for tasks by volunteering to the tasks, view my volunteerings, edit and delete them.
    - AC1 - Volunteer to the tasks 
    - AC2 - View their volunteering , 
    - AC 3 - Edit/cancel their volunteering

Tasks
-   Create a volunteer form where users, including admin can volunteer for tasks, by choosing the date, task and can write a message and also request a co-volunteer in the form.
-  Create a volunteer detail page, where the user can view his volunteering and can also see if it is confirmed.also, scan edit/ cancel his volunteering.

## Epic - Site Access

### Log-in and log-out

- As a user, I can log in with my created username and password to access the site and see my previous actions
    - AC1 - Site user can log in with their created username and password after they have registered to the site
    - AC2 - Site users can see the volunteerings they have registered from a previous login
    - AC 3 - Site user can log out when they have finished their session and confirm they want to log out

Assignments
- Link accounts/login template so that users can sign into the site.
- Link accounts/logout template so that users can sign out of the site.
- Ensure data is saved from previous login so that users can see their volunteerings.

### Register an account

- As a user I can register an account so that I can return to see the volunteerings I have volunteered through the volunteer form.
    - AC1 - User can register account and see site functionality

Tasks
- Create a Register nav link button
- Link 'accounts/sign_up.html' template so that new users can register to the site
- Ensure registered users can see site functionality changed from being logged in vs logged out

## Epic - User Functions

### View Task List

- As a user I can view the tasks and decide to volunteer if I wish to register and sign up to a volunteering
    - AC1 - When the site loads,the list of tasks to volunteer should be displayed
    - AC2 - User can view tasks without logged in
    - AC3 - User can view and can volunteer once logged in

Assignments
- Create a swim model to pull data from added swims and view to show the swims on the homepage
- Create user authentication so that only logged-in users can join swims

### Volunteer for a Task

- As a logged-in user, I can click on the task card , which leads me to the volunteer form so I can make sure to choose the task that i choose to volunteer, date and also, request a co-volunteer.
    - AC1 - The volunteer form is displayed for logged in user to volunteer for tasks.
    - AC2 - The volunteer detail card is displayed for the logged in user in the volunteer homepage. on clicking that, he can either edit or cancel his volunteering.

Assignments
- Ensure the volunteer form is not visible to unauthorised users
- Create model caleed volunteering.
- Create a view in relation to the volunteering model, to view, create , edit, delete, and  confirm to delete the volunteerings.

### Profile

- As a logged-in user, I can update my account informations
    - AC1 - A dedicated profile page is assigned to update username and email

Assignments
- Create a acount detail button in the account coloumn , white leads to account informations page , where the username and email can be updated.


# User Experience

## Web Templates

![HomePage](documentation/readme%20images/homepage.png "Lucid image")
![SignIn ](documentation/readme%20images/sign%20in%20page.png "Lucid image")
![SignUp ](documentation/readme%20images/signup%20page.png "Lucid image")
![VolunteerForm Page](documentation/readme%20images/Volunteer%20form.png "Lucid image")
![Volunteer Home ](documentation/readme%20images/Volunteer%20home.png "Lucid image")
![Volunteer Home Admin](documentation/readme%20images/Volunteer%20home%20admin.png "Lucid image")
![Volunteer Detail](documentation/readme%20images/Volunteer%20detail%20form.png "Lucid image")
![Profile](documentation/readme%20images/Profile%20page.png "Lucid image")

Site structure was created before the site was created to test layout idea.

## Database Schema

The project uses ElephantSQL as PostgreSQL relational database for storing the data.

The data schema was created using [Lucid Chart](https://www.lucidchart.com "Lucid Chart") before the project was started to get the flow and function of the models. 

![Data Schema Image](documentation/readme%20images/data%20schema.png " Data Schema Image ")

## Typography

The google font [Poppins](https://fonts.google.com/specimen/Poppins "Poppins") was used throughout the site with different weights for different headings and paragraphs.

I selected this font due to its tall stature and expansive proportions, which enhance readability.

## Colour Palette

- The main colors used were based on the the colors in the logo.
  - #f9f8f1 
  - #f5f5dc
  - #491609
  - #491609
  - #000000
  
![Color palette Image](documentation/readme%20images/color-pallete.png "Color palette Image ")

### Logo

The logo used in the head section is agape community's official logo. Permission was taken to use the logo

![Logo Image](documentation/readme%20images/agapesverige_logo_favicon.png " Logo Image ")

## Design Choices

I aimed for the website's design to convey a sense of warmth and hospitality to visitors. My goal was to ensure that navigating the site would be effortless and intuitive, providing users with easy access to the information they seek. Rather than overwhelming visitors with excessive details about Agape, I focused on presenting essential information in a clear and concise manner. Through strategic decisions, I endeavored to introduce Agape in a manner that would resonate positively with users.  


[Back to Top](#agape)

# Features

## Existing Features

## Non-Logged in User

### The Landing page And General Site Content

![Homepage](documentation/readme%20images/Homepage%20Agape.png " Home page image ")
![Homepage](documentation/readme%20images/HomePage%202%20Agape.png " Home page image ")
![Homepage](documentation/readme%20images/HomePage%203%20Agape.png " Home page image ")


The landing page of the site of a non logged in / non registered user introduces them to agape and motivates them to volunteer for the tasks for agape . 
The page sections 
*values, and about us* intorduces the site visitor to agape and motivates them to volunteer for the tasks presented in the *connect* page section. 
Further , the page sections *contact*, is provided to give the location and contact the admin for feedback and queries
The landing page has 2 call to actions, *Register* and *Login*. 
The landing page is responsive for different screen sizes and scales down for easy mobile or tablet use. 

### Login

![login](documentation/readme%20images/SignIn%20Page%20agape.png " login image ")

The login page welcomes the user back to the site and has 2 clear options, username and password.
The design is friendly and approachable by using rounded corners on the input boxes.

The text at the bottom of the login section lets users know they must be logged into the site to use the full functions, it offers them an action if they have not yet registered by using the sign up link.

If the username and password are not correct this error will show.


### Register

![register](documentation/readme%20images/SignUp%20Agape.png " register form image ")

The register page welcomes users to the site with a friendly greeting. It lets users know that in order to use the site functions they must register an account.

It offers them space for a username, email(optional) password and then rechecks the password to ensure it matches and there were no errors.
An example of some of the errors:

The text at the top lets users know who already have an account that they can sign in using the login page.

## Logged in User


### Volunteer form page

![Volunteer form page](documentation/readme%20images/Volunteer%20form%20Agape.png "joined-swim-button image ")

The user will notice when the have logged in is that there is now more information regarding the volunteering oppurtunities and when agape happens. 
The user can now choose the task he wants to volunteer, the date he wants to volunteer, write an additional message regarding the task he chooses to volunteer. 
He can further notify the user and request for a covolunteer.
Now the user submits the form by cliking on the volunteer button and is redirected to the Volunteer home page 
additionally errors will be displayed, if the user chooses a task/date which is not available, an error message is displayed. also, if the user chooses a date in the past or if the date is not a wednesday, an error message is displayed.

### Volunteer home page

#### Logged in user
![Volunteer home page](documentation/readme%20images/Volunteer%20home%20agape.png "volunteer home page ")
Now the user is taken to the page where he can view all the tasks that he has choosen to volunteer on the left and his account details on the right.
when clicked on the card he is redirected to the volunteer-detail page, where he can edit or cancel his volunteering.*(more on volunteer-detail page is explained in the section below)*
Furthermore, the user can update his account information by clicking on the account details button.
Also, the user can choose to volunteer for more tasks by clicking the volunteer button below the account details button.

If the user hasn't volunteered for any tasks, the volunteer home page will look like this ![Volunteer home page](documentation/readme%20images/No%20upcoming%20Volunteers.png "no upcoming volunteerings")

#### Admin
![Volunteer home page](documentation/readme%20images/volunteer%20home%20admin%20agape.png "volunteer home page admin ")
For an admin, the volunteer home page is similar as an normal user, but he is provided with an additional search form on the right coloumn, 
where he can search for tasks the the user have choosen to volunteered by name or date or both. 
On the left column, admin can view all the volunteerings by default and is changed according to the search filter options.

### Volunteer-detail page

#### Logged in user
![joined swims](documentation/readme%20images/Volunteer%20detail%20page%20agape.png " volunteer detail page ")

when the user clickes on his volunteering card he is redirected to the volunteer detail page. 
He is now displayed with the choosen volunteer card , which gives the information like the date of volunteering, task, requested volunteer(if requested), confirmed/not confirmed yet. and 3 additional buttons.
When clicked on the Edit Volunteering button, the user is directed to the volunteer form page with the predefined user choices, where he can further make changes to his volunteering task.
when clicked on the cancel volunteering button, he is directed to the dete volunteering page, 
where the user is asked again if he wants to delete his volunteering task![no swims joined](documentation/readme%20images/volunteer%20delete%20page%20agape.png " Delete Volunteering ")
when clicked on back button, the user is taken back to the volunteer home page

### Logout

![logout](documentation/readme%20images/Signout%20agape.png " logout image ")

The logout page checks if the user does wish to sign out of the site.

## Future Features

There are some future features that I would like to add to the project to improve user functions.

- Email notifications:
  It would be nice to notify users regarding their tasks they have choosen to volunteered, and also, notify them when the admin confirms their task.
- Social media signup
- can add a profile picture and update their account information.
 
[Back to Top](#agape)

# Technologies Used

- [Lucidchart](https://www.lucidchart.com/ "link to Lucidchart homepage")
Lucidchart was used to create the website templates and dataschema
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "link to html5 wikipedia")
Used to create structure and content for the site.
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html "link to w3")
Used to add custom styles to the site.
- [Django](https://www.djangoproject.com/ "link to django docs homepage")
The python framework used to develop the site.
- [Bootstrap](https://getbootstrap.com/ "link to bootstrap homepage")
The CSS framework used to add styles and structure to the site.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "link to Python wikipedia")
Used to provide functionality to the site.
- [Cloudinary](https://cloudinary.com/ "link to cloudinary homepage")
Used to host the hero image
- [ElephantSQL](https://www.elephantsql.com/ "link to elephantsql homepage")
Used to host the database used for the site.
- [Am I Responsive?](https://ui.dev/amiresponsive "Link to Am I responsive webpage")
Am I Responsive was used to see the responsive design and create screenshots of the final page on different devices.
- [Codeanywhere](https://app.codeanywhere.com/ "Link to Codeanywhere webpage")
Codeanywhere was used for writing code, adding, committing and pushing to GitHub before issues were faced and moved to GitPod.
- [Gitpod](https://www.gitpod.io/#get-started "Link to gitpod webpage")
Used to continue to create code and file structure for the respository.
- [GitHub](https://github.com/ "Link to github webpage")
GitHub was used to store the code files, README files and asset files after pushing
- [Heroku](https://id.heroku.com/login "Link to Heroku login")
Heroku was used to deploy the project.
- [Canva]("https://www.canva.com")
Canva was used to create volunteer card image in connect section
-[Pexels]("https://www.pexels.com/")
Pexels was used to download free images for the home page of the website.


# Testing

Testing detail can be found [here](TESTING.md)

# Deployment

This project was developed using [Codeanywhere](https://app.codeanywhere.com/ "Link to Codeanywhere login") to begin with until issues with codeanywhere occurred. It was committed and pushed to GitHub using the Codeanywehere terminals.
After the issues with codeanywhere, the project was moved to [GitPod](https://www.gitpod.io/ "link to gitpod homepage") and continued from there. The projected had deployed at the start so the following is a step by step of how it was first deployed.

## Cloning The Repository

To clone the repository using GitHub the following steps were taken:

1. In the repository, select the "code" tab.
2. Select "HTTPS" in the dropdown menu.
3. Click the 'copy URL to dashboard button.
4. Open your chosen IDE
5. Create a new workspace and paste in the copied URL
6. Press enter

## Deploying on GitHub Pages

To deploy this page to Heroku from its Codeanywhere repository, the following steps were taken:

1. Get Python Essentials Template from Code Institute [P3 Template](https://github.com/Code-Institute-Org/p3-template "p3 template link")
2. Create a new repository using the P3 template
3. Copy the repo URL and copy it into Codeanywhere to create a new workspace
4. Install Django - add to requirements file
5. Create Procfile and add guricorn
6. Log in to Heroku
7. Click 'New' - 'Create new app'
8. Enter a name for the application and select the region
9. Click 'Create App'
10. Go to Settings and connect to GitHub - choose the correct repository
11. Click 'Reveal config vars' and add DISABLE_COLLECTSTATIC as the key with a value of 1
12. Go to Deploy and scroll down, click on 'Deploy Branch' to manually deploy
13. Once the app has deployed, click 'Open App' at the top of the page

## The ElephantSQL Database
ElephantSQL PostgreSQL Database was used for this project, to set up a database the following steps were taken:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance
4. Select "Tiny Turtle (Free)" free plan.
5. Click "Select Region".
6. Select a data centre near you.
7. Click "Review".
8. Ensure that all details are correct and then click "Create instance".
9. Copy the database URL
10. Add the database into the setting.py file

You will also need to add the database to your Django settings.py file:

DATABASES = {

'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))

}

[Back to Top](#agape)

# Credits

## Content

Content of the agape website is by jayadeep ravuri

### Images

Images for agape website were taken from pexels.
The logo image in the connect section for the task cards was created in canva.

## Education
*Error Pages*
- [Code institute course material](https://codeinstitute.net/se)
  The course material has helped me to create the backend funtionality of this project.
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow webpage")
  Stack overflow was used to answer questions as to why certain code may not be performing as expected.
- [ChatGPT](https://openai.com/blog/chatgpt "link to chatgpt page")
  ChatGPT was used to gain a better understanding of errors faced.

# Acknowledgements
- Agape group in sweden, who allowed me to build a project for the group and for providing me with ideas.
- Inspiration from the projects of my colleagues at code institute.
- Friends and family who helped test the site on different devices and give real world user feedback


[Back to Top](#agape)
