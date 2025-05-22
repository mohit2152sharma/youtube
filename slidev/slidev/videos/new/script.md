Suppose you are writing a database connector.
You create a class database connector and when you create an instance of it
it creates a connection
But there is a design flaw in it, can you see it?

Welcome .....
And today I am taking about `__new__` magic method

Going back, so what's the design flaw?
It creates a new connection every time you create a new instance.
If you create too many instances i.e. too many connections you will get an error
as postgres/mysql have connection limits.
There is more than one way to solve for this.
A hackish way would be to create one instance in global and then reuse it.
Alternative, I think much better way is to use the `__new__` method.

Normally when you create a class, you define the `__init__` method this is initialisation method
This is called when you are to initialise the instance i.e. sets up the attribute, the object.
But before `__init__`, new method is called, which creates the actual object in memory and you can use this
to implement a singleton pattern.

# final script

Suppose you are writing a database connector
it has a connect method which creates a connection to the database
and whenever you create an instance
it connects to the database using the connect method
Looks good enough, but there is one issue with it

Welcome to one minute python and
today I am talking about singleton pattern
and the new magic method in python classes

So what's the issue,
whenever you create a new instance
you are creating a new connection
and if you create too many instances
you will create too many connections
and you will start encountering the too many clients error in postgres
this is because postgres has a connection limit
intuitively you can already guess the solution
i.e. whenever we create a new instance we do not create a new connection, instead reuse it

To solve for this, we can use singleton design pattern
it ensures that there is only instance of a class and that instance is globally accessible
normally when you create a class, you use the init method
this method initialises the instance and sets up the instance attributes
But there is also a new method which is responsible for creating the instance in memory
This is called before init method
We can use it to implement singleton pattern
We create a class attribute and use it track if the instance is already created or not
if the instance is not created
we create a new instance and assign it to the class attribute
and then return the instance

Going back to our example of database connector
we create two class attributes
instance and connection to track the creation of instance and connection
if the instance is not created
we create a new instanec
and we create a new connection by calling the connect method

So in this example,
the first time i create an instance
the print statements inside new method will be printed.
but the next time i create the instance only the print
statements inside init method will be printed
We can use is operator to confirm both the instances are actually the same.

One important thing to note,
it's important to pass args and kwargs to the new method
if the init method expects any parameters.
Since new method is called before init method
the parameters you pass while creating the instance will be passed to the new method first and it should be able to accept those parameters.
Also notice the order in which the print statement appears this shows that new method was called before init method
