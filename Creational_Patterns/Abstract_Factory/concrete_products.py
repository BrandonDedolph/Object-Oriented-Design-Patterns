from abstract_products import Button, Checkbox

# Concrete Windows Button
class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows-style button"

# Concrete Windows Checkbox
class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering a Windows-style checkbox"

# Concrete Mac Button
class MacButton(Button):
    def render(self):
        return "Rendering a Mac-style button"

# Concrete Mac Checkbox
class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering a Mac-style checkbox"
