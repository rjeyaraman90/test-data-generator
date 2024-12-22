from src.data_generator import DataGenerator


def test_generate_data():
    fields = {"Name": "string", "Email": "email", "CreatedDate": "date"}
    generator = DataGenerator()
    records = generator.generate_data(fields, 3)

    assert len(records) == 3
    for record in records:
        assert "Name" in record
        assert "Email" in record
        assert "CreatedDate" in record
