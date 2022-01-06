# Pyrmanent

A base class to make your Python classes permanent in a flash.

[![PyPI](https://img.shields.io/pypi/v/pyrmanent?color=%231182C2&label=PyPI)](https://pypi.org/project/pyrmanent/)
[![Python](https://img.shields.io/badge/Python->3.0-%23FFD140)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-%23e83633)](https://github.com/sergioteula/pyrmanent/blob/master/LICENSE)
[![Support](https://img.shields.io/badge/Support-Good-brightgreen)](https://github.com/sergioteula/pyrmanent/issues)


## Features

- Easy to use.
- Great compatibility.
- No database needed.
- Ask for new features through the [issues](https://github.com/sergioteula/pyrmanent) section.
- Join our [Telegram group](https://t.me/pyrmanent) for support or development.

## Installation

You can install or upgrade the module with:

    pip install pyrmanent --upgrade

## Usage guide

### Basic usage:

Making your custom clases permanent is as easy as adding Pyrmanent as the base class.

```python
from pyrmanent import Pyrmanent

class MyClass(Pyrmanent):
    pass
```

Call the `save` method to save the current instance data:

```python
my_class_instance = MyClass()
my_class_instance.my_data = "Hello world!"
my_class_instance.save()
```

To load a previously saved instance data, just create the instance and data will be
automatically loaded:

```python
my_class_instance = MyClass()
print(my_class_instance.my_data)

"Hello world!"
```

### Configuration

#### Instance name

The `name` parameter allows saving different instances of the same class. Each one will
keep its own data.

```python
first_instance = MyClass(name="first")
first_instance.my_data = "This is the first instance"
first_instance.save()

second_instance = MyClass(name="second")
second_instance.my_data = "And this the second one"
second_instance.save()
```

#### Saving path

The path for the saved files can be customized with the `folder` parameter. If not provided,
the files will be saved on the execution folder.

```python
my_class_instance = MyClass(folder="data")
```

#### Auto saving

The `autosave` parameter allows using the `autosave` method to save data only when `True`.
This is specially useful for your custom class methods.

```python
class MyClass(Pyrmanent):
    def set_title(self, title):
        self.title = title
        self.autosave()

# The instance data will be saved when the method is called
my_class_instance = MyClass(autosave=True)
my_class_instance.set_title("Test")

# You should manually save the instance data
my_class_instance = MyClass(autosave=False)
my_class_instance.set_title("Test")
my_class_instance.save()
```

### Override the \_\_init\_\_ method

The `__init__` method can be overrided to add attributes and provide default configurations,
like for example the saving path in below example. Remember that the `super()` call should
be always done at the end.

```python
class MyClass(Pyrmanent):
    def __init__(self, name, autosave=True):
        self.first_value = 1
        self.second_value = 2
        super().__init__(name=name, folder="data", autosave=autosave)
```

### Reset instance data

To reset instance data, call the `reset` method and then initialize the instance again.

```python
my_class_instance.reset()
my_class_instance = MyClass()
```

### Use dill instead of pickle

Dill extends the compatibility with several data types that pickle module can't serialize.
It provides the same interface, so it's totally compatible without any code change needed.
To start using dill, just install it using pip and it will be used by default:

    pip install dill --upgrade

To stop using dill, just uninstall it. You can find more information about dill in the
[official repo](https://github.com/uqfoundation/dill).

## License

Copyright © 2021 Sergio Abad. See [license](https://github.com/sergioteula/pyrmanent/blob/master/LICENSE) for details.
