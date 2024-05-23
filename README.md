# Testr

Hi, say hello to Testr!

Testr is an automatic unit and integration testing framework for Python.

Testr works by allowing you to give it a function and a expected output, if the expected output does not match the actual output then Testr will mark that Test as failed!

## Usage

### Creating a Test

To create a test, use the following format:

`Testr.Test(<Function>, <Expected Output>)`

For the duration of this document, the function used in Tests will be called the Reactant and the expected output will be called the Product.

If you would like to provide arguments to the Reactant when the Test is ran, you can add the keyword parameter `ReactantArguments` with a tuple containing the arguments, like this:

`Testr.Test(<Reactant>, <Product>, ReactantArguments=<Reactant Arguments>)`

### Creating a TestingGroup

Testr allows for the creation of another type, called a TestingGroup, a TestingGroup allows you to group tests together and even print them to the console in a pretty format!

To create a TestingGroup, use the following format:

`Testr.TestingGroup(<TestingGroup Name>, <List Of Test Objects>)`

You may also provide the keyword arguments `Exit` and `Print`, both are booleans, `Exit` being `True` will make Testr exit your program after testing the group, and `Print` being `True` will make Testr print the results to the console in a pretty format.

`Exit` has a default of `False` and `Print` has a default of `True`.

### Methods

Both Test and TestingGroup objects support the following methods:

`.Test()`: Execute this Test or every Test in this TestingGroup.

`.GetPassed()`: Return a Boolean or NoneType to whether this Test or TestingGroup passed.

`.GetTested()`: Return a Boolean of whether this Test's or TestingGroup's `.Test()` method has previously been called.

#### Test Exclusive

`.GetReactant()`: Return the reactant that was provided to the Test when it was created.

`.GetProduct()`: Return the product that was provided to the Test when it was created.

`.SetReactant()`: Set the Test's Reactant.

`.SetProduct()`: Set the Test's Product.

#### TestingGroup Exclusive

`.GetPassedTests()`: Return a list of all Tests that passed.

`.GetFailedTests()`: Return a list of all Tests that failed.

`.SetGroupName()`: Set the TestingGroup's name.

`.SetTests()`: Set the Tests for the TestingGroup.