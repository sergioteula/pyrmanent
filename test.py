from pyrmanent import Pyrmanent


class MyClass(Pyrmanent):
    def __init__(self, name="", folder="", autosave=True):
        self.hola = "Hola"
        self.adios = "Adios"
        self.castaña = "castaña"
        super().__init__(name=name, folder=folder, autosave=autosave)


myclass = MyClass()
# myclass.hola = "nuevo hola"
# myclass.save()

for key, value in myclass.__dict__.items():
    print(key, ":", value)
