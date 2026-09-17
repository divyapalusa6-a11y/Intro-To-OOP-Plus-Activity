# add your Student class here!
class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_to_add):
            self.classes.append(class_to_add)
            return self.classes
        
    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        class_count = "class" if self.get_num_classes() == 1 else "classes"
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} {class_count}"