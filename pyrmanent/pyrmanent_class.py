import os
from pickle import UnpicklingError

try:
    import dill as pickle
except ImportError:
    import pickle


class PyrmanentError(Exception):
    """Base class for Pyrsistent exceptions"""


class Pyrmanent:
    """This class makes data permanent using object storage with pickle. If you want to
    use dill instead, just install it using pip. Your custom class should inherit from
    this one.

    Args:
        name (``str``): The instance identificator name. Defaults to blank.
        folder (``str``): Folder where pickle files should be saved. Defaults to blank.
        autosave (``bool``): Allows saving by calling autosave method. Defaults to True.

    Raises:
        ``PyrsistentError``: On save or load errors.
    """

    def __init__(self, name="", folder="", autosave=True):
        self._name = str(name)
        self._autosave = autosave
        self._filename = self._get_filename()
        self._folder = None
        self._path = None
        self._create_folder(folder)

        if not self.load():
            self.save()

    def load(self):
        """Loads the instance data from the previously saved file."""
        try:
            if os.path.isfile(self._path):
                with open(self._path, "rb") as file:
                    data = pickle.load(file)
                    self.__dict__.update(data.__dict__)
                return True

            with open(self._path, "xb"):
                return False

        except (UnpicklingError, AttributeError, EOFError, IndexError, IOError) as exc:
            exc_msg = "Error saving %s: %s" % (self._filename, exc)
            raise PyrmanentError(exc_msg) from exc

    def save(self):
        """Saves the current instance data to a file."""
        try:
            data = pickle.dumps(self)
            with open(self._path, "wb") as file:
                file.write(data)

        except (TypeError, IOError) as exc:
            exc_msg = "Error saving %s: %s" % (self._filename, exc)
            raise PyrmanentError(exc_msg) from exc

    def autosave(self):
        """Saves the current instance data to a file only if autosave is true."""
        if self._autosave:
            self.save()

    def _create_folder(self, folder):
        self._prepare_path(folder)

        if self._folder and not os.path.exists(self._folder):
            try:
                os.makedirs(self._folder)
            except OSError as exc:
                exc_msg = "Folder creation error for %s: %s"
                raise PyrmanentError(exc_msg, self._filename, exc) from exc

    def _prepare_path(self, folder):
        if folder:
            folder = folder.replace("\\", "/")
            if folder[-1] != "/":
                folder += "/"

        self._folder = folder
        self._path = self._folder + self._filename

    def _get_filename(self):
        if not self._name:
            return self.__class__.__name__ + ".pickle"
        return self.__class__.__name__ + "_" + self._name + ".pickle"
