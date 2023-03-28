class Package:
    # Package constructor
    def __init__(self, package_id, delivery_address, delivery_city, delivery_state, delivery_zip, delivery_deadline,
                 delivery_time, package_weight,
                 delivery_status, departure_time):
        self.delivery_state = delivery_state
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_deadline = delivery_deadline
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time
        self.departure_time = departure_time

    def update_status(self, time):
        if time < self.departure_time:
            self.delivery_status = "At Hub"
        elif self.departure_time <= time < self.delivery_time:
            self.delivery_status = "En Route"
        else:
            self.delivery_status = "Delivered at %s" % self.delivery_time

    # Package string constructor
    def __str__(self):
        return "ID: %s, Address: %s %s, %s %s, Deadline: %s, Weight: %s, Status: %s" % (self.package_id, self.delivery_address, self.delivery_city,
                                                       self.delivery_state, self.delivery_zip,
                                                       self.delivery_deadline, self.package_weight,
                                                       self.delivery_status)
