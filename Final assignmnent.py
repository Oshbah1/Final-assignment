# Base class Employee
class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def print_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"Employee Name: {self.name}, ID: {self.employee_id}, Department: {self.department}"

# Accountant class inherits from Employee
class Accountant(Employee):
    def __init__(self, name, employee_id, department, certifications):
        super().__init__(name, employee_id, department)
        self.certifications = certifications

    def __str__(self):
        return super().__str__() + f", Certifications: {self.certifications}"

# Marketer class inherits from Employee
class Marketer(Employee):
    # Additional marketer-specific attributes and methods can be added here
    pass

# Handyman class inherits from Employee
class Handyman(Employee):
    # Additional handyman-specific attributes and methods can be added here
    pass

# Salesperson class inherits from Employee
class Salesperson(Employee):
    def __init__(self, name, employee_id, department, sales_target):
        super().__init__(name, employee_id, department)
        self.sales_target = sales_target

    def __str__(self):
        return super().__str__() + f", Sales Target: {self.sales_target}"

# SalesManager class inherits from Salesperson
class SalesManager(Salesperson):
    def __init__(self, name, employee_id, department, sales_target, team_size):
        super().__init__(name, employee_id, department, sales_target)
        self.team_size = team_size

    def __str__(self):
        return super().__str__() + f", Team Size: {self.team_size}"

# Designer class inherits from Employee
class Designer(Employee):
    def __init__(self, name, employee_id, department, portfolio):
        super().__init__(name, employee_id, department)
        self.portfolio = portfolio

    def __str__(self):
        return super().__str__() + f", Portfolio: {self.portfolio}"

# Main program where we will create the instances or objects of the classes
if __name__ == "__main__":
    accountant = Accountant("Oshbah", "E001", "Finance", ["CPA"])
    marketer = Marketer("Hamda", "E002", "Marketing")
    handyman = Handyman("Ahmed", "E003", "Maintenance")
    salesperson = Salesperson("Dana", "E004", "Sales", 50000)
    sales_manager = SalesManager("Evan", "E005", "Sales", 100000, 5)
    designer = Designer("Fiona", "E006", "Design", "www.fionasportfolio.com")

    # Print the details of each employee
    for employee in [accountant, marketer, handyman, salesperson, sales_manager, designer]:
        print(employee)
        print()  # Adding a newline for better readability

class SalesPerson:
    def __init__(self, name, clients=None):
        # SalesPerson constructor with an optional list of clients
        self.name = name
        self.clients = clients if clients is not None else []  # Represents an association with Client objects

    def add_client(self, client):
        # Adds a client to the SalesPerson's list of clients, representing an association
        self.clients.append(client)
        client.sales_person = self  # This establishes a bidirectional association

    def get_clients(self):
        # Returns the list of client names associated with the SalesPerson
        return [client.name for client in self.clients]

    def __str__(self):
        # String representation of SalesPerson and their associated clients
        return f"SalesPerson {self.name} manages clients: {self.get_clients()}"

class Client:
    def __init__(self, name, sales_person=None):
        # Client constructor with an optional reference to a SalesPerson
        self.name = name
        self.sales_person = sales_person  # Represents an association with a SalesPerson object

    def assign_sales_person(self, sales_person):
        # Assigns a SalesPerson to the client, establishing an association
        self.sales_person = sales_person
        sales_person.add_client(self)  # Completes the bidirectional association

    def __str__(self):
        # String representation of Client and their associated SalesPerson
        return f"Client {self.name} managed by SalesPerson: {self.sales_person.name if self.sales_person else 'None'}"

# Main program
s1 = SalesPerson("Alice")
c1 = Client("XYZ Corp")

# Associate client with sales person, establishing the association between them
c1.assign_sales_person(s1)  # This line creates the association as per the sample code

print(s1)  # Output information about the SalesPerson and their associated clients
print(c1)  # Output information about the
class Event:
    def __init__(self, event_id, date):
        self.event_id = event_id
        self.date = date

    def rent_furniture(self, furniture_supplier, furniture_list):
        # Event class depends on FurnitureSupplier class because it uses its rent_furniture_service
        furniture_supplier.rent_furniture_service(furniture_list)  # Calling the function creates a dependency

    def __str__(self):
        return f"Event {self.event_id} on date {self.date}"

class FurnitureSupplier:
    def __init__(self, supplier_id):
        self.supplier_id = supplier_id
        self.available_furniture = ["Chairs", "Tables", "Sofas"]  # Example furniture items

    def rent_furniture_service(self, furniture_list):
        # Updates the status of furniture to "Rented"
        for furniture in furniture_list:
            if furniture in self.available_furniture:
                print(f"{furniture} rented.")
            else:
                print(f"{furniture} is not available for rent.")
        # This method could update the status or inventory of furniture, indicating a dependency

    def __str__(self):
        return f"FurnitureSupplier {self.supplier_id}"

# Main program
event = Event("E123", "2024-05-01")
supplier = FurnitureSupplier("S456")

# Event renting furniture from the supplier
event.rent_furniture(supplier, ["Chairs", "Stage"])  # This operation demonstrates the dependency of Event on FurnitureSupplier

# Output information about the Event and FurnitureSupplier
print(event)
print(supplier)
class Event:
    def __init__(self, event_id, date):
        self.event_id = event_id
        self.date = date
        self.suppliers = []  # Aggregates Suppliers, but the event doesn't own Suppliers
        self.guests = []  # Aggregates Guests, but the event doesn't own Guests

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)  # Aggregating supplier objects

    def invite_guests(self, guest_list):
        self.guests.extend(guest_list)  # Aggregating guest objects

    def __str__(self):
        return f"Event {self.event_id} on date {self.date}"

class Supplier:
    def __init__(self, name, supplies):
        self.name = name
        self.supplies = supplies

    def __str__(self):
        return f"Supplier {self.name}, Supplies: {self.supplies}"

class Guest:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Guest {self.name}"

# Main program
event = Event("E123", "2024-05-01")
supplier1 = Supplier("Supplier A", ["Chairs", "Tables"])
supplier2 = Supplier("Supplier B", ["Stage", "Lighting"])

# Event aggregates suppliers
event.add_supplier(supplier1)
event.add_supplier(supplier2)

# Guests are created here and sent to the Event
guest1 = Guest("Alice")
guest2 = Guest("Bob")
guest3 = Guest("Charlie")
guest_list = [guest1, guest2, guest3]

# Event aggregates guests
event.invite_guests(guest_list)

# Output information about the Event, Suppliers, and Guests
print(event)
for supplier in event.suppliers:
    print(supplier)

for guest in event.guests:
    print(guest)
class Event:
    def __init__(self, event_id, date):
        self.event_id = event_id
        self.date = date
        self.agenda = EventAgenda()  # Event owns EventAgenda - composition relationship

    def add_agenda_item(self, start_time, end_time, description):
        # Event directly manages its EventAgenda's items
        self.agenda.add_item(start_time, end_time, description)

    def __str__(self):
        return f"Event {self.event_id} on {self.date} with Agenda: {self.agenda}"

class EventAgenda:
    def __init__(self):
        self.items = []  # List of agenda items

    def add_item(self, start_time, end_time, description):
        self.items.append({'start_time': start_time, 'end_time': end_time, 'description': description})

    def __str__(self):
        return f"{[f'{item['start_time']} to {item['end_time']}: {item['description']}' for item in self.items]}"

# Main program - Only the Event is created here, not the EventAgenda, which is created by the Event itself
event = Event("E123", "2024-05-01")

# Adding agenda items to the Event
event.add_agenda_item("09:00", "10:00", "Opening Ceremony")
event.add_agenda_item("10:00", "12:00", "Guest Speaker Session")
event.add_agenda_item("12:00", "13:00", "Lunch Break")
# Base class for all suppliers
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def display_details(self):
        # Print the details of the supplier
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact Details: {self.contact_details}")

    def __str__(self):
        # String representation of a Supplier
        return f"{self.name} ({self.supplier_id})"

# Inherited class from Supplier for Venue
class Venue(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, capacity):
        # Initialize the base class
        super().__init__(supplier_id, name, address, contact_details)
        # Venue-specific attribute
        self.capacity = capacity

    def __str__(self):
        # Extend the string representation with capacity information
        return super().__str__() + f", Capacity: {self.capacity}"

# Inherited class from Supplier for Caterer
class Caterer(Supplier):
    # Additional attributes or methods for Caterer can be added here
    pass

# Inherited class from Supplier for Cleaner
class Cleaner(Supplier):
    # Additional attributes or methods for Cleaner can be added here
    pass

# Inherited class from Supplier for Decorator
class Decorator(Supplier):
    # Additional attributes or methods for Decorator can be added here
    pass

# Inherited class from Supplier for Entertainer
class Entertainer(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, genre):
        super().__init__(supplier_id, name, address, contact_details)
        # Entertainer-specific attribute
        self.genre = genre

    def __str__(self):
        # Extend the string representation with genre information
        return super().__str__() + f", Genre: {self.genre}"

# Main program
# Creating instances of the subclasses
venue = Venue("V001", "Grand Hall", "123 Venue St.", "555-1234", 200)
caterer = Caterer("C002", "Gourmet Catering", "456 Food Ave.", "555-5678")
cleaner = Cleaner("CL003", "Sparkle Clean", "789 Clean Blvd.", "555-9012")
decorator = Decorator("D004", "Elegant Decor", "321 Decor Ln.", "555-3456")
entertainer = Entertainer("E005", "Jazz Band", "654 Music Rd.", "555-7890", "Jazz")

# Displaying details of the instances
print(venue)
print(caterer)
print(cleaner)
print(decorator)
print(entertainer)


# Output information about the Event and its composed EventAgenda
print(event)
import tkinter as tk
from tkinter import messagebox
import pickle
import os

# Entity class to represent different types of data entries
class Entity:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# DataLayer class to handle data storage and retrieval
class DataLayer:
    def __init__(self, file_prefix):
        self.file_prefix = file_prefix

    def save(self, entity_type, data_dict):
        with open(f'{self.file_prefix}_{entity_type}.pkl', 'wb') as file:
            pickle.dump(data_dict, file)

    def load(self, entity_type):
        try:
            with open(f'{self.file_prefix}_{entity_type}.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

# Main GUI class
class ManagementSystemGUI:
    def __init__(self, root, data_layer):
        self.root = root
        self.data_layer = data_layer
        self.entities = {}
        self.entity_type = tk.StringVar(self.root)
        self.entity_type.set('employee')  # default value

        self.setup_gui()

    def setup_gui(self):
        # Dropdown menu to select entity type
        entity_options = ['employee', 'event', 'client', 'guest', 'supplier', 'venue']
        self.entity_type_menu = tk.OptionMenu(self.root, self.entity_type, *entity_options)
        self.entity_type_menu.pack()

        # Buttons for operations
        tk.Button(self.root, text="Add", command=self.add_entity).pack()
        tk.Button(self.root, text="Delete", command=self.delete_entity).pack()
        tk.Button(self.root, text="Modify", command=self.modify_entity).pack()
        tk.Button(self.root, text="Display", command=self.display_entity).pack()

    def add_entity(self):
        # TODO: Add logic to collect entity details from the user and store it
        pass

    def delete_entity(self):
        # TODO: Add logic to delete an entity based on a unique identifier
        pass

    def modify_entity(self):
        # TODO: Add logic to modify an existing entity's details
        pass

    def display_entity(self):
        # TODO: Add logic to display an entity's details
        pass

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Management System")
    data_layer = DataLayer(file_prefix='data')
    app = ManagementSystemGUI(root, data_layer)
    root.mainloop()


