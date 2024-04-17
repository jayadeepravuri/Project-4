# [AGAPE](https://wild-swim-scotland-47f727d45ac1.herokuapp.com/ "take you to the Agape's Deployed Page")

![am-i-responsive-image](documentation/readme-images/am-i-responsive")

# Introduction

The platform was built utilizing Django, boasting comprehensive CRUD operations and an intuitive user interface to facilitate volunteering for agape-related tasks. Users receive alerts in the form of notification boxes for any updates to their accounts or bookings. Administrators enjoy additional privileges, such as the ability to search for volunteers and their selected tasks based on dates and usernames.


[Live Site Here](https://wild-swim-scotland-47f727d45ac1.herokuapp.com/ "take you to the Wild Swim Deployed Page")

# Table of Contents

- [Key Project Goals](#key-project-goals)
- [Agile Development](#agile-development)
- [User Stories](#user-stories)
- [User Experience](#user-experience)
    - [Wireframes](#wireframes)
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

[Back to Top](#wild-swim-scotland)

# Key Project Goals

The goals of the sites functionality are:

- List View: users will get introduced about agape and can view the tasks they can volunteer
- Register: users can register to the site so that they can use the sites functionality 
- Logged In: users have the ability to volunteer for a task in agape and can edit/cancel their volunteering
- Logged Out: users are asked if they wish to sign out of the site
- Admin: can view the task that are volunteered and can also volunteer himself in one of the available tasks

# Agile Development

A Kaban board was used in GitHub to create the agile development process – see the board [here]( https://github.com/users/sarahgoodwin93/projects/3 "Kaban board for Wild Swim Scotland Project")

User stories were labelled using the MoSCoW method.

[Back to Top](#wild-swim-scotland)

# User Stories

4 Epics were created broken down into user stories, the epics included:

1. Admin
2. Staff
3. Site Access
4. User Functions

The user stories are as follows:

## Epic - Admin

### Create staff users

- As an admin, I can use the Django admin panel to create new staff users so that they can create new swims
    - AC1 - Admin can access the Django admin panel
    - AC2 - Admin can create staff users in the Django admin panel
    - AC 3 - New staff users can create, read, edit and delete swims

Tasks 
- Create staff users
- Ensure new staff members can create, read, edit and delete swims

## Epic - Staff

### Create Swim Posts (Full CRUD)

- As a site staff member, I can make new swim posts so that my users can see upcoming swims
    - AC1 - Create new swims by filling out the 'Add Swim' form
    - AC2 - Read the new swim that has been created on the homepage
    - AC 3 - Update/ edit the swim that I have created
    - AC 4 - Delete the swim I have created

Tasks
-  Create 'Add Swim' form on user interface for staff members only to be able to add swims
- Create view so that the added swims will be added to the homepage
- Create authenticated users for that specific swim so that only that staff member can edit the swims they have added
- Create a delete warning message so that staff can confirm they want to delete the swim

## Epic - Site Access

### Log-in and log-out

- As a site user, I can log in with my created username and password to access the site and see my previous actions
    - AC1 - Site user can log in with their created username and password after they have registered to the site
    - AC2 - Site users can see the swims they have registered from a previous login
    - AC 3 - Site user can log out when they have finished their session and confirm they want to log out

Tasks
- Link accounts/login template so that users can sign into the site
- Link accounts/logout template so that users can sign out of the site
- Ensure data is saved from previous login so that users can see their previous swim actions

### Register an account

- As a site user I can register an account so that I can return to see the swims I have booked to join
    - AC1 - User can register account and see site functionality

Tasks
- Create a Register nav link button
- Link 'accounts/sign_up.html' template so that new users can register to the site
- Ensure registered users can see site functionality changed from being logged in vs logged out

## Epic - User Functions

### View wild swim list

- As a site user I can view the wild swims around Scotland so that I can decided if I wish to register and sign up to a swim
    - AC1 - When the site loads, the list of swims is visible to the user both logged and not logged in.
    - AC2 - User can view swim detail without logged in
    - AC 3 - User can join the swim once logged in

Tasks
- Create a swim model to pull data from added swims and view to show the swims on the homepage
- Create user authentication so that only logged-in users can join swims

### Join a swim

- As a logged-in site user, I can click to join a swim so I can make sure there is a place for me on that time and date
    - AC1 - The site can be logged into and the join swim button is not visible to users who are not logged in or registered
    - AC2 - The join swim button then moves that swim card to the Upcoming Swims page where users can revisit their upcoming swims
    - AC 3 - Users can cancel their swim reservation

Tasks
- Ensure the 'Join Swim' button is not visible to unauthorised users
- Create model and view for moving joined swim into upcoming swim page
- Create cancel button which removes the swim from the upcoming swim page

## Future Stories

Future user stories were also created for the following:

- Commenting on swims
- Adding reviews to site
- Editing account details


# User Experience

## Wireframes

![HomePage](documentation/readme-images/wireframe.png "Lucid image")
![SignIn ](documentation/readme-images/wireframe.png "Lucid image")
![SignUp ](documentation/readme-images/wireframe.png "Lucid image")
![VolunteerForm Page](documentation/readme-images/wireframe.png "Lucid image")
![Volunteer Home ](documentation/readme-images/wireframe.png "Lucid image")
![Volunteer Home Admin](documentation/readme-images/wireframe.png "Lucid image")
![Volunteer Detail](documentation/readme-images/wireframe.png "Lucid image")
![Profile](documentation/readme-images/wireframe.png "Lucid image")

Site structure was created before the site was created to test layout idea.

## Database Schema

The project uses ElephantSQL as PostgreSQL relational database for storing the data.

The data schema was created using [Lucid Chart](https://www.lucidchart.com "Lucid Chart") before the project was started to get the flow and function of the models. 

![Data Schema Image](documentation/readme-images/new-data-schema.png " Data Schema Image ")

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
  
![Color palette Image](documentation/readme-images/colour-palette.png "Color palette Image ")

### Logo

The logo used in the head section is agape community's official logo. Permission was taken to use the logo

![Logo Image](documentation/readme-images/ws-logo.png " Logo Image ")

## Design Choices

I aimed for the website's design to convey a sense of warmth and hospitality to visitors. My goal was to ensure that navigating the site would be effortless and intuitive, providing users with easy access to the information they seek. Rather than overwhelming visitors with excessive details about Agape, I focused on presenting essential information in a clear and concise manner. Through strategic decisions, I endeavored to introduce Agape in a manner that would resonate positively with users.  

![Swim Card](documentation/readme-images/swimcard.png " Swim Card Image ")

[Back to Top](#wild-swim-scotland)

# Features

## Existing Features

## Non-Logged in User

### The Landing page And General Site Content

![Homepage](documentation/readme-images/homepage.png " Home page image ")

The landing page of the site of a non logged in / non registered user introduces them to agape and motivates them to volunteer for the tasks for agape . 
The page sections 
*values, and about us* intorduces the site visitor to agape and motivates them to volunteer for the tasks presented in the *connect* page section. 
Further , the page sections *contact*, is provided to give the location and contact the admin for feedback and queries
The landing page has 2 call to actions, *Register* and *Login*. 
The landing page is responsive for different screen sizes and scales down for easy mobile or tablet use. 

### Login

![login](documentation/readme-images/login.png " login image ")

The login page welcomes the user back to the site and has 2 clear options, username and password.
The design is friendly and approachable by using rounded corners on the input boxes.

The text at the bottom of the login section lets users know they must be logged into the site to use the full functions, it offers them an action if they have not yet registered by using the sign up link.

If the username and password are not correct this error will show.

![username error](documentation/readme-images/username-error.png " username error image ")

### Register

![register](documentation/readme-images/register-form.png " register form image ")

The register page welcomes users to the site with a friendly greeting. It lets users know that in order to use the site functions they must register an account.

It offers them space for a username, email(optional) password and then rechecks the password to ensure it matches and there were no errors.
An example of some of the errors:

![register form errors](documentation/readme-images/register-form-errors.png " register form errors image ")

The text at the top lets users know who already have an account that they can sign in using the login page.

## Logged in User


### Volunteer form page

![Volunteer form page](documentation/readme-images/join-swim-button.png "joined-swim-button image ")

The user will notice when the have logged in is that there is now more information regarding the volunteering oppurtunities and when agape happens. 
The user can now choose the task he wants to volunteer, the date he wants to volunteer, write an additional message regarding the task he chooses to volunteer. 
He can further notify the user and request for a covolunteer.
Now the user submits the form by cliking on the volunteer button and is redirected to the Volunteer home page 
additionally errors will be displayed, if the user chooses a task/date which is not available, an error message is displayed. also, if the user chooses a date in the past or if the date is not a wednesday, an error message is displayed.

### Volunteer home page

#### Logged in user
![Volunteer home page](documentation/readme-images/join-swim-button.png "joined-swim-button image ")
Now the user is taken to the page where he can view all the tasks that he has choosen to volunteer on the left and his account details on the right.
when clicked on the card he is redirected to the volunteer-detail page, where he can edit or cancel his volunteering.*(more on volunteer-detail page is explained in the section below)*
Furthermore, the user can update his account information by clicking on the account details button.
Also, the user can choose to volunteer for more tasks by clicking the volunteer button below the account details button.

#### Admin
![Volunteer home page](documentation/readme-images/join-swim-button.png "joined-swim-button image ")
For an admin, the volunteer home page is similar as an normal user, but he is provided with an additional search form on the right coloumn, 
where he can search for tasks the the user have choosen to volunteered by name or date or both. 
On the left column, admin can view all the volunteerings by default and is changed according to the search filter options.

### Volunteer-detail page

#### Logged in user
![joined swims](documentation/readme-images/joined-swim-page.png " joined-swim-page image ")

when the user clickes on his volunteering card he is redirected to the volunteer detail page. 
He is now displayed with the choosen volunteer card , which gives the information like the date of volunteering, task, requested volunteer(if requested), confirmed/not confirmed yet. and 3 additional buttons.
When clicked on the Edit Volunteering button, the user is directed to the volunteer form page with the predefined user choices, where he can further make changes to his volunteering task.[no swims joined](documentation/readme-images/no-swims-yet.png " no-swims-joined image ")
when clicked on the cancel volunteering button, he is directed to the dete volunteering page, 
where the user is asked again if he wants to delete his volunteering task![no swims joined](documentation/readme-images/no-swims-yet.png " no-swims-joined image ")
when clicked on back button, the user is taken back to the volunteer home page

### Logout

![logout](documentation/readme-images/logout.png " logout image ")

The logout page checks if the user does wish to sign out of the site.

## Future Features

There are some future features that I would like to add to the project to improve user functions.

- Email notifications:
  It would be nice to notify users regarding their tasks they have choosen to volunteered, and also, notify them when the admin confirms their task.
- Social media signup
- can add a profile picture and update their account information.
 
[Back to Top](#wild-swim-scotland)

# Technologies Used

- [Lucidchart](https://www.lucidchart.com/ "link to Lucidchart homepage")
Lucidchart was used to create the wireframe in the planning stages of the project
- [drawSQL](https://drawsql.app/ "Drawsql homepage")
Drawsql was used to create the data schema
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
Used to host images for the swim cards
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

[Back to Top](#wild-swim-scotland)

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
- Friends and family who helped test the site on different devices and give real world user feedback


[Back to Top](#wild-swim-scotland)
