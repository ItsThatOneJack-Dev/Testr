import colorama

TestStructure = {}

def PrintTestingGroupResults(Data, Index):
    Tabs1 = "   " * Index
    Tabs2 = "   " * (Index + 1)
    for Key in Data:
        print(f"{Tabs1}{Key}:")
        Value = Data[Key]
        if isinstance(Value, dict):
            PrintTestingGroupResults(Value, Index + 1)
        elif isinstance(Value, (list, tuple)):
            for Item in Value:
                if isinstance(Item, (list, tuple)):
                    for Subitem in Item:
                        print(f"{Tabs2}{Subitem}")
                else:
                    print(f"{Tabs2}{Item}")
        else:
            print(f"{Tabs2}{Value}")

class TestingGroupError():
    def __init__(self, Header, Message):
        print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}An error has occured: {Header}{colorama.Style.NORMAL}\n{Message}{colorama.Style.RESET_ALL}")
        exit(9)

class Test:
    """
    A Test, can be used to create automated unit or integration tests.

    Use the `.Test()` method to run the Test.

    Arguments:
        Reactant           - The function object to test.
        Product            - The expected output of the Reactant.

        ReactantArguments  - A tuple of the arguments to provide to the Reactant.
    """
    def __init__(self, Reactant, Product, *, ReactantArguments:tuple):
        self.Reactant = Reactant
        self.Product = Product
        self.ReactantArguments = ReactantArguments
        self.Tested = False
        self.Passed = None
    def Test(self):
        ReactantResult = ""
        ReactantResult = self.Reactant(*self.ReactantArguments)
        self.Tested = True
        if ReactantResult == self.Product:
            self.Passed = True
        else:
            self.Passed = False
    def GetPassed(self):
        return self.Passed
    def GetReactant(self):
        return self.Reactant
    def GetProduct(self):
        return self.Product
    def GetTested(self):
        return self.Tested
    def SetReactant(self, Reactant):
        self.Reactant = Reactant
    def SetProduct(self, Product):
        self.Product = Product
    
class TestingGroup:
    """
    A collection of Tests, ran one by one.
    Allows for automatically printing the results.

    Use the `.Test()` method to run the Tests.

    Arguments:
        GroupName  - The name to use for the TestingGroup.
        Tests      - A list of Tests to put into the group.

        Print      - Whether to print the results to the console, defaults to True.
        Exit       - Whether to terminate your program after this group finishes being tested.
    """
    def __init__(self, GroupName:str, Tests:list[Test]|tuple[Test], *, Print:bool=True, Exit:bool=False):
        global TestStructure
        self.Tests = Tests
        self.GroupName = GroupName
        self.Passed = None
        self.Tested = False
        self.ShouldPrint = Print
        self.ShouldExit = Exit
        self.PassedTests = None
        self.FailedTests = None
        if GroupName.strip() == "": TestingGroupError("INVALID_NAME","An attempt was made to create a new TestingGroup with an invalid name.\nName: \""+GroupName+"\"")
        if TestStructure.get(GroupName,"") != "":
            TestingGroupError("NAME_CLASH","An attempt was made to create a new TestingGroup with a name that already exists.\nName: \""+GroupName+"\"")
        else:
            self.Safe = True
    
    def Test(self):
        global TestStructure
        if not self.Safe:
            TestingGroupError("INVALID_TestingGroup","An attempt was made to run a test on a TestingGroup that is invalid.")
        FormattedTests = []
        self.PassedTests = []
        self.FailedTests = []
        for Index,Test in enumerate(self.Tests,start=1):
            Test.Test()
            Passed = Test.GetPassed()
            if Passed:
                self.PassedTests.append(Test)
            else:
                self.Passed = False
                self.FailedTests.append(Test)
            FormattedTests.append(f"{colorama.Fore.GREEN if Passed else colorama.Fore.RED}Test {colorama.Style.BRIGHT}Nº{Index}{colorama.Style.NORMAL} {'Passed' if Passed else 'Failed'}{colorama.Style.RESET_ALL}")
        self.Tested = True
        TestStructure[(colorama.Fore.GREEN if self.Passed else colorama.Fore.RED)+self.GroupName+colorama.Style.RESET_ALL] = FormattedTests
        if self.ShouldPrint:
            PrintTestingGroupResults(TestStructure,0)
        if self.ShouldExit:
            exit()
    def GetPassed(self):
        return self.Passed
    def GetTested(self):
        return self.Tested
    def GetPassedTests(self):
        return self.PassedTests
    def GetFailedTests(self):
        return self.FailedTests
    def SetGroupName(self, GroupName):
        if GroupName.strip() == "": TestingGroupError("INVALID_NAME","An attempt was made to create a new TestingGroup with an invalid name.\nName: \""+GroupName+"\"")
        if TestStructure.get(GroupName,"") != "":
            TestingGroupError("NAME_CLASH","An attempt was made to create a new TestingGroup with a name that already exists.\nName: \""+GroupName+"\"")
        self.GroupName = GroupName
    def SetTests(self, Tests):
        self.Tests = Tests
    