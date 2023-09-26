<h1 align="center">Dispatch Pro</h1>
<h3 align="center">A delivery schedule dispatching tool</h3>

<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/dp-banner.png" alt="dispatch-pro-banner" align="center"/></p>

---

[Video Presentation](https://youtu.be/3X1Z2U_-6bQ?si=B3M67jzaNGJxBZRx&t=611), presented at Coding Dojo Graduation Ceremony. Timestamps: 10:11 to 19:08

---

## Table of Contents

-   [Background](#background)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Screenshots](#screenshots)
-   [Functionality](#functionality)
-   [Design](#design)
-   [Running Locally](#running-locally)

---

## Background

Having a background in the distribution industry after the Military was my inspiration for this project. I worked for two smaller, family owned businesses, one that eventually became a subsidiary for a national corporation, and one that is still a growing, national, privately-owned business. Though both were vastly different in operation processes and resources, one this remained the same; they both has insufficient means for scheduling their local deliveries.

At both companies, I took it upon myself to develop a Google Sheets version of a delivery schedule so we could meticulously schedule deliveries and display all the valuable information for those deliveries, mitigating the risk for dropping, or forgetting about deliveries.

I took that Google Sheets idea and turned it into a web application that was minimal, but carried all the weight of the most basic needs these companies need for their daily operations.

So, with customer satisfaction and organizational readiness and efficiency in mind, I created Dispatch Pro.

[Return to Table of Contents](#table-of-contents)

---

## Features

-   Login for existing Dispatch Pro customers
-   Dispatch Pro is controlled by the Customer
-   Includes Role-Based permissions and visibility
    -   Admins can create/view:
        -   Users for company
        -   Distribution Centers (DC) for company
        -   Vehicles for company
        -   Drivers for company
        -   Customers and Schedules for assign DC
    -   Regionals can create/view:
        -   Vehicles and Drivers for assigned Region
        -   Customers and Schedules for assigned DC
    -   Dispatchers can create/view:
        -   Vehicles, Drivers, Customers, and Schedules for assigned DC
    -   Operations can create/view:
        -   Schedules for assigned DC
    -   Sales can view Schedules for assigned DC
-   Extensive MySQL Database for storing all essential company information
-   Future Features will include
    -   Route Mapping
    -   Reports

[Return to Table of Contents](#table-of-contents)

---

## Technologies Used

-   Full-stack Python
-   HTML, CSS
-   JavaScript
-   Flask & Jinja2
-   MySQL Database
-   AJAX
-   WTForms
-   SQL-Alchemy
-   Bootstrap
-   Bcrypt
-   Flask Login
-   Email Validator

[Return to Table of Contents](#table-of-contents)

---

## Screenshots

<p align="center">Login & Schedule Screen</p>
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/login.jpg" alt="login-view" width="400"/> <img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/schedule-view.jpg" alt="schedule-view" width="400"/></p>

<p align="center">Create Schedule & Schedule Delivery</p>
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/create-schedule.jpg" alt="create-schedule" width="400"/> <img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/schedule-delivery.jpg" alt="schedule-delivery" width="400"/></p>

<p align="center">Schedule Delivery Demo</p>
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/schedule-delivery-demo.gif" alt="schedule-delivery-demo" width="600"/></p>

<p align="center">Create Trucks/Drivers and Create Customers</p>
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/create-truck-view.jpg" alt="create-trucks-drivers" width="400"/> <img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/create-customer-view.jpg" alt="create-customers" width="400"/></p>

<p align="center">Create DCs and Create Users</p>
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/create-dc-view.jpg" alt="create-dc" width="400"/> <img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/creat-user-view.jpg" alt="create-users" width="400"/></p>

<p align="center">Slide-in Sidebar Nav</p>
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/sidebar-nav.jpg" alt="sidebar-nav" width="400"/> <img src="https://github.com/bobbycoleman-dev/array-v2/blob/main/screenshots/responsive-tablet.jpg" alt="array-banner" width="250"/></p>

---

## Functionality

When first visiting the site, you are brought to the Login screen if you have an account, or you can travel to the Registration screen to create an account. The registration form takes your full name, a selected (unique) username, your email, and password/confirm password. After successfully registering, you are taken to the login screen to login in.

After logging in, your information is stored in your personal browser local storage to maintain your login state even after closing the browser, and you are brought to the home screen which features a navigation on the left, users and trending languages on the right, and the main post feed in the middle.

From the home screen, a user can post code, traverse to their personal profile, view other user profiles, and search all posts in the [Array] array.

A user can view a single post, like that post, and comment on that post. A user can also follow other users and view their own followers.

Because [Array] is fully responsive, a user can also view posts and make posts from their tablet or mobile device.

[Return to Table of Contents](#table-of-contents)

---

## Design

I wanted to take a mobile-first approach to my design while also ensuring it can be comfortably viewed on larger screens and in light or dark mode.

The light mode design has a subtle white to light gray gradient, while the dark mode design has a pleasing blueish green gradient with light green primary colors. Dark mode also features a dark gray code block, making the syntax highlighting easy to read.

The layout of [Array] intentionally leaves the left and right sections static while changing the middle section to display the information the user wants to view such as the feed, a single post, or theirs and other users profiles.

[Return to Table of Contents](#table-of-contents)

---

## Running Locally

1. You will need a MongoDB account, I used [Atlas](https://www.mongodb.com/cloud/atlas/register)
2. You will need a [Firebase](https://firebase.google.com/) account to set up Authentication
3. Clone the repository, run `npm i` to install dependencies
4. Create a `.env` file for both the server and the client
5. Server side `.env` file will need:

    ```env
    PORT=8000
    MONGODB_URI=mongodb+srv://{username}:{password}{db_conection_string}?retryWrites=true&w=majority
    ```

6. Client side `.env` file will need (for Firebase authentication):

    ```env
    # All values auto-generated when creating a Firebase application
    VITE_FIREBASE_APIKEY= {firebase_api_key}
    VITE_FIREBASE_AUTH_DOMAIN= {firebase_auth_domain}
    VITE_FIREBASE_PROJECT_ID= {project_id}
    VITE_FIREBASE_STORAGE_BUCKET= {storage_bucket}
    VITE_FIREBASE_MESSAGING_SENDER_ID= {messaging_sender_id}
    VITE_FIREBASE_APP_ID= {app_id}
    ```

7. Open server in terminal, run `nodemon server.js` to start server
8. Open client in terminal, run `npm run dev` to start client

[Return to Table of Contents](#table-of-contents)
