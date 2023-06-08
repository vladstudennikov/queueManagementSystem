# queueManagementSystem_v3

![appdia drawio](https://github.com/vladstudennikov/queueManagementSystem_v3/assets/91913216/2cce6286-b8db-4fac-b2f9-f8549ce9a672)


Idea:

- Models are used to work with a database, all settings are provided in file setup.py
- All models should inherit AbstractModel, it gives an ooportunity to create another models which would work with different DB`s or file formats
- Business Logic Layer is now represented by QueueController - it is a logic for a queue. Maybe there would be added some new classes
- Validation layer would be used to validate data from users (I wanted to create validation directly in models, but peewee (used orm library) does not provide an ability to validate data before saving.
Also I thought that data validation should be written in business logic, but when I started to write code, I understood that to create classes for manipulating data in business logic, it should be written to many code that was already written in Models. For example, I have created businessLogic for login data, but code here was mostly the same as in Models, and there were too many similar lines of code. Then I have decided to create data validation outside business logic. Is it good decision or it should be written logic for all models?
- Then would be written class to create a web-app. Web-app would fully use logic from Busness Logic Layer and Validators, so it would be needed as a Controller in MVC Model.
