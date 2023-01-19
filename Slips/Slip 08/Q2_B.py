
class String:

    def get_string(self):
        self.string = input("Enter the string: ")

    def print_string(self):
        return self.string.upper()

    def reverse_string(self):
        return self.string[::-1]


string_obj = String()
string_obj.get_string()
print(f"The string in upper case is: {string_obj.print_string()}")
print(f"The string in reverse is: {string_obj.reverse_string()}")