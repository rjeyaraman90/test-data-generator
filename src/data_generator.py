from faker import Faker

class DataGenerator:
    """
    Generates realistic test data for Salesforce objects based on metadata.
    """
    def __init__(self):
        """
        Initializes the data generator with the Faker library.
        """
        self.fake = Faker()

    def generate_data(self, fields, count):
        """
                Generates a list of records with fake data for the specified fields.

                Args:
                    fields (dict): A dictionary of field names and their types.
                    count (int): Number of records to generate.

                Returns:
                    list: A list of dictionaries representing the generated records.
        """
        records = []

        for _ in range(count):
            record = {}
            for field_name, field_type in fields.items():
                records[field_name] = self.generate_field_data(field_type)
            records.append(record)
        return records

    def generate_field_data(self, field_type):
        """
                Generates fake data for a specific field type.

                Args:
                    field_type (str): The Salesforce field type (e.g., "string", "email").

                Returns:
                    str: Generated fake data for the field.
        """
        if field_type == 'string':
            return self.fake.text(max_nb_chars=255)
        elif field_type == 'email':
            return self.fake.email()
        elif field_type == 'date':
            return self.fake.date()
        elif field_type == 'phone':
            return self.fake.phone_number()
        elif field_type == 'url':
            return self.fake.url()
        elif field_type == 'integer':
            return self.fake.random_int(min=0, max=1000)
        elif field_type == 'boolean':
            return self.fake.boolean()
        elif field_type == 'id':
            return None
        else:
            return None
