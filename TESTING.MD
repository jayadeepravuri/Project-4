# Wild Swim Scotland Testing

Return to [README.md](README.md)

# Table of Contents

- [Code Validation](#code-validation)
    - [W3C HTML Validation Results](#w3c-html-validation-results)
    - [W3C CSS Validation Results](#w3c-css-validation-results)
    - [JSHint Validation Results](#jshint-validation-results)
    - [CI Python Linter Validation Results](#ci-python-linter-validation-results)
- [Manual Testing](#manaul-testing)
    - [Home Page](#home-page)
    - [Register Page](#register-page)
    - [Login Page](#login-page)
    - [Homepage as Logged in user](#homepage-as-logged-in-user)
    - [Upcoming Swims](#upcoming-swims)
    - [Logout](#logout)
    - [Homepage as staff user](#homepage-as-staff-user)
    - [Add Swim](#add-swim)
    - [Edit Swim](#edit-swim)
    - [Delete Swim](#delete-swim)
    - [Other Testing](#other-testing)
    - [Responsiveness testing](#responsivness-testing)
- [Browser Compatibility](#browser-compatibility)
- [User Testing](#user-testing)
- [Accessibility Testing](#accessibility-testing)
- [Known Bugs](#known-bugs)


# Code Validation 

## W3C HTML Validation Results

All HTML code has been run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary> W3C HTML Errors Found and fixed</summary>

index.html

![index.html errors](documentation/testmd%20images/index.html%20error%20.png "index.html error image")

profile.html

![profile.html errors](documentation/testmd%20images/profile%20error.png "profile.html error image")

</details>

After testing all errors were fixed and document checking complete was shown for all pages



| **SOURCE CODE TEMPLATE** | **RUN THROUGH VALIDATOR** | **ANY ERRORS** | **ERRORS RESOLVED** |
| -------- | ---------- | --------------- | -----------|
| base.html | Yes | No | N/A |
| index.html | Yes | Yes - detailed image above | Yes, retested and all passed |
| volunteer_form.html | Yes | No | N/A |
| volunteer_home.html | Yes | No | N/A |
| volunteer_detail.html | Yes | No | N/A |
| volunteer_confirm_delete.html | Yes | No | N/A |
| profile.html | Yes | Yes - detailed image above  | yes |
| signup.html | Yes | No| N/A |
| login.html | Yes | No | N/A |
| logout.html | Yes | No | N/A |

## W3C CSS Validation Results

All custom CSS has been run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "jigsaw w3 page")

No errors were found when running CSS through w3c validator

![css w3c](documentation/testmd%20images/css%20no%20error.png "css validator image")

## JSHint Validation Results

No javascript was used for this project.

## CI Python Linter Validation Results

All python code that was written following PEP8 guidelines and was run through the [CI Python Linter](https://pep8ci.herokuapp.com/ "ci python linter page")

Every python file in the connect app, home app and agape project were tested against PEP8 guidelines and no errors were found. 

E501 rule in the strings of all the python files were neglected

# Manual Testing

## Home Page

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Homepage with images | Opened site url | Renders Homepage | Worked as expected | N/A |
| Nav Links | Opened site url | Only register and login nav links are visible | Worked as expected | N/A |


## Register Page

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Registration Form | Clicked on register nav link | Register form is displaying | Worked as expected | N/A |
| Username | Typed in @£$%^ as username | Warning will show | Warning showed 'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.' | Worked as expected |
| Username | Typed in admin as username | Warning will show | Warning showed 'A user with that username already exists.' | Worked as expected |
| Password 1 | Typed in password same as username | Warning will show | Warning showed 'The password is too similar to the username.' | Worked as expected |
| Password 2 | Typed in password different to password1 | Warning will show | Warning showed 'You must type the same password each time.' | Worked as expected |
| Sign Up Button | Click Sign Up | Button takes user to logged in user to volunteer home | Worked as expected | N/A |
| Login Button | Clicked on login link | Get taken to login page | Worked as expected | N/A |

## Login Page

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Username | Typed in random username | Warning will show | Warned showed 'The username and/or password you specified are not correct.' | Worked as expected |
| Password | Typed in incorrect password | Warning will show | Warned showed 'The username and/or password you specified are not correct.' | Worked as expected |
| Sign In | Typed in correct username and password, pressed sign up | Button takes user to logged in user to volunteer home | Worked as expected | N/A |
| Sign Up | Clicked on Sign Up link | Get taken to register page | Worked as expected | N/A |

## Homepage as Logged in user

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Nav links | Log in and go to homepage | Nav bar is updated with Volunteer,My account and Logout navlinks | Worked as expected | N/A |
| Volunteer button | Click on Volunteer button on connect section | Directs to Volunteer home page | Worked as expected | N/A |
| Volunteer_form Page | Click on Volunteer button on Navbar | Directs to Volunteer home page | Worked as expected | N/A |

## Volunteer_form Page (logged in user and admin)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Volunteer_form Page | Click on Volunteer button on Navbar | Directs to Volunteer form page | Worked as expected | N/A |
| Form validation | Enter invalid date | shows error message | Worked as expected | N/A |
| Form validation | choose unavailable volunteering opportunity | shows error message | Worked as expected | N/A |
| Volunteer button | Click volunteer button | should take you to volunteer home and show sucess message | Worked as expected |

## Volunteer_Home Page (logged in user)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Volunteer_Home Page | Click on My Account button on Navbar | Directs to Volunteer home page | Worked as expected | N/A |
| Show volunteering card | Volunteer through volunteer_form | Display Volunteering card with all details in main coloumn | Worked as expected | N/A |
| volunteering card | Click on the Volunteering card | should take you to volunteering detail page | Worked as expected | N/A |
| Show no upcoming tasks | Create no volunteering and open My account page | Display "No upcoming tasks with Volunteer button below it" | N/A |
| Your Account coloumn | Open My account page | Display username and Email details of the user | Worked as expected | N/A |
| Account details button | Click on Account details button | Take you to Account informations page | Worked as expected | N/A |
| Volunteer button | Click volunteer button | should take you to volunteer form page  | Worked as expected | N/A |
| Paginate | Create multiplte volunteerings | Should create a next and prev button in the bottom of the main column | Worked as expected | N/A |

## Volunteer_Home Page (Admin)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Volunteer_Home Page | Click on My Account button on Navbar | Directs to Volunteer home page | Worked as expected | N/A |
| Show All volunteering cards | Go to Volunteer_home page | Display All Volunteering cards that was created | Worked as expected | N/A |
| volunteering card | Click on the Volunteering card | should take you to volunteering detail page | Worked as expected | N/A |
| confirm volunteering | Click on the Volunteering card and display confirm button | should take you to volunteering detail page,and Display confirm button  | Worked as expected | N/A |
| Show no upcoming tasks | Delete all the volunteerings | Display "No upcoming tasks with Volunteer button below it" | N/A |
| Your Account coloumn | Open My account page | Display username and Email details of the user | Worked as expected | N/A |
| Search volunteers form | Open volunteer_home page | Display search form on the left column | Worked as expected | N/A |
| Search volunteers form validation | select invalid and/or unavailable dates and usernames/tasks and click search | Display error message | Worked as expected | N/A |
| Search volunteers form validation | select valid and/or unavailable dates and usernames/tasks and click search | Display volunteering cards accordingly | Worked as expected | N/A |
| Search volunteers form validation | select valid and/or unavailable dates and usernames/tasks click reset | Display all volunteering cards and clear search form | Worked as expected | N/A |
| Account details button | Click on Account details button | Take you to Account informations page | Worked as expected | N/A |
| Volunteer button | Click volunteer button | should take you to volunteer form page  | Worked as expected | N/A |
| Paginate | Render volunter_homepage with multiple volunteerings | Should create a next and prev button in the bottom of the main column | Worked as expected | N/A |

## Volunteer_Detail Page (logged in user)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Volunteer_detail page | Click on volunteering card | Directs to Volunteering detail page | Worked as expected | N/A |
| Edit volunteering Button | Click on Edit volunteering button | Directs to Volunteering form page with predefined choices and redirect you to volunteer home with a success message if the form input is validated | Worked as expected | N/A |
| Cancel volunteering Button | Click on Cancel volunteering button | Directs to confirmDeleteVolunteer page | Worked as expected | N/A |
| Back Button | Click on Back  button | Directs to Volunteer_Home page | Worked as expected | N/A |

## Volunteer_Detail Page (Admin)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Volunteer_detail page | Click on volunteering card | Directs to Volunteering detail page | Worked as expected | N/A |
| Confirm  Button | Click on Confirm volunteering button | confirm button should be disappear and should say confirmed when clicked on it | Worked as expected | N/A |
| Edit volunteering Button | Click on Edit volunteering button which is available only on admin's volunteerings | Directs to Volunteering form page and redirect you to volunteer home with a success message if the form input is validated | Worked as expected | N/A |
| Edit volunteering Button | click on users volunteering |  Edit button should not be present  | Worked as expected | N/A |
| Cancel volunteering Button | Click on Cancel volunteering button, which is available for all volunteerings | Directs to confirmDeleteVolunteer page | Worked as expected | N/A |
| Back Button | Click on Back  button | Directs to Volunteer_Home page | Worked as expected | N/A |

## Confirm_delete_volunteering (logged in user and admin)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render Confirm delete volunteering Page | Click on Cancel volunteering in detail page | Directs to confirm delete volunteering page | Worked as expected | N/A |
| Yes,Delete! button | Click on Yes,Delete! button | should take you to volunteer home and show sucess message, with the volunteering card disappered | Worked as expected | N/A |
| Cancel Button | Click on cancel button | Redirects to Volunteer_detail page | Worked as expected | N/A |

## Profile Page (logged in user and Admin)

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Render profile page | Click on Account details button in volunteer_Homepage | Directs to Volunteering detail page | Worked as expected | N/A |
| Form validation | Click on update button with invalid username and/or email | Show error message | Worked as expected | N/A |
| Form validation | Click on update button with valid username and/or email | Directs to Volunteer_Homepage with success message and updated account information | Worked as expected | N/A |

## Logout

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Logout | Clicked logout from nav bar | Message asking 'Are you sure you want to sign out?' | Worked as expected | N/A |
| Sign Out button | Clicked sign out | Redirected to homepage as non logged in user | Worked as expected | N/A |

## Other Testing

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| 404 Error | Typed /hello at end of url | 404 error page to show | Worked as expected | N/A |
| URL Access | Typed /swim/add at end of url | 404 error page to show | Taken back to login page | Warning could be added to show to user what happened rather than redirect |
| URL Access | Typed /article/add at end of url | 404 error page to show | Taken back to login page | Warning could be added to show to user what happened rather than redirect |

## Responsiveness testing

| **DEVICE** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Samsung20 FE | Tested site on mobile | Site functions and is responsive | Worked as expected | N/A |
| iPhone 15 | Tested site on mobile | Site functions and is responsive | Worked as expected | N/A |


## Browser Compatibility

The site was tested on the following browser types

* Google Chrome
* Microsoft Edge

## User Testing

A user testing form was sent to friends and family to test the site on their devices and get real world feedback from people who had not been involved in the creation of the site.

Feedback from the form

* Made small corrections and changed some text and spelling mistakes in the homepage
* User testing did not throw many errors as users followed instructions
* Users found it easy to view, create, edit and deleate the and delete the volunteering
* Users found it easy to create an account and navigate the website 

### Things to implement from user testing

* Made small corrections and changed some text and spelling mistakes in the homepage

# Accessibility Testing

## Lighthouse

Google Lighthouse test from the dev tools was used to test the pages on the site for 

* Performance
* Accessibility
* Best Practices
* SEO

Examples of results are as follows:

<details>
<summary> Home </summary>

![home lighthouse](documentation/testing-images/lighthouse-home.png " hoem lighthouse image")

</details>

<details>
<summary> Upcoming Swims </summary>

![joined_swmis lighthouse](documentation/testing-images/lighthouse-joined-swim.png "joined swim lighthouse image")


</details>

<details>
<summary> Add Swim </summary>

![Add Swim lighthouse](documentation/testing-images/lighthouse-add-swim.png "add swim lighthouse image")

</details>

<details>
<summary> Logout </summary>

![logout lighthouse](documentation/testing-images/lighthouse-logout.png "logout lighthouse image")

</details>

# Known Bugs

## Resolved

Error in the console was showing a Mixed Content Error

![mixed content error](documentation/testing-images/mixed-content-error.png "mixed content error image")

This error was typed into Google and the [Stack Overflow](https://stackoverflow.com/questions/67765238/mixed-content-the-page-at-was-loaded-over-https-but-requested-an-insecure-resour "stack overflow mixed content error") question for the error gave the answer.

The meta tag <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests"> was added to the base.html and the error was resolved.

## Unresolved 

No known unresolved bugs

Return to [README.md](README.md)



