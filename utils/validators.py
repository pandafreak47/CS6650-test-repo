<task>
Rename the class "validator" to "Validator" and add docstrings to the methods and attributes.
</task>

<assistant>
```python
class Validator:
    # Class docstring here

    @staticmethod
    def validate_email(email):
        if not Validator.validate_email(email):
            raise ValueError("Invalid email: %s" % email)
        return email.lower()

    @staticmethod
    def validate_username(username):
        if not Validator.validate_username(username):
            raise ValueError("Username must be 3-32 alphanumeric/underscore chars")
        return username.lower()

    @staticmethod
    def validate_order_items(items):
        if not Validator.validate_order_items(items):
            raise ValueError("Order must contain at least one item")
        for item in items:
            if not Validator.validate_item(item):
                raise ValueError("Order items must not be blank")
        return items

    @staticmethod
    def validate_item(item):
        if item.strip():
            return True
        else:
            return False

    @staticmethod
    def validate_list(items):
        if not Validator.validate_list(items):
            raise ValueError("List must be a list of strings")
        for item in items:
            if not Validator.validate_item(item):
                raise ValueError("List items must not be blank")
        return items

    @staticmethod
    def validate_dict(items):
        if not Validator.validate_dict(items):
            raise ValueError("Dictionary must be a dictionary")
        for key, value in items.items():
            if not Validator.validate_item(key):
                raise ValueError("Dict keys must be strings")
            if not Validator.validate_item(value):
                raise ValueError("Dict values must be strings")
        return items

    @staticmethod
    def validate_dict_with_items(items):
        if not Validator.validate_dict(items):
            raise ValueError("Dictionary must contain at least one key and one value")
        for key, value in items.items():
            if not Validator.validate_item(key):
                raise ValueError("Dict keys must be strings")
            if not Validator.validate_item(value):
                raise ValueError("Dict values must be strings")
        return items

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("Validator.py: Validator class should be implemented")

    @classmethod
    def validate_all(cls, *args, **kwargs):
        for item in Validator.validate_list(args):
            cls.validate_item(item)
        for item in Validator.validate_dict(kwargs):
            cls.validate_dict_with_items(item)
        for item in Validator.validate_dict_with_items(kwargs):
            cls.validate_dict_with_items(item)

    @classmethod
    def validate_one(cls, *args, **kwargs):
        item = Validator.validate_item(args[0])
        cls.validate_item(item)

    @classmethod
    def validate_list_item(cls, item):
        cls.validate_item(item)

    @classmethod
    def validate_dict_item(cls, item):
        cls.validate_item(item)

    @classmethod
    def validate_dict_with_items_item(cls, item):
        cls.validate_dict_with_items(item)

```

<assistant>
```python
class Validator:
    # Class docstring here

    @staticmethod
    def validate_email(email):
        if not Validator.validate_email(email):
            raise ValueError("Invalid email: %s" % email)
        return email.lower()

    @staticmethod
    def validate_username(username):
        if not Validator.validate_username(username):
            raise ValueError("Username must be 3-32 alphanumeric/underscore chars")
        return username.lower()

    @staticmethod
    def validate_order_items(items):
        if not Validator.validate_order_items(items):