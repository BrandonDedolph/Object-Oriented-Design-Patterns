from abstract_factory import GUIFactory
from concrete_factories import WindowsFactory, MacFactory

def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


# Windows UI
print("Creating Windows UI")
windows_factory = WindowsFactory()
create_ui(windows_factory)

# Mac UI
print("Creating Mac UI")
mac_factory = MacFactory()
create_ui(mac_factory)
