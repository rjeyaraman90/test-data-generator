import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Test Data Generator CLI Tool")
    parser.add_argument("--output", "-o", type=str, default="data/test_data.json",
                        help="Output file path for the generated data (default: data/test_data.json)")
    parser.add_argument("--count", "-c", type=int, default=10,
                        help="Number of test records to generate (default: 10)")
    parser.add_argument("--schema", "-s", type=str, required=True,
                        help="Path to the schema file defining the data structure")
    return parser.parse_args()

