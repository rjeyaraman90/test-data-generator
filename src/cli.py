import argparse

class CLI:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            description="Salesforce Data Generator: Generate and insert test data for Salesforce objects."
        )

        # Salesforce Authentication Parameters
        parser.add_argument(
            "--object", "-o", type=str, required=True,
            help="Salesforce object name (e.g., Account, Contact, CustomObject__c)."
        )
        parser.add_argument(
            "--record-count", "-r", type=int, default=5,
            help="Number of records to generate and insert. Default is 5."
        )

        # Optional Verbose Output
        parser.add_argument(
            "--verbose", "-v", action="store_true",
            help="Enable verbose output for debugging."
        )

        return parser.parse_args()
