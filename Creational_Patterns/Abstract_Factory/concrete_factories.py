from abstract_factory import GUIFactory
from abstract_products import Button, Checkbox
from concrete_products import (
    WindowsButton,
    WindowsCheckbox,
    MacButton,
    MacCheckbox
)

# Factory for creating Windows-style UI elements
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Factory for creating Mac-style UI elements
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
