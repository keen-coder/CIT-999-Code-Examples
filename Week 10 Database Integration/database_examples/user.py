class User:
    def __init__(self, first_name, last_name, age, street, city,
                 state, zipcode, phone, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.username = username
        self.password = password

    def full_name_first(self):
        return f"{self.first_name} {self.last_name}"

    def full_name_last(self):
        return f"{self.last_name} {self.first_name}"

    def address(self):
        return f"{self.street} \n           {self.city}, {self.state} {self.zipcode}"

    def __str__(self):
        return (
            f"Name     : {self.full_name_first()}\n"
            f"Age      : {self.age}\n"
            f"Address  : {self.address()}\n"
            f"Phone    : {self.phone}\n"
            f"Username : {self.username}\n"
            f"Password : {self.password}\n"
        )