#!/usr/bin/python3
"""
COMPLETE PYTHON OOP REFERENCE GUIDE
===================================
A comprehensive demonstration of all Object-Oriented Programming concepts
in Python through a feature-rich 'SuperObject' class.

This file serves as the ultimate reference for beginners and intermediate
programmers learning Python OOP.
"""

import math
from datetime import datetime
from typing import Any, Dict, List, Optional

# =================================================================
# MAIN CLASS DEFINITION
# =================================================================

class SuperObject:
    """
    The Ultimate SuperObject Class
    ==============================
    
    This class demonstrates EVERY important OOP concept in Python:
    - All types of attributes and methods
    - Properties with validation
    - All essential magic methods
    - Best practices and common pitfalls
    """
    
    # ===== 1. CLASS ATTRIBUTES =====
    # WHY: Shared data among ALL instances of the class
    # WHEN: Use for counters, shared constants, or configuration
    # HOW: Define outside __init__ without 'self.'
    # WHEN NOT: Don't use for instance-specific data
    # WRONG WAY: Don't modify class attributes through instances (use cls.)
    
    instance_count = 0  # Tracks how many objects were created
    MAX_NAME_LENGTH = 50  # Constant shared by all instances
    created_objects = []  # List of all created objects (be careful with memory!)

    def __init__(self, name: str, age: int, email: str = None, 
                 skills: List[str] = None, metadata: Dict[str, Any] = None):
        """
        CONSTRUCTOR METHOD
        ==================
        
        WHY: Initialize object state when creating new instances
        WHEN: Called automatically when you write SuperObject(...)
        HOW: Define attributes using self.attribute_name = value
        WHEN NOT: Don't put complex business logic here
        WRONG WAY: Don't access properties directly (use self._attribute)
                   This bypasses setter validation!
        """
        
        # 2. INSTANCE ATTRIBUTES - PUBLIC, PROTECTED, PRIVATE
        # WHY: Store object-specific data with different access levels
        # WHEN: Use based on intended access from outside the class
        # HOW: 
        #   - Public: self.attribute (accessible everywhere)
        #   - Protected: self._attribute (internal use, but accessible)
        #   - Private: self.__attribute (name mangling, harder to access)
        # WHEN NOT: Don't use private for everything (Python favors openness)
        # WRONG WAY: Accessing self.__private directly in __init__ bypasses validation
        
        # CORRECT: Use private attribute for internal storage
        self._name = None  # Internal storage
        self._age = None   # Internal storage  
        self._email = None # Internal storage
        
        # Use properties to set values (this triggers validation!)
        self.name = name    # This calls the setter with validation
        self.age = age      # This calls the setter with validation  
        self.email = email  # This calls the setter with validation
        
        # Public attributes (direct access)
        self.skills = skills if skills is not None else []
        self.metadata = metadata if metadata is not None else {}
        self.created_at = datetime.now()
        
        # Protected attribute (intended for internal use)
        self._id = id(self)  # Object's memory ID
        
        # Private attribute (name mangling applied)
        self.__secret_key = f"secret_{SuperObject.instance_count}"
        
        # Update class attributes
        SuperObject.instance_count += 1
        SuperObject.created_objects.append(self)

    # ===== 3. PROPERTIES (GETTERS AND SETTERS) =====
    # WHY: Control access to attributes, add validation, computed values
    # WHEN: When you need to validate data, transform values, or compute on-the-fly
    # HOW: Use @property for getter, @attribute.setter for setter
    # WHEN NOT: Don't use for simple attributes that need no validation
    # WRONG WAY: Don't access self.__private_attr directly in __init__
    
    @property
    def name(self) -> str:
        """
        NAME PROPERTY GETTER
        WHY: Provides controlled read access to the name
        WHEN: Every time someone accesses obj.name
        """
        return self._name
    
    @name.setter  
    def name(self, value: str) -> None:
        """
        NAME PROPERTY SETTER
        WHY: Validates name before storing it
        WHEN: Every time someone assigns obj.name = value
        HOW: Automatically called on assignment
        VALIDATION: Must be string, 1-50 chars, no special chars
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= SuperObject.MAX_NAME_LENGTH):
            raise ValueError(f"Name must be 1-{SuperObject.MAX_NAME_LENGTH} characters")
        if not value.replace(' ', '').replace('-', '').isalnum():
            raise ValueError("Name can only contain letters, spaces, and hyphens")
        self._name = value.strip().title()  # Clean and format
    
    @property
    def age(self) -> int:
        """AGE GETTER: Returns the person's age"""
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        """
        AGE SETTER WITH BUSINESS LOGIC VALIDATION
        WHY: Ensure age is realistic and valid
        WHEN: Setting age during creation or updates
        VALIDATION: Must be int, between 0-150
        """
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if not (0 <= value <= 150):
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    @property
    def email(self) -> Optional[str]:
        """EMAIL GETTER: Returns the email address"""
        return self._email
    
    @email.setter
    def email(self, value: Optional[str]) -> None:
        """
        EMAIL SETTER WITH FORMAT VALIDATION
        WHY: Ensure email format is valid if provided
        WHEN: Setting email during creation or updates
        VALIDATION: Must contain @ and . if not None
        """
        if value is None:
            self._email = None
            return
        if not isinstance(value, str):
            raise TypeError("Email must be a string or None")
        if '@' not in value or '.' not in value:
            raise ValueError("Email must contain @ and . symbols")
        if len(value) < 5:
            raise ValueError("Email is too short")
        self._email = value.lower().strip()
    
    @property  
    def secret_info(self) -> str:
        """
        READ-ONLY COMPUTED PROPERTY
        WHY: Provides access to private data in a controlled way
        WHEN: Need to expose private information safely
        HOW: Only getter, no setter (read-only)
        """
        return f"Secret: {self.__secret_key}"
    
    @property
    def full_description(self) -> str:
        """
        COMPUTED PROPERTY
        WHY: Generate dynamic content based on current state
        WHEN: Need a calculated value that depends on multiple attributes
        HOW: Combines multiple attributes into meaningful information
        """
        email_part = f" ({self.email})" if self.email else ""
        skills_part = f" | Skills: {', '.join(self.skills)}" if self.skills else ""
        return f"{self.name}, {self.age} years old{email_part}{skills_part}"

    # ===== 4. METHOD TYPES =====
    
    def instance_method(self) -> str:
        """
        INSTANCE METHOD
        ===============
        WHY: Operate on specific object's data
        WHEN: Need access to object's attributes (self)
        HOW: First parameter is always 'self'
        WHEN NOT: Don't use if method doesn't need object data
        """
        return f"Instance method called on {self.name} (ID: {self._id})"
    
    @classmethod
    def create_default(cls) -> 'SuperObject':
        """
        CLASS METHOD - ALTERNATIVE CONSTRUCTOR
        =====================================
        WHY: Provide different ways to create objects
        WHEN: Need factory methods or alternative constructors
        HOW: Use @classmethod decorator, first parameter is 'cls'
        WHEN NOT: Don't use if simple __init__ is sufficient
        """
        return cls("Default User", 25, "default@example.com")
    
    @classmethod
    def get_statistics(cls) -> Dict[str, Any]:
        """
        CLASS METHOD - CLASS INFORMATION
        ===============================
        WHY: Provide information about the class itself
        WHEN: Need data about all instances, not specific instance
        """
        return {
            'total_instances': cls.instance_count,
            'max_name_length': cls.MAX_NAME_LENGTH,
            'objects_in_memory': len(cls.created_objects)
        }
    
    @staticmethod
    def validate_email_format(email: str) -> bool:
        """
        STATIC METHOD - UTILITY FUNCTION
        ===============================
        WHY: Provide utility functions related to the class
        WHEN: Function is related to class but doesn't need class/instance data
        HOW: Use @staticmethod decorator, no self or cls parameter
        WHEN NOT: Don't use if function needs class or instance data
        """
        if not isinstance(email, str):
            return False
        return '@' in email and '.' in email and len(email) >= 5

    # ===== 5. MAGIC METHODS (DUNDER METHODS) =====
    # WHY: Define how objects behave with built-in Python operations
    # WHEN: Want objects to work naturally with Python syntax
    # HOW: Define methods with double underscores (__method__)
    # WHEN NOT: Don't implement unless you need the specific behavior
    
    def __str__(self) -> str:
        """
        STRING REPRESENTATION - USER FRIENDLY
        ====================================
        WHY: Define how object appears when printed
        WHEN: Called by print(), str(), f-strings
        HOW: Return a human-readable string
        SHOULD: Be concise and informative for end users
        """
        return f"{self.name} ({self.age} years)"
    
    def __repr__(self) -> str:
        """
        REPRESENTATION - DEVELOPER FRIENDLY  
        ==================================
        WHY: Define unambiguous object representation
        WHEN: Called by repr(), debugger, interactive shell
        HOW: Return string that could recreate the object
        SHOULD: Be unambiguous and useful for debugging
        """
        return (f"SuperObject(name='{self.name}', age={self.age}, "
                f"email='{self.email}', skills={self.skills})")
    
    def __len__(self) -> int:
        """
        LENGTH OPERATOR
        ==============
        WHY: Define what len(obj) returns
        WHEN: Object represents a collection or has a meaningful size
        HOW: Return an integer representing size/length
        """
        return len(self.skills) + len(self.metadata)
    
    def __getitem__(self, key: str) -> Any:
        """
        INDEX/KEY ACCESS - GET
        =====================
        WHY: Allow dictionary-style access obj['key']
        WHEN: Object contains key-value pairs or collections
        HOW: Return value for the given key
        WRONG WAY: Don't forget to handle KeyError appropriately
        """
        if key in self.metadata:
            return self.metadata[key]
        elif key == 'skills':
            return self.skills
        elif key == 'name':
            return self.name
        elif key == 'age':
            return self.age
        elif key == 'email':
            return self.email
        else:
            raise KeyError(f"Key '{key}' not found")
    
    def __setitem__(self, key: str, value: Any) -> None:
        """
        INDEX/KEY ACCESS - SET
        =====================
        WHY: Allow assignment like obj['key'] = value
        WHEN: Want to modify object using dictionary syntax
        HOW: Store the key-value pair appropriately
        """
        if key in ['name', 'age', 'email']:
            # Use property setters for validation
            setattr(self, key, value)
        else:
            # Store in metadata
            self.metadata[key] = value
    
    def __contains__(self, item: str) -> bool:
        """
        MEMBERSHIP TEST - 'in' OPERATOR
        ==============================
        WHY: Define behavior of 'item in obj'
        WHEN: Want to check if object contains something
        HOW: Return True if item is found, False otherwise
        """
        return (item in self.skills or 
                item in self.metadata or
                item == self.name or
                item == self.email)
    
    def __eq__(self, other: object) -> bool:
        """
        EQUALITY COMPARISON
        ==================
        WHY: Define when two objects are considered equal
        WHEN: Need to compare objects with == operator
        HOW: Compare relevant attributes
        IMPORTANT: Return NotImplemented for incompatible types
        """
        if not isinstance(other, SuperObject):
            return NotImplemented
        return (self.name == other.name and 
                self.age == other.age and 
                self.email == other.email)
    
    def __lt__(self, other: 'SuperObject') -> bool:
        """
        LESS THAN COMPARISON
        ===================
        WHY: Enable sorting and comparison operations
        WHEN: Objects have a natural ordering
        HOW: Compare based on meaningful criteria
        """
        if not isinstance(other, SuperObject):
            return NotImplemented
        return self.age < other.age
    
    def __add__(self, other: 'SuperObject') -> 'SuperObject':
        """
        ADDITION OPERATOR
        ================
        WHY: Define behavior of obj1 + obj2
        WHEN: Addition makes sense for your objects
        HOW: Return new object combining both objects
        WRONG WAY: Don't modify existing objects, return new one
        """
        if not isinstance(other, SuperObject):
            raise TypeError("Can only add another SuperObject")
        
        # Combine names
        new_name = f"{self.name} and {other.name}"
        # Use average age
        new_age = (self.age + other.age) // 2
        # Combine skills
        new_skills = list(set(self.skills + other.skills))  # Remove duplicates
        # Combine metadata
        new_metadata = {**self.metadata, **other.metadata}
        
        return SuperObject(new_name, new_age, None, new_skills, new_metadata)
    
    def __iadd__(self, other: 'SuperObject') -> 'SuperObject':
        """
        IN-PLACE ADDITION (+=)
        =====================
        WHY: Define behavior of obj += other
        WHEN: Want to modify object in place
        HOW: Modify self and return self
        DIFFERENCE: Modifies existing object vs __add__ creates new one
        """
        if not isinstance(other, SuperObject):
            raise TypeError("Can only add another SuperObject")
        
        # Modify this object
        self.skills.extend(other.skills)
        self.skills = list(set(self.skills))  # Remove duplicates
        self.metadata.update(other.metadata)
        
        return self  # Must return self for in-place operations
    
    def __call__(self, action: str = "greet") -> str:
        """
        CALLABLE OBJECT
        ==============
        WHY: Make object callable like a function obj()
        WHEN: Object represents an action or function
        HOW: Define what happens when obj() is called
        """
        if action == "greet":
            return f"Hello! I'm {self.name}, nice to meet you!"
        elif action == "introduce":
            return self.full_description
        else:
            return f"I don't know how to '{action}'"
    
    def __bool__(self) -> bool:
        """
        BOOLEAN CONVERSION
        =================
        WHY: Define truthiness of object
        WHEN: Object used in if statements or bool()
        HOW: Return True for "valid" objects, False for "empty" ones
        """
        return self.name is not None and len(self.name) > 0
    
    def __hash__(self) -> int:
        """
        HASH VALUE - FOR SETS AND DICT KEYS
        ==================================
        WHY: Allow objects to be used in sets and as dictionary keys
        WHEN: Objects need to be hashable
        HOW: Return hash based on immutable attributes
        IMPORTANT: Objects that compare equal must have same hash
        WARNING: Only implement if object is immutable or hash is stable
        """
        return hash((self.name, self.age, self.email))
    
    def __del__(self) -> None:
        """
        DESTRUCTOR - CLEANUP
        ===================
        WHY: Clean up resources when object is destroyed
        WHEN: Object holds external resources (files, connections)
        HOW: Define cleanup actions
        WARNING: Don't rely on this for critical cleanup (use context managers)
        """
        print(f"SuperObject {self.name} is being destroyed")


# ===== 6. INHERITANCE =====
# WHY: Create specialized versions of existing classes
# WHEN: New class is a "type of" existing class
# HOW: class Child(Parent):
# WHEN NOT: Don't use for "has a" relationships (use composition)

class EmployeeObject(SuperObject):
    """
    INHERITANCE EXAMPLE - SPECIALIZED SUPEROBJECT  
    ============================================
    
    WHY: Employee IS A SuperObject with additional features
    WHEN: Need all SuperObject features plus employee-specific ones
    HOW: Inherit from SuperObject and extend functionality
    """
    
    # Class attribute specific to employees
    company_name = "Tech Corp"
    
    def __init__(self, name: str, age: int, email: str, employee_id: str, 
                 salary: float, department: str, skills: List[str] = None):
        """
        EXTENDED CONSTRUCTOR
        WHY: Initialize parent class plus new attributes
        HOW: Call super().__init__() then add new attributes
        """
        # Initialize parent class
        super().__init__(name, age, email, skills)
        
        # Add employee-specific attributes
        self._employee_id = None
        self._salary = None
        self._department = None
        
        # Use properties for validation
        self.employee_id = employee_id
        self.salary = salary  
        self.department = department
    
    @property
    def employee_id(self) -> str:
        return self._employee_id
    
    @employee_id.setter
    def employee_id(self, value: str) -> None:
        """Employee ID validation"""
        if not isinstance(value, str):
            raise TypeError("Employee ID must be a string")
        if not value.startswith("EMP") or len(value) != 7:
            raise ValueError("Employee ID must start with 'EMP' and be 7 characters")
        self._employee_id = value
    
    @property
    def salary(self) -> float:
        return self._salary
    
    @salary.setter
    def salary(self, value: float) -> None:
        """Salary validation"""
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = float(value)
    
    @property
    def department(self) -> str:
        return self._department
    
    @department.setter  
    def department(self, value: str) -> None:
        """Department validation"""
        valid_departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]
        if value not in valid_departments:
            raise ValueError(f"Department must be one of: {valid_departments}")
        self._department = value
    
    # ===== 7. POLYMORPHISM =====
    # WHY: Same interface, different behavior in subclasses
    # WHEN: Subclass needs different behavior for same method
    # HOW: Override parent methods in child class
    
    def instance_method(self) -> str:
        """
        METHOD OVERRIDE - POLYMORPHISM
        =============================
        WHY: Employee objects need different behavior
        HOW: Override parent method but can still call it with super()
        """
        parent_info = super().instance_method()
        return f"{parent_info} | Employee ID: {self.employee_id}"
    
    def __str__(self) -> str:
        """Override string representation for employees"""
        return f"{self.name} - {self.department} ({self.employee_id})"
    
    # Employee-specific methods
    def get_annual_bonus(self) -> float:
        """Calculate annual bonus based on salary"""
        return self.salary * 0.1
    
    def promote(self, new_salary: float) -> None:
        """Promote employee with salary increase"""
        if new_salary <= self.salary:
            raise ValueError("Promotion salary must be higher than current salary")
        old_salary = self.salary
        self.salary = new_salary
        print(f"{self.name} promoted! Salary increased from ${old_salary:,.2f} to ${new_salary:,.2f}")


# =================================================================
# COMPREHENSIVE PRACTICAL APPLICATION
# =================================================================

def demonstrate_all_concepts():
    """
    COMPLETE DEMONSTRATION OF ALL OOP CONCEPTS
    ==========================================
    This function demonstrates every single concept implemented above
    in a practical, real-world scenario.
    """
    
    print("=" * 60)
    print("COMPREHENSIVE PYTHON OOP DEMONSTRATION")
    print("=" * 60)
    
    # ===== 1. BASIC OBJECT CREATION AND ATTRIBUTES =====
    print("\n1. OBJECT CREATION AND ATTRIBUTE ACCESS")
    print("-" * 40)
    
    try:
        # Creating objects with validation
        person1 = SuperObject("Alice Johnson", 28, "alice@email.com", 
                            ["Python", "JavaScript"], {"location": "New York"})
        print(f"✓ Created: {person1}")
        print(f"  Public data: {person1.name}")
        print(f"  Protected data: {person1._id}")
        print(f"  Private data (via property): {person1.secret_info}")
        
        # Demonstrating validation errors
        print("\n  Testing validation:")
        try:
            invalid_person = SuperObject("", 200, "invalid-email")  # Should fail
        except (ValueError, TypeError) as e:
            print(f"  ✓ Validation caught error: {e}")
            
    except Exception as e:
        print(f"✗ Error in object creation: {e}")
    
    # ===== 2. PROPERTIES AND VALIDATION =====
    print("\n2. PROPERTIES AND VALIDATION")
    print("-" * 40)
    
    print(f"  Original name: {person1.name}")
    
    # Valid property change
    person1.name = "Alice Marie Johnson"
    print(f"  ✓ Name changed to: {person1.name}")
    
    # Invalid property change
    try:
        person1.name = "A1ice"  # Contains number
    except ValueError as e:
        print(f"  ✓ Validation prevented invalid name: {e}")
    
    # Demonstrating computed property
    print(f"  Full description: {person1.full_description}")
    
    # ===== 3. METHOD TYPES =====
    print("\n3. METHOD TYPES")
    print("-" * 40)
    
    # Instance method
    print(f"  Instance method: {person1.instance_method()}")
    
    # Class method
    stats = SuperObject.get_statistics()
    print(f"  Class method stats: {stats}")
    
    # Static method
    is_valid = SuperObject.validate_email_format("test@example.com")
    print(f"  Static method validation: {is_valid}")
    
    # Alternative constructor (class method)
    default_person = SuperObject.create_default()
    print(f"  Created via class method: {default_person}")
    
    # ===== 4. MAGIC METHODS =====
    print("\n4. MAGIC METHODS DEMONSTRATION")
    print("-" * 40)
    
    person2 = SuperObject("Bob Smith", 32, "bob@email.com", 
                         ["Java", "C++"], {"location": "California"})
    
    # String representations
    print(f"  __str__: {person1}")
    print(f"  __repr__: {repr(person1)}")
    
    # Length and container operations
    print(f"  __len__: len(person1) = {len(person1)}")
    print(f"  __getitem__: person1['name'] = {person1['name']}")
    print(f"  __contains__: 'Python' in person1 = {'Python' in person1}")
    
    # Set item
    person1['project'] = "AI Development"
    print(f"  __setitem__: Added project = {person1['project']}")
    
    # Comparison operations
    print(f"  __eq__: person1 == person2 = {person1 == person2}")
    print(f"  __lt__: person1 < person2 = {person1 < person2}")
    
    # Arithmetic operations
    combined = person1 + person2
    print(f"  __add__: Combined person = {combined}")
    print(f"  Combined skills: {combined.skills}")
    
    # In-place addition
    person1_copy = SuperObject("Alice Johnson", 28, "alice@email.com", 
                              ["Python"], {"location": "New York"})
    person1_copy += person2
    print(f"  __iadd__: After += operation, skills = {person1_copy.skills}")
    
    # Callable object
    greeting = person1("greet")
    print(f"  __call__: {greeting}")
    
    # Boolean conversion
    try:
        empty_person = SuperObject("", 0, None)  # This will fail validation
        print(f"  __bool__: bool(empty_person) = {bool(empty_person)}")
    except ValueError as e:
        print(f"  ✓ Boolean test: Correctly failed to create an empty object. Error: {e}")

    # Let's create properly for boolean test
    print(f"  __bool__: bool(person1) = {bool(person1)}")
    
    # ===== 5. INHERITANCE AND POLYMORPHISM =====
    print("\n5. INHERITANCE AND POLYMORPHISM")
    print("-" * 40)
    
    # Create employee (inherited from SuperObject)
    employee = EmployeeObject("Carol Davis", 30, "carol@company.com", 
                             "EMP1001", 75000.0, "Engineering", ["Python", "AI"])
    
    print(f"  Employee created: {employee}")
    print(f"  Employee method (polymorphism): {employee.instance_method()}")
    print(f"  Annual bonus: ${employee.get_annual_bonus():,.2f}")
    
    # Demonstrate inheritance - employee has all SuperObject methods
    print(f"  Inherited property: {employee.full_description}")
    print(f"  Inherited magic method: len(employee) = {len(employee)}")
    
    # Employee-specific functionality
    employee.promote(80000.0)
    
    # ===== 6. CLASS ATTRIBUTES AND METHODS =====
    print("\n6. CLASS ATTRIBUTES AND METHODS")
    print("-" * 40)
    
    print(f"  Total SuperObjects created: {SuperObject.instance_count}")
    print(f"  Max name length allowed: {SuperObject.MAX_NAME_LENGTH}")
    print(f"  Employee company: {EmployeeObject.company_name}")
    
    # Create more objects to see counter
    temp_objects = [SuperObject(f"Person{i}", 20+i, f"person{i}@test.com") 
                   for i in range(3)]
    print(f"  After creating 3 more: {SuperObject.instance_count}")
    
    # ===== 7. ERROR HANDLING AND EDGE CASES =====
    print("\n7. ERROR HANDLING DEMONSTRATION")
    print("-" * 40)
    
    error_cases = [
        ("Invalid age", lambda: SuperObject("Test", -5, "test@test.com")),
        ("Invalid email", lambda: SuperObject("Test", 25, "invalid")),  
        ("Invalid name", lambda: SuperObject("Test123", 25, "test@test.com")),
        ("Wrong type addition", lambda: person1 + "string"),
    ]
    
    for description, test_func in error_cases:
        try:
            test_func()
            print(f"  ✗ {description}: Should have failed!")
        except Exception as e:
            print(f"  ✓ {description}: {type(e).__name__}")
    
    # ===== 8. ADVANCED USAGE PATTERNS =====
    print("\n8. ADVANCED USAGE PATTERNS")
    print("-" * 40)
    
    # Using objects in collections
    people = [person1, person2, employee]
    people.sort()  # Uses __lt__ for sorting
    print(f"  Sorted by age: {[str(p) for p in people]}")
    
    # Using objects as dictionary keys (requires __hash__)
    person_roles = {person1: "Developer", person2: "Designer", employee: "Engineer"}
    print(f"  As dict keys: {person_roles[employee]}")
    
    # Using objects in sets (requires __hash__ and __eq__)
    unique_people = {person1, person2, employee, person1}  # person1 appears twice
    print(f"  In set (unique): {len(unique_people)} people")
    
    # ===== 9. MEMORY AND LIFECYCLE =====
    print("\n9. OBJECT LIFECYCLE")
    print("-" * 40)
    
    # Show object creation tracking
    print(f"  Objects in memory: {len(SuperObject.created_objects)}")
    
    # Create and destroy object to show __del__
    temp_obj = SuperObject("Temporary", 25, "temp@test.com")
    temp_name = temp_obj.name
    del temp_obj  # This should trigger __del__ method
    
    print(f"  Final object count: {SuperObject.instance_count}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("All OOP concepts successfully demonstrated!")
    print("=" * 60)


# =================================================================
# BEST PRACTICES AND COMMON MISTAKES SUMMARY
# =================================================================

"""
KEY TAKEAWAYS AND BEST PRACTICES:
=================================

1. PROPERTIES:
   ✓ DO: Use properties for validation and computed values
   ✓ DO: Store data in private/protected attributes
   ✗ DON'T: Access private attributes directly in __init__
   ✗ DON'T: Make every attribute a property unnecessarily

2. CLASS vs INSTANCE ATTRIBUTES:
   ✓ DO: Use class attributes for shared data and constants
   ✓ DO: Modify class attributes using ClassName.attribute
   ✗ DON'T: Modify class attributes through instances
   ✗ DON'T: Use class attributes for instance-specific data

3. METHOD TYPES:
   ✓ DO: Use instance methods when you need object data
   ✓ DO: Use class methods for alternative constructors
   ✓ DO: Use static methods for utility functions
   ✗ DON'T: Use static methods if you need class/instance data

4. MAGIC METHODS:
   ✓ DO: Implement __str__ for user-friendly representation
   ✓ DO: Implement __repr__ for debugging
   ✓ DO: Implement __eq__ and __hash__ together for collections
   ✗ DON'T: Implement __del__ for critical cleanup

5. INHERITANCE:
   ✓ DO: Use inheritance for "is-a" relationships
   ✓ DO: Call super().__init__() in child constructors
   ✓ DO: Override methods for polymorphism when needed
   ✗ DON'T: Use inheritance for "has-a" relationships (use composition)
   ✗ DON'T: Create deep inheritance hierarchies

6. VALIDATION:
   ✓ DO: Validate data in property setters
   ✓ DO: Use type hints for better code documentation
   ✓ DO: Provide meaningful error messages
   ✗ DON'T: Skip validation to save time
   ✗ DON'T: Use generic exceptions (use specific ones)

COMMON MISTAKES TO AVOID:
========================

1. BYPASSING VALIDATION:
   WRONG: self.__private_data = value  # In __init__
   RIGHT: self.property_name = value   # Uses setter validation

2. MODIFYING CLASS ATTRIBUTES INCORRECTLY:
   WRONG: instance.class_attribute = new_value  # Creates instance attribute!
   RIGHT: ClassName.class_attribute = new_value  # Modifies class attribute

3. NOT HANDLING TYPE CHECKING IN MAGIC METHODS:
   WRONG: def __eq__(self, other): return self.name == other.name
   RIGHT: def __eq__(self, other): 
           if not isinstance(other, MyClass): return NotImplemented
           return self.name == other.name

4. FORGETTING TO RETURN self IN IN-PLACE OPERATIONS:
   WRONG: def __iadd__(self, other): self.data += other.data
   RIGHT: def __iadd__(self, other): self.data += other.data; return self

5. USING MUTABLE DEFAULT ARGUMENTS:
   WRONG: def __init__(self, items=[]):
   RIGHT: def __init__(self, items=None): items = items or []
"""


# =================================================================
# RUNNING THE DEMONSTRATION
# =================================================================

if __name__ == "__main__":
    """
    EXECUTION ENTRY POINT
    ====================
    WHY: Allows script to be imported without running demonstration
    WHEN: Always use this pattern for executable scripts
    HOW: Code only runs when script is executed directly
    """
    try:
        demonstrate_all_concepts()
    except Exception as e:
        print(f"Demonstration failed with error: {e}")
        import traceback
        traceback.print_exc()


# =================================================================
# ADDITIONAL ADVANCED EXAMPLES
# =================================================================

class DatabaseConnection:
    """
    CONTEXT MANAGER EXAMPLE
    ======================
    Demonstrates proper resource management using context managers.
    This is the RIGHT way to handle cleanup, not relying on __del__.
    """
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None
        self.is_connected = False
    
    def __enter__(self):
        """Called when entering 'with' statement"""
        print(f"Connecting to database: {self.connection_string}")
        self.connection = f"Connection to {self.connection_string}"
        self.is_connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' statement"""
        if self.is_connected:
            print(f"Closing database connection: {self.connection_string}")
            self.connection = None
            self.is_connected = False
        return False  # Don't suppress exceptions
    
    def execute_query(self, query: str) -> str:
        if not self.is_connected:
            raise RuntimeError("Database not connected")
        return f"Executed: {query}"


class ObserverPattern:
    """
    DESIGN PATTERN EXAMPLE - OBSERVER
    ================================
    Demonstrates how OOP concepts enable design patterns.
    """
    
    def __init__(self, name: str):
        self.name = name
        self._observers = []
        self._value = None
    
    def attach(self, observer):
        """Add an observer"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        """Remove an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers of changes"""
        for observer in self._observers:
            observer.update(self, self._value)
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        print(f"{self.name}: Value changed from {old_value} to {new_value}")
        self.notify()


class Observer:
    """Observer that watches for changes"""
    
    def __init__(self, name: str):
        self.name = name
    
    def update(self, subject, value):
        print(f"  Observer {self.name} notified: {subject.name} = {value}")


def demonstrate_advanced_patterns():
    """Additional demonstration of advanced OOP patterns"""
    
    print("\n" + "=" * 60)
    print("ADVANCED OOP PATTERNS")
    print("=" * 60)
    
    # Context Manager Example
    print("\n1. CONTEXT MANAGER (Resource Management)")
    print("-" * 50)
    
    with DatabaseConnection("postgresql://localhost:5432/mydb") as db:
        result = db.execute_query("SELECT * FROM users")
        print(f"Query result: {result}")
    # Connection automatically closed here
    
    # Observer Pattern Example
    print("\n2. OBSERVER PATTERN")
    print("-" * 50)
    
    subject = ObserverPattern("Temperature Sensor")
    observer1 = Observer("Display")
    observer2 = Observer("Logger")
    observer3 = Observer("Alarm")
    
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    
    subject.value = 25.5  # All observers get notified
    subject.value = 30.0  # All observers get notified again
    
    subject.detach(observer2)
    subject.value = 35.0  # Only observer1 and observer3 get notified
    
    print("\nAdvanced patterns demonstration complete!")


# =================================================================
# COMPREHENSIVE TESTING FUNCTIONS
# =================================================================

def run_comprehensive_tests():
    """
    COMPREHENSIVE TEST SUITE
    =======================
    Tests every aspect of the SuperObject to ensure correctness.
    """
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    
    test_results = []
    
    # Test 1: Basic Object Creation
    try:
        obj = SuperObject("Test User", 25, "test@example.com")
        assert obj.name == "Test User"
        assert obj.age == 25
        assert obj.email == "test@example.com"
        test_results.append("✓ Basic object creation")
    except Exception as e:
        test_results.append(f"✗ Basic object creation: {e}")
    
    # Test 2: Property Validation
    try:
        obj = SuperObject("Valid Name", 30, "valid@email.com")
        
        # Test invalid name
        try:
            obj.name = "123Invalid"
            test_results.append("✗ Name validation: Should have failed")
        except ValueError:
            test_results.append("✓ Name validation")
        
        # Test invalid age
        try:
            obj.age = -5
            test_results.append("✗ Age validation: Should have failed")
        except ValueError:
            test_results.append("✓ Age validation")
            
        # Test invalid email
        try:
            obj.email = "invalid-email"
            test_results.append("✗ Email validation: Should have failed")
        except ValueError:
            test_results.append("✓ Email validation")
            
    except Exception as e:
        test_results.append(f"✗ Property validation: {e}")
    
    # Test 3: Magic Methods
    try:
        obj1 = SuperObject("Alice", 25, "alice@test.com", ["Python"])
        obj2 = SuperObject("Bob", 30, "bob@test.com", ["Java"])
        
        # Test string representations
        assert str(obj1) == "Alice (25 years)"
        assert "SuperObject" in repr(obj1)
        
        # Test equality
        obj3 = SuperObject("Alice", 25, "alice@test.com")
        assert obj1 == obj3
        assert obj1 != obj2
        
        # Test addition
        combined = obj1 + obj2
        assert "Alice & Bob" in combined.name
        assert len(combined.skills) == 2
        
        # Test container methods
        assert len(obj1) == 1  # One skill
        obj1['location'] = 'NYC'
        assert obj1['location'] == 'NYC'
        assert 'Python' in obj1
        
        test_results.append("✓ Magic methods")
        
    except Exception as e:
        test_results.append(f"✗ Magic methods: {e}")
    
    # Test 4: Inheritance
    try:
        emp = EmployeeObject("John Doe", 28, "john@company.com", 
                            "EMP1001", 50000, "Engineering")
        
        # Test inheritance of parent methods
        assert "John Doe" in emp.instance_method()
        assert emp.name == "John Doe"
        
        # Test employee-specific methods
        bonus = emp.get_annual_bonus()
        assert bonus == 5000.0
        
        # Test polymorphism
        parent_method = SuperObject("Test", 25, "test@test.com").instance_method()
        child_method = emp.instance_method()
        assert len(child_method) > len(parent_method)  # Child method adds more info
        
        test_results.append("✓ Inheritance and polymorphism")
        
    except Exception as e:
        test_results.append(f"✗ Inheritance and polymorphism: {e}")
    
    # Test 5: Class Methods and Attributes
    try:
        initial_count = SuperObject.instance_count
        obj1 = SuperObject("Test1", 25, "test1@test.com")
        obj2 = SuperObject("Test2", 30, "test2@test.com")
        
        assert SuperObject.instance_count == initial_count + 2
        
        stats = SuperObject.get_statistics()
        assert stats['total_instances'] == initial_count + 2
        
        default_obj = SuperObject.create_default()
        assert default_obj.name == "Default User"
        
        test_results.append("✓ Class methods and attributes")
        
    except Exception as e:
        test_results.append(f"✗ Class methods and attributes: {e}")
    
    # Print test results
    print("\nTEST RESULTS:")
    print("-" * 30)
    for result in test_results:
        print(f"  {result}")
    
    passed = len([r for r in test_results if r.startswith("✓")])
    total = len(test_results)
    print(f"\nTESTS PASSED: {passed}/{total}")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! 🎉")
    else:
        print("❌ Some tests failed. Check the implementation.")


# =================================================================
# INTERACTIVE LEARNING EXERCISES
# =================================================================

def interactive_exercises():
    """
    INTERACTIVE LEARNING EXERCISES
    =============================
    Provides hands-on exercises for learners to practice OOP concepts.
    """
    
    print("\n" + "=" * 60)
    print("INTERACTIVE OOP LEARNING EXERCISES")
    print("=" * 60)
    
    exercises = [
        {
            "title": "Exercise 1: Create a Student Class",
            "description": """
Create a Student class that inherits from SuperObject with:
- student_id property (must start with 'STU' and be 8 chars)
- gpa property (must be between 0.0 and 4.0)
- courses list (public attribute)
- add_course(course_name) method
- get_honor_status() method (GPA >= 3.5 returns 'Honor Student')
- Override __str__ to show student info
            """,
            "solution": """
class Student(SuperObject):
    def __init__(self, name, age, email, student_id, gpa):
        super().__init__(name, age, email)
        self.courses = []
        self.student_id = student_id
        self.gpa = gpa
    
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, str):
            raise TypeError("Student ID must be string")
        if not value.startswith('STU') or len(value) != 8:
            raise ValueError("Student ID must start with 'STU' and be 8 chars")
        self._student_id = value
    
    @property
    def gpa(self):
        return self._gpa
    
    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("GPA must be a number")
        if not 0.0 <= value <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        self._gpa = float(value)
    
    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
    
    def get_honor_status(self):
        return "Honor Student" if self.gpa >= 3.5 else "Regular Student"
    
    def __str__(self):
        return f"{self.name} ({self.student_id}) - GPA: {self.gpa}"
            """
        },
        
        {
            "title": "Exercise 2: Create a BankAccount Class",
            "description": """
Create a BankAccount class with:
- account_number property (read-only after creation)
- balance property (cannot be negative)
- transaction_history list (private)
- deposit(amount) method
- withdraw(amount) method (check sufficient funds)
- get_balance() method
- Magic methods: __str__, __add__ (merge accounts), __len__ (transaction count)
            """,
            "solution": """
class BankAccount:
    account_counter = 1000
    
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self._account_number = f"ACC{BankAccount.account_counter}"
        BankAccount.account_counter += 1
        self._balance = 0
        self.__transaction_history = []
        if initial_balance > 0:
            self.deposit(initial_balance)
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self.__transaction_history.append(f"Deposit: +${amount}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.__transaction_history.append(f"Withdrawal: -${amount}")
    
    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"Account {self.account_number}: ${self.balance:.2f}"
    
    def __len__(self):
        return len(self.__transaction_history)
    
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError("Can only merge with another BankAccount")
        new_account = BankAccount(f"{self.owner_name} & {other.owner_name}")
        new_account._balance = self.balance + other.balance
        return new_account
            """
        }
    ]
    
    for i, exercise in enumerate(exercises, 1):
        print(f"\n{exercise['title']}")
        print("=" * len(exercise['title']))
        print(exercise['description'])
        
        user_input = input(f"\nPress Enter to see solution for Exercise {i}...")
        if user_input.lower() not in ['skip', 's']:
            print(f"\nSOLUTION:")
            print("-" * 20)
            print(exercise['solution'])
    
    print(f"\n🎓 Congratulations! You've completed all exercises!")
    print("Practice implementing these solutions to master Python OOP!")


# =================================================================
# MAIN EXECUTION WITH ALL DEMONSTRATIONS
# =================================================================

if __name__ == "__main__":
    """
    COMPLETE EXECUTION SEQUENCE
    ==========================
    Runs all demonstrations, tests, and exercises in sequence.
    """
    
    # Main demonstration
    demonstrate_all_concepts()
    
    # Advanced patterns
    demonstrate_advanced_patterns()
    
    # Comprehensive tests
    run_comprehensive_tests()
    
    # Interactive exercises
    user_choice = input("\nWould you like to see interactive exercises? (y/n): ")
    if user_choice.lower() in ['y', 'yes']:
        interactive_exercises()
    
    print(f"\n🚀 COMPLETE PYTHON OOP MASTERY GUIDE FINISHED! 🚀")
    print("You now have a comprehensive understanding of:")
    print("✓ Classes and Objects")
    print("✓ Attributes (Public, Protected, Private)")
    print("✓ Properties with Validation") 
    print("✓ All Method Types")
    print("✓ All Important Magic Methods")
    print("✓ Inheritance and Polymorphism")
    print("✓ Design Patterns")
    print("✓ Best Practices and Common Mistakes")
    print("✓ Advanced Usage Patterns")
    print("✓ Testing and Validation")
    print("\nKeep practicing and building amazing Python applications! 🐍")
