import argparse
import json
from faker import Faker

"""
This method is used to define the basic CLI structure
--output/-o : specifies the output file for generated test data
--count/-c : specifies the number of test records to generate
--schema/-s : specifies the file path for test data schema

:returns an object of user's CLI inputs
"""
def parse_args():
    parser = argparse.ArgumentParser(description="Test Data Generator CLI Tool")
    parser.add_argument("--output", "-o", type=str, default="data/test_data.json",
                        help="Output file path for the generated data (default: data/test_data.json)")
    parser.add_argument("--count", "-c", type=int, default=10,
                        help="Number of test records to generate (default: 10)")
    parser.add_argument("--schema", "-s", type=str, required=True,
                        help="Path to the schema file defining the data structure")
    return parser.parse_args()

"""
This method reads a JSON schema file and generates test data using faker library
The loop runs for "count" times
It creates an empty dictionary for each count and populates the test data 
The created record is then appended to the test_data list
"""
def generate_test_data(schema_path, count):
    fake = Faker()

    with open(schema_path, 'r') as schema_file:
        schema = json.load(schema_file)

    test_data = []
    for _ in range(count):
        record = {}
        for key, value in schema.items():
            if hasattr(fake, value):
                record[key] = getattr(fake, value)()
            else:
                record[key] = f"Unsupported field: {value}"
        test_data.append(record)
    return test_data

"""
This method is used to write the generated test data into a file
"""
def write_test_data_to_file(data, output_path):

    with open(output_path, 'w') as output_file:
        json.dump(data, output_file, indent=4)
    print(f"Test data written to {output_path}")

if __name__ == "__main__":
    args = parse_args()
    test_data = generate_test_data(args.schema, args.count)
    write_test_data_to_file(test_data, args.output)


