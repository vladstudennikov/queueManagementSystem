# $${\color{lightblue}Queue \space management \space system}$$
Below would be described how to use this app and how it could be changed and modified.

## Table of contents
* [The purpose of the application](#the-purpose-of-the-application)
* [Technologies](#used-technologies)
* [Installation](#installation)
* [General information](#general-information)
* [API](#queue-management-system-api)

## The purpose of the application

This application was developed for managing queues in business establishments and could help to increase productivity of work. Lately it would be disscussed in more details how queue controlling could help businesses.
Application consist of 2 independent parts: queue management system component, which could be used to implement different queue management system (see paragraph 4 - queue management sysytem API), and web-app which uses this API.

## Used technologies
- SQLite database;
- ORM: peewee;
- Flask (Flask Admin, Flask Login, WTForms, sessions);

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

### Used terminology:
- Customer - a person who should be served by a business establishment;
- Serve a customer - providing a product or service that the customer would like to receive;
- Operator - company representative who can serve a customer;
- Workplace - area where the services are provided by an operator;
- Admin - person who has an ability to add new customers to a queue and can observe the state of a queue;
- Monitor - electronic device for showing current state of the queue (customers who are waiting to be served, operators and customers who are served by each of them);
- Superuser - person who can add data to a database;

### Usertypes in the app: 
Usertypes: operator, monitor, admin, superuser. Data about each user, their logins and passwords are stored in the database.

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

## Queue management system API

App may be divided into 3 parts:
- Models;
- Business logic;
- Web-app;

Models are stored in "Models" folder (app/Models). 
Business logic incldes 3 files:
- QueueServices - control of queue;
- LoginController - class for getting userdata by login and password;
- Models logic - set of classes for adding and deleting models.
- Validators - classes for data validation.

#### Models:

Models were written using peewee ORM, but you can create your own models without changing other parts of the app.
To create own models, they should be inherited from AbstractModel class. This is an abstract class where defined all method that should contain a Model class. If custom models would not be inherited from AbstractClass, then it would be raised Exception and app would not work.
Path to a database and tablenames from where Models get data are written in file "setup.py". You can easily create own database and set link to it in this file.

#### QueueServices:

In QueueServices you can find all necessary method to work with queue. 
It consist of list of customers (it is actually a queue) and list of workspaces, to each workplace attached a customer.

#### ModelsLogic:

ModelsLogic is needed to check data before its adding. Actually classes from this file are not used in this particular program.
In this file you can find 2 abstract classes: ModelAdder and ModelRemover, each class for adding data or its deletion should be inherited from those classes.
In this file you can find class PeeweeModelAdder, it is needed to validate data before its adding to a database. Class for deleting objects from a database could be also implemented.

#### Validators:

In ModelsLogic data validation is used, it is needed to check correctness of the data. 
All validators should be inherited from `ValidatorModel` class.
There are several validators implemented: validator for email, name, surname and id. To validate all values from a particular list ValuesVaidator class is used. It is needed to valuidate data from a whole model, not just one field. 
Own validation: To implement yout own data validation classes, they need to be inherited from ValidatorModel class. Also name of the value that is validated by written class and the classname itself should be added to `validationsetup`.

#### LoginController:

The task of this class - to get data about particular user from login and password.

#### Facade:

All methods from all classes described above are added to 1 class - BusinessLogic. This class is needed to make it simpler to work with logic of the app on its upper layers.
