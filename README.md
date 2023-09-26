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
<p align="center"><img src="https://github.com/bobbycoleman-dev/dispatch-pro-flask/blob/main/screenshots/sidebar-nav.jpg" alt="sidebar-nav" width="400"/> </p>

---

## Functionality

After a company Admin has been created by Dispatch Pro, the Admin can create Distribution Centers (DC) for their organization and create company users and assign them to their respective DC. Once a user has an account, they can login with their default password and they will be greeted with their blank schedule dashboard.

From the dashboard, the user can navigate to the Vehicles/Drivers tab and begin adding their DC Vehicle and Driver information, first creating Drivers so they can then have a Truck assigned to them. Admins can create Trucks and Drivers for the whole company should they choose, Regionals can do the same for the DC's in their Region (i.e. South, Northeast, West, etc.), and Dispatchers can do the same for their assigned DC.

Next, users can navigate to the Customers tab and begin adding in their customers first, then creating addresses for those specific customers.

Once the Drivers, Trucks, and Customers are created, the user then can begin creating weekly schedules for each truck and begin scheduling deliveries.

[Return to Table of Contents](#table-of-contents)

---

## Design

My design approach was minimalistic. Keeping in mind that the target audience (smaller, busy distribution companies that make multiple local deliveries daily) may not have the time or resources to figure out how to use a large application with many features they do not necessarily need.

The main focal point of the application is the delivery schedule, so developing a simple,clean, and unobstructed weekly view of a the DCs truck schedules was critical. Additionally, once the users spend the extra time on the front-end creating customers, trucks, and drivers, the rest of their time will be spent on the schedule dashboard screen. Lastly, creating a sliding navbar with icons was essential for ensuring full screen real estate for the schedule.

[Return to Table of Contents](#table-of-contents)

---

## Running Locally

TBD

[Return to Table of Contents](#table-of-contents)
