from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_data(self, fields, count):
        records = []
        for _ in range(count):
            record = {}
            for field_name, field_type in fields.items():
                if field_type == "string":
                    record[field_name] = self.fake.text(max_nb_chars=255)
                elif field_type == "email":
                    record[field_name] = self.fake.email()
                elif field_type == "date":
                    record[field_name] = self.fake.date()
                elif field_type == "reference":
                    record[field_name] = "003xx0000002TpdAAE"  # Replace with valid ID
                else:
                    record[field_name] = None
            records.append(record)
        return records
