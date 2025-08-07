#!/usr/bin/python3
"""
A single file demonstrating a comprehensive 'SuperObject' class,
its subclass, and a practical application of all its features.
"""

# =================================================================
# CLASS DEFINITIONS
# =================================================================

class SuperObject:
    """
    This is the "SuperObject."
    It combines all the fundamental and advanced concepts of OOP.
    """
    
    # 1. Class Attribute: Shared among all instances (without self. and outside __init__)
    instance_count = 0

    def __init__(self, public_data, protected_data, private_data, components=None):
        """
        Constructor: Initializes attributes when a new object is created.
        """
        # 2. Attributes (Public, Protected, Private)
        self.public_data = public_data
        self._protected_data = protected_data
        self.__private_data = private_data
        self.components = components if components is not None else {}
        
        SuperObject.instance_count += 1

    # 3. Properties: Pythonic Getter and Setter
    @property
    def secret_info(self):
        """The Getter: Called when reading the property's value."""
        return self.__private_data

    @secret_info.setter
    def secret_info(self, value):
        """The Setter: Called when assigning a value to the property."""
        if isinstance(value, str) and len(value) > 3:
            self.__private_data = value
        else:
            raise ValueError("Value must be a string longer than 3 characters.")

    # 4. Method Types (Instance, Class, Static)
    def instance_method(self):
        """Instance Method: Works on the object's own data via self."""
        return f"My public data is: '{self.public_data}'"

    @classmethod
    def get_instance_count(cls):
        """Class Method: Works on the class itself via cls."""
        return f"{cls.instance_count} instances of this class have been created."

    @staticmethod
    def is_valid_data(data):
        """Static Method: A helper function that doesn't depend on the class or object."""
        return data is not None and data != ""

    # 5. Important Magic Methods
    def __str__(self):
        """Called by print(obj) for a user-friendly representation."""
        return f"[SuperObject: {self.public_data}]"

    def __repr__(self):
        """Called for a developer-focused, unambiguous representation."""
        return f"SuperObject('{self.public_data}')"
        
    def __len__(self):
        """Called by len(obj) to return the 'length' of the object."""
        return len(self.components)
        
    def __getitem__(self, key):
        """Allows dictionary-style access, like obj['key']."""
        return self.components[key]
        
    def __eq__(self, other):
        """Defines the behavior of the equality operator (==)."""
        if not isinstance(other, SuperObject):
            return NotImplemented
        return self.public_data == other.public_data

    def __add__(self, other):
        """Defines the behavior of the addition operator (+)."""
        if not isinstance(other, SuperObject):
            raise TypeError("Can only add another SuperObject.")
        new_public = f"{self.public_data} & {other.public_data}"
        new_components = {**self.components, **other.components}
        return SuperObject(new_public, "combined", "secret", new_components)

# 6. Inheritance
class SubObject(SuperObject):
    """A child class that inherits everything from the SuperObject."""
    def __init__(self, public_data, protected_data, private_data, components, new_feature):
        super().__init__(public_data, protected_data, private_data, components)
        self.new_feature = new_feature

    # 7. Polymorphism
    def instance_method(self):
        """Overrides the parent class's method."""
        parent_msg = super().instance_method()
        return f"{parent_msg} | And my new feature is: '{self.new_feature}'"


# =================================================================
# APPLICATION AND DEMONSTRATION
# =================================================================

if __name__ == "__main__":
    print("--- 1. Instance Creation and Attribute Access ---")
    obj1 = SuperObject("Data A", "protected A", "secret A", {'part1': 10, 'part2': 20})
    print(f"Public: {obj1.public_data}")
    print(f"Protected: {obj1._protected_data}")
    print(f"Private (mangled): {obj1._SuperObject__private_data}")
    
    print("\n--- 2. Properties (Getter and Setter) ---")
    print(f"Reading secret info (calls getter): {obj1.secret_info}")
    print("Setting secret info to 'New Secret' (calls setter)...")
    obj1.secret_info = "New Secret"
    print(f"New secret info: {obj1.secret_info}")
    print("Trying to set an invalid value...")
    try:
        obj1.secret_info = "No"
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n--- 3. Method Types ---")
    print(f"Instance method call: {obj1.instance_method()}")
    print(f"Class method call: {SuperObject.get_instance_count()}")
    print(f"Static method call: Is 'Data A' valid? {SuperObject.is_valid_data('Data A')}")

    print("\n--- 4. Inheritance and Polymorphism ---")
    sub_obj = SubObject("Data B", "protected B", "secret B", {'part3': 30}, "Awesome Feature")
    print(f"Sub-object's secret info (inherited): {sub_obj.secret_info}")
    print(f"Sub-object's overridden method: {sub_obj.instance_method()}")
    print(f"Class method after 2nd instance: {SuperObject.get_instance_count()}")
    
    print("\n--- 5. Magic Methods in Action ---")
    print(f"__str__ call: {obj1}")
    print(f"__len__ call: Number of components in obj1 is {len(obj1)}")
    print(f"__getitem__ call: Value of 'part1' is {obj1['part1']}")
    obj2 = SuperObject("Data A", "p", "s")
    print(f"__eq__ call: Is obj1 == obj2? {obj1 == obj2}")
    combined_obj = obj1 + sub_obj
    print(f"__add__ call: {combined_obj}")
    print(f"Components of combined object: {combined_obj.components}")
    