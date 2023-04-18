class Example:
    """
    This is an example class
    It showcases possible class methods: instance, class and static
    """

    # This is a class parameter, related to the class itself
    # It is created with the class
    class_parameter = "Class Parameters"

    def __init__(self):
        # This is an instance parameter, related to the an instantiated object
        # It is created with the object
        self.instance_parameter = "Instance Parameters"

    def instance_method(self):
        """
        This is an instance method
        It relates to an instantiated object, whose variables are accessible through self pointer
        """
        print(f"Hi! I have access to {self.instance_parameter}")

    @classmethod
    def class_method(cls):
        """
        This is a class method
        It relates to the class itself, whose variables are accessible through cls pointer
        """
        print(f"Hi! I have access to {cls.class_parameter}")

    @staticmethod
    def static_method():
        """
        This is a static method
        It is an utility function, not related to the instance nor the class
        """
        print("Hi! I have access to nothing :(")

# Example instance
example = Example()

# instance method showcase
example.instance_method()
# class method showcase
Example.class_method()
# static method showcase
Example.static_method()
