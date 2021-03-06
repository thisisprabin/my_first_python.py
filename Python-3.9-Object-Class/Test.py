class MyFirst:
    emp = 0
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        MyFirst.emp += 1;

    def displayName(self):
        print("Person name ", self.name, " ", MyFirst.emp);
        return;

    def displayAge(self):
        print("Person age ", self.age);
        return;


name = "Prabin";
age = 22;

obj = MyFirst(name, age);
obj.displayName();
obj.displayAge();

print(getattr(obj, 'age'));
print(hasattr(obj, 'age'));
print(setattr(obj, 'age', 34));
obj.displayAge();

print("Docmentation ", MyFirst.__doc__);
print("Dictionary ", MyFirst.__dict__);
print("Name ", MyFirst.__name__);
print("Module ", MyFirst.__module__);
print("Base ", MyFirst.__base__);
print(id(obj));