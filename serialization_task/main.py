from enum import Enum
import struct


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():

    def __init__(self, parent):
        self.parent = parent
        self.childrens = []
        if self.parent is not None:
            self.parent.add_children(self)

    def add_children(self, children: "Widget"):
        self.childrens.append(children)

    def to_binary(self):
        class_name = self.__class__.__name__.encode()
        res = struct.pack("i", len(class_name)) + class_name

        if isinstance(self, Layout):
            res += struct.pack("i", self.alignment.value)
        elif isinstance(self, LineEdit):
            res += struct.pack("i", self.max_length)
        elif isinstance(self, ComboBox):
            items = [str(item) for item in self.items]
            items_str = ";".join(items).encode()
            res += struct.pack("i", len(items_str)) + items_str
        elif isinstance(self, MainWindow):
            res += struct.pack("i", len(self.title.encode())) + self.title.encode()

        data = b""
        for child in self.childrens:
            node = child.to_binary()
            data += node
        res += struct.pack("i", len(data)) + data
        return res

    @classmethod
    def from_binary(cls, data, parent=None):
        class_name_len = struct.unpack("i", data[:4])[0]
        curr_pos = 4
        class_name = data[curr_pos:curr_pos + class_name_len].decode()
        curr_pos += class_name_len

        property_len = struct.unpack("i", data[curr_pos:curr_pos + 4])[0]
        curr_pos += 4
        property_value = data[curr_pos:curr_pos + property_len].decode()
        curr_pos += property_len

        root_element = None
        if class_name == "MainWindow":
            root_element = cls(property_value)
        elif class_name == "Layout":
            curr_pos -= property_len
            root_element = Layout(parent, property_len)
        elif class_name == "LineEdit":
            curr_pos -= property_len
            root_element = LineEdit(parent, property_len)
        elif class_name == "ComboBox":
            root_element = ComboBox(parent, property_value)

        children_len = struct.unpack("i", data[curr_pos:curr_pos + 4])[0]
        curr_pos += 4
        children_data = data[curr_pos:]

        cursor = 0
        while cursor < children_len:
            child_node, child_cursor = root_element.from_binary(children_data[cursor:], parent=root_element)
            cursor += child_cursor

        return root_element, curr_pos + cursor

    def __str__(self):
        return f"{self.__class__.__name__}{self.childrens}"

    def __repr__(self):
        return str(self)


class MainWindow(Widget):

    def __init__(self, title: str):
        super().__init__(None)
        self.title = title


class Layout(Widget):

    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment


class LineEdit(Widget):

    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length


class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items


app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(app)

bts = app.to_binary()
print(f"Binary data length {len(bts)}")

new_app = MainWindow.from_binary(bts)
print(new_app)
