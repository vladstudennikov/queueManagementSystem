# queueManagementSystem_v3

![appdia drawio](https://github.com/vladstudennikov/queueManagementSystem_v3/assets/91913216/2cce6286-b8db-4fac-b2f9-f8549ce9a672)


Idea:

1. Models are quite simple classes, they are used for working with a database. Models are written using ORM peewee, but it is possible to create own models that would work with different files or databases. Own models should be inherited from class "AbstractModel" and should have all methods from this class. So it is possible to create models that will work with some other databases, files (XML, binary etc). If model would not be inherited from AbstractModel, business logic could not work with it.
2. Logic is represented with class QueueController (name should be changed, as it is not a controller, but a part of business logic). In this class we have all methods for working with queue.
3. I think, that it is needed to have a logic for adding objects to DB, or for their deleting, to prevent errors in database. For this classes "ModelsAdder" and "ModelsRemover" were made. It is abstract classes, they are needed to have several logic classes that would work with different data (another databases, XML files etc). To create logic for a particular data storage, classes for this task should be inherited from foregoing abstract classes. Until now  was created a class "PeeweeModelAdder". It validates input data and checks whether adding could be commited.
4. Data validation: data validation is an automated process: to validate fields, fieldname should be added to a dictionary "validationsetup" (Validators.py), and then should be specified a class for validation of this field. Classes for validation should be inherited from class "ValidationModel" and have a method named "validate" that returns boolean value (true if the field is correct, false - incorrect). For validating of all fields of some classes it is needed to create ValuesValidator object and call method "validate". This method would check in "validationsetup" what values should be validated and will call method "validate" from each validation class from "validationsetup".
