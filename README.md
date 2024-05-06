# $${\color{lightblue}Queue \space management \space system}$$
Below would be described how to use this app and how it could be changed and modified.

## Table of contents
* [The purpose of the application](#the-purpose-of-the-application)
* [Technologies](#used-technologies)
* [Installation](#installation)
* [General information](#general-information)
* [Detailed description](#detailed-description)

## The purpose of the application

This application was developed for managing queues in business establishments and could help to increase productivity of work. Lately it would be disscussed in more details how queue controlling could help businesses.
Application consist of 2 independent parts: queue management system component, which could be used to implement different queue management system (see paragraph 4 - queue management sysytem API), and web-app which uses this API.

## Technologies
- Python;
- ORM: peewee;
- HTML, CSS, JS;
- JQuery;
- Flask (with Flask Login and Flask Admin);

## Installation

- Download app as an archive;
- Unpack archive;
- Unpack "venv" forlder - it contains all necessary libraries for launching the app;
- Open console;
- Go to the project folder;
- Activate virtual environment:

```bash
cd venv/Scripts
activate
```

- Go back to the project folder:

```bash
cd ../..
```

- Launch app:

```bash
py app.py
```

- Now you can open browser and type 127.0.0.1:5000/login to open web-application
- To use app in local network type server ip-adress in the app.py:

```python

if __name__ == '__main__':
  app.run(host = "<your_ip_adress>")

```

## General information

### Terminology:
- Customer - a person who should be served by a business establishment;
- Serve a customer - providing a product or service that the customer would like to receive;
- Operator - company representative who can serve a customer;
- Workplace - area where the services are provided by an operator;
- Admin - person who has an ability to add new customers to a queue and can observe the state of a queue;
- Monitor - electronic device for showing current state of the queue (customers who are waiting to be served, operators and customers who are served by each of them);
- Superuser - person who can add data to a database;

### Usertypes: 
The app provides separate functionality for several types of users: operators, admins and superusers. Admins can add new customers to the queue, operators can serve them and superusers can set up the whole system. 

### How queue management system works from client`s side:
When customer come to the establishment, he should enter the queue, which could be done with the help of administrator. Each visitor in the queue has a number, we can say that the visitor in the queue is represented by this particular number. Lets call this number as the position in the queue. Suppose after entering the queue customers position is 6.
After the visitor has queued, his number will appear in the queue shown on a screen.

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/67be4a7e-358c-46a5-aa42-adf57a26fb02)

When a customer is ready to be served, his number will appear in the center of a screen with the workplaces id and would disappear from the queue. Customer should come to the workplace where he can be served.
When customer is served, his id and workplaces id would disappear:

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/d81519d5-8a64-495f-a405-066b6d018680)

### Logging in:
To use an app user should enter the system firstly. A start screen of the app is shown below.

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/d5e70ba0-bfaa-43f6-bc01-8ee464e321c6)

After entering login and password user would be redirected to a necessary page. Note that if you logg in once, you will not have an access to other pages of the app and will see a page with error message.

### Monitor page:
Monitor page was already shown in paragraph 3. In the right part of the monitor queue is shown, in the left part of a monitor operators with customers that could be served by them are shown.
Monitor:

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/44a49b5e-fc64-47d7-b5bc-b52bc7cf2609)

### Administrator`s page:
Page for administrator is shown below:

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/db259ceb-88dd-486f-a38b-b997141260cc)

Admin can see the queue, operators and customers attached to them, operators states (states would be disscussed in more details later) and can add customers by pressing a button. Button "Show tickets" is now does not have any functionality, as function for printing tickets was not added yet.

### Workplace page:
Page of operator is shown below.

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/a9b81eaa-68c5-4514-a117-aeae3fb1b51f)

We can see, that on the page some brief information about operator, queue and operators with attached customers are shown. 
Operator can change the state of his workplace, there are 2 possible states that workplace can have: busy and free. When the state is "busy", operator does not have an ability to serve customers (he may have a break, he may depart or serve a visitor). When workplace is free, new customer can go to it.
When operator is ready to serve a customer, he changes the state to "free". When the operator started to serve a customer, he should change his state to "busy". Then, if customer was served and operator is ready to serve someone new, he should change his state to "free".
As you can see, there are 2 buttons for changing state.

### Working with a database:
You can add new operators, monitors and admins and their data for logging in to this app. For this enter the system with the superuser login data and you will see next page:

![image](https://github.com/vladstudennikov/queueManagementSystem/assets/91913216/1590dbfa-ea3c-476b-b47d-713ff1f9313e)

Adding of new data and its deletion is quite simple and clear, so it would not be disscussed. But to configure the application, you need to remember that workplace has a state, not the operator, so if you want to add an operator to the system, you need to add his data and assign it to the workplace. If you would simply add operator`s data, he will not be shown in the system and you will not have an ability to enter his page.
Why we have separated workplaces and operators: different operators can work at different workplaces, for example, different operators can work at one workplace in different shifts, so it is necessary to be able to configure the workplace.
If you want to add login data, you should remember that passwords itself are not stored in the database to protect login data of the users, so users should remember their passwords. Password could be changed by superuser if user has forgotten it.

## Detailed description

App may be divided into 3 parts:
- Models;
- Business logic;
- Web-app;

### Models

Models are used to simplify work with the database. Each model represents particular table from the database.
Models are stored in Models folder (./app/Models). In this folder you can find next classes:
- Admin;
- Monitor;
- Operator;
- Workplace;
- AdminLoginData, OperatorLoginData, MonitorLoginData;
To see how to work with thid models you can read documentation of peewee library (see References).
You can add your own models easily - you should simply inherit it from BaseModel class. BaseModel describes a set of functions that are needed to be in each model - save(), delete(), get() and update(). Also BaseModel determines the database with which models would work, so in case of adding your own models change the link to a database here.
You can place any data for setting up your models into file setup.py.

### Business logic

Business logic (or BL) is a set of more abstract functions over the Models. 
In BL you can find main class for managing queue - QueueServices. This class represents the queue and contains next methods:
- addCustomer(id) - adding new customer to the queue. If there are some workplaces where operators are free, then new customer is being attached to the free operator.
-  getWorkplaces() - returns all data about workplaces;
-  getListOfCustomers() - returns full list of customers.
-  changeWorkplaceState(workplaceid, state) - change the state of particular workplace to another. This method changes the state and assigns a new customer to the workplace if operator that works in this workplace is free.
Methods in QueueServices could throw InvalidDatatypeException in case of invalid datatype of the parameter and WorkplaceWasNotFound is case if we are trying to work with an absent workplace. 

Customers are described in eponymous class, the only field that the customer has is an id.

LoginController is the class that has ony 1 method - getUser() - it returns the data about user using his login and password. 

In BL also implemented some additional logic for working with models for validating data before its adding into db. For it was created the class ModelAdder - an abstract class that has one method - add(). If you want to add your own logic of adding data into db using models, you should inherit your class from ModelAdder. There was implemented the class PeeweeModelAdder inherited from ModelAdder. This class provides validation of data bafore its adding into database. For future, it was created class ModelDeleter - an abstract class that describes the logic of removing data from db in BL layer.

The class in which all necessary functions could be found to work with queue is BusinessLogic. All methods from all classes were added into this class. This class is an only class needed to work with the full system.

### The app

Using BL was created the web-app using Flask, Flask-Login and Flask-Admin. If file app.py the app on Flask is fully given - here you can find some configuration of Superuser page and all controllers. Superuser data is given in a file superuser_data.py - add your own password hashed with md5 before start sorking with an app. Good luck!
