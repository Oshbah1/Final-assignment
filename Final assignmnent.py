# Base class Employee
class Employee:
    def __init__(self, name, employee_id, department):
        self._name = name
        self._employee_id = employee_id
        self._department = department

    # Getters for name, employee_id, and department properties
    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_department(self):
        return self._department

    # Setters for name, employee_id, and department properties
    def set_name(self, name):
        self._name = name

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_department(self, department):
        self._department = department

    def print_details(self):
        print(f"Employee ID: {self._employee_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")

    def __str__(self):
        return f"Employee Name: {self._name}, ID: {self._employee_id}, Department: {self._department}"


# Accountant class inherits from Employee
# Accountant class inherits from Employee
class Accountant(Employee):
    def __init__(self, name, employee_id, department, certifications):
        super().__init__(name, employee_id, department)
        self._certifications = certifications

    # Getter for certifications property
    def get_certifications(self):
        return self._certifications

    # Setter for certifications property
    def set_certifications(self, certifications):
        self._certifications = certifications

    def __str__(self):
        return super().__str__() + f", Certifications: {self._certifications}"


# Marketer class inherits from Employee
class Marketer(Employee):
    pass


# Handyman class inherits from Employee
class Handyman(Employee):
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
event.rent_furniture(supplier,
                     ["Chairs", "Stage"])  # This operation demonstrates the dependency of Event on FurnitureSupplier

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
    pass


# Inherited class from Supplier for Cleaner
class Cleaner(Supplier):
    pass


# Inherited class from Supplier for Decorator
class Decorator(Supplier):
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

# Importing the necessary libraries for the program

import tkinter as tk
from tkinter import messagebox
import pickle
import os

data_path = "data"
os.makedirs(data_path, exist_ok=True)


class Entity:
    def __init__(self, entity_type, id_number, name, location, email):
        self.entity_type = entity_type
        self.id_number = id_number
        self.name = name
        self.location = location
        self.email = email

    def to_dict(self):
        return {
            "ID": self.id_number,
            "Name": self.name,
            "Location": self.location,
            "Email": self.email
        }


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Management System")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Entity to Manage:").pack(pady=5)

        entities = ["Employee", "Event", "Client", "Supplier", "Guest", "Venue"]
        self.entity_var = tk.StringVar(self)
        self.entity_var.set(entities[0])

        entity_option_menu = tk.OptionMenu(self, self.entity_var, *entities)
        entity_option_menu.pack()

        tk.Label(self, text="Enter ID Number").pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

        tk.Label(self, text="Enter Name").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Enter Position/Location").pack(pady=5)
        self.position_entry = tk.Entry(self)
        self.position_entry.pack()

        tk.Label(self, text="Enter Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        add_button = tk.Button(self, text="Add", command=self.add_entity)
        add_button.pack(pady=10)

        delete_button = tk.Button(self, text="Delete", command=self.delete_entity)
        delete_button.pack(pady=5)

        update_button = tk.Button(self, text="Update", command=self.update_entity)
        update_button.pack(pady=5)

        display_button = tk.Button(self, text="Display Details", command=self.display_details)
        display_button.pack(pady=5)

        next_page_button = tk.Button(self, text="Next Page", command=self.open_next_page)
        next_page_button.pack(pady=5)

    def add_entity(self):
        entity_type = self.entity_var.get()
        entity = Entity(entity_type, self.id_entry.get(), self.name_entry.get(), self.position_entry.get(),
                        self.email_entry.get())

        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            with open(filename, 'wb') as file:
                pickle.dump(entity.to_dict(), file)
            messagebox.showinfo("Success", f"{entity_type} added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add {entity_type}: {str(e)}")

    def delete_entity(self):
        entity_type = self.entity_var.get()
        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            os.remove(filename)
            messagebox.showinfo("Success", f"{entity_type} data deleted successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No {entity_type} data found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete {entity_type}: {str(e)}")

    def update_entity(self):
        entity_type = self.entity_var.get()
        entity = Entity(entity_type, self.id_entry.get(), self.name_entry.get(), self.position_entry.get(),
                        self.email_entry.get())

        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            with open(filename, 'wb') as file:
                pickle.dump(entity.to_dict(), file)
            messagebox.showinfo("Success", f"{entity_type} data updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update {entity_type}: {str(e)}")

    def display_details(self):
        entity_type = self.entity_var.get()
        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                messagebox.showinfo(f"{entity_type} Details", f"{entity_type} Data:\n{data}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No {entity_type} data found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display {entity_type} details: {str(e)}")

    def open_next_page(self):
        next_page = NextPage(self)
        self.withdraw()
        next_page.mainloop()
        self.deiconify()
    def open_next_page(self):
        new_window = tk.Toplevel(self)
        NextPage(new_window)


class NextPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Details Page")

        tk.Label(self.master, text="Enter Event ID:").pack(pady=10)
        self.event_id_entry = tk.Entry(self.master)
        self.event_id_entry.pack()

        event_details_button = tk.Button(self.master, text="Get Event Details", command=self.get_event_details)
        event_details_button.pack(pady=10)

        tk.Label(self.master, text="Enter Client ID:").pack(pady=10)
        self.client_id_entry = tk.Entry(self.master)
        self.client_id_entry.pack()

        client_details_button = tk.Button(self.master, text="Get Client Details", command=self.get_client_details)
        client_details_button.pack(pady=10)

        # Adding Supplier ID input and button
        tk.Label(self.master, text="Enter Supplier ID:").pack(pady=10)
        self.supplier_id_entry = tk.Entry(self.master)
        self.supplier_id_entry.pack()

        supplier_details_button = tk.Button(self.master, text="Get Supplier Details",
                                            command=self.display_supplier_details)
        supplier_details_button.pack(pady=10)
        # Widgets for Guest ID
        tk.Label(self.master, text="Enter Guest ID:").pack(pady=10)
        self.guest_id_entry = tk.Entry(self.master)
        self.guest_id_entry.pack()

        guest_details_button = tk.Button(self.master, text="Get Guest Details", command=self.display_guest_details)
        guest_details_button.pack(pady=10)

        # Widgets for Venue ID
        tk.Label(self.master, text="Enter Venue ID:").pack(pady=10)
        self.venue_id_entry = tk.Entry(self.master)
        self.venue_id_entry.pack()

        venue_details_button = tk.Button(self.master, text="Get Venue Details", command=self.display_venue_details)
        venue_details_button.pack(pady=10)
    def get_event_details(self):
        event_id = self.event_id_entry.get().strip()
        # Display  details for event E001
        if event_id == "E001":
            event = Event("E001", "Sample Event", "Sample Location", "2022-12-31")
            details = f"Event ID: {event.event_id}\nName: {event.name}\nLocation: {event.location}\nDate: {event.date}"
            messagebox.showinfo("MetGala,Newyork,Manhattan,2,1,2025,floral theme", details)
        else:
            messagebox.showerror("Error", "Event details not found.")

    def get_client_details(self):
        client_id = self.client_id_entry.get().strip()
        # Display  details for client E001
        if client_id == "E001":
            client = Client("E001", "Maria,", "Maria@client.com")
            details = f"Client ID: {client.id_number}\nName: {client.name}\nEmail: {client.email}"
            messagebox.showinfo("Client Details", details)
        else:
            messagebox.showerror("Error", "Client details not found.")

    def display_guest_details(self):
        guest_id = self.guest_id_entry.get().strip()
        #  function to simulate fetching guest details
        if guest_id == "E001":
            messagebox.showinfoguests = {
    "G001": {"name": "Alice", "email": "alice@example.com", "phone": "123-456-7890", "additional_info": "VIP Guest"},
    "G002": {"name": "Bob", "email": "bob@example.com", "phone": "234-567-8901", "additional_info": "Regular attendee"},
    "G003": {"name": "Charli", "email": "charli@example.com", "phone": "345-678-9012", "additional_info": "First-time attendee"}}
        else:
            messagebox.showerror("Error", "Guest details not found.")

            def show_guest_details():
                guest_id = id_entry.get().strip()
                guest = guests.get(guest_id)
                if guest:
                    details = (
                        f"Name: {guest['name']}\n"
                        f"Email: {guest['email']}\n"
                        f"Phone: {guest['phone']}\n"
                        f"Status: {guest['additional_info']}"
                    )
                    messagebox.showinfo("Guest Details", details)
                else:
                    messagebox.showerror("Error", "Guest details not found for ID: " + guest_id)



    def display_venue_details(self):
        venue_id = self.venue_id_entry.get().strip()
        # Mock function to simulate fetching venue details
        if venue_id == "E001":
            messagebox.showinfo("Venue Details",
                                "Details for Venue ID: V001: Name: Grand Hall, Location: Downtown, Capacity: 300")
        else:
            messagebox.showerror("Error", "Venue details not found.")



    def display_supplier_details(self):
        supplier_id = self.supplier_id_entry.get().strip()
        entities = self.load_data("suppliers.pkl")
        if supplier_id in entities:
            supplier = entities[supplier_id]
            details = f"ID: {supplier.id_number}, Name: {supplier.name}, Email: {supplier.email}"
            messagebox.showinfo("Supplier Details", details)
        else:
            messagebox.showerror("Error", "Supplier not found.")

    def get_event_details(self):
        event_id = self.event_id_entry.get().strip()
        #  function to simulate fetching event details
        if event_id == "E001":
            messagebox.showinfo("Event Details", "New York,Manhattan,2,1,2025, floral times")
        else:
            messagebox.showerror("Error", "Event details not found.")

    def get_client_details(self):
        client_id = self.client_id_entry.get().strip()
        # Mock function to simulate fetching client details
        if client_id == "E001":
            messagebox.showinfo("Client Details", "Meera,has an event that holds 200 guests,paid the deposit,choose a floral theme,agreed on a certain budget")
        else:
            messagebox.showerror("Error", "Client details not found.")

    def display_supplier_details(self):
        supplier_id = self.supplier_id_entry.get().strip()
        #  function to simulate fetching supplier details
        if supplier_id == "E001":
            messagebox.showinfo("Supplier A", "Supplies chairs and tables flowers and plates and supplies entertainment center for the client")
        else:
            messagebox.showerror("Error", "Supplier not found.")

    class EventDetails:

        def __init__(self, guest_id_entry, venue_id_entry):
            self.guest_id_entry = guest_id_entry
            self.venue_id_entry = venue_id_entry

        def display_guest_details(self):
            guest_id = self.guest_id_entry.get().strip()
            if guest_id == "E001":
                messagebox.showinfo("Guest A", "Attending as a VIP guest with a plus one.")
            else:
                messagebox.showerror("Error", "Guest not found.")

        def display_venue_details(self):
            venue_id = self.venue_id_entry.get().strip()
            if venue_id == "E001":
                messagebox.showinfo("Venue X", "Located in downtown area, capacity of 200 people.")
            else:
                messagebox.showerror("Error", "Venue not found.")

    # Example usage:
    # event = EventDetails(guest_id_entry, venue_id_entry)
    # event.display_guest_details()
    # event.display_venue_details()
if __name__ == "__main__":
    app = Application()
    app.mainloop()