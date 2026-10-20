
"""
Synthetic Data Quality & Edge-Case Generator
Author: Shirleen Wambui Gatu
Purpose: Programmatically generate clean test records and intentionally 
         inject edge-case corruption to stress-test data ingestion pipelines.
"""

import json
import random
from typing import List, Dict, Any

class SyntheticDataGenerator:
    """Generates valid datasets and mutation stress-tests for QA pipelines."""
    
    def __init__(self):
        self.sample_names = ["Alice Smith", "Bob Jones", "Charlie Mwangi", "Diana Ochieng", "Evan Wright"]
        self.sample_statuses = ["active", "pending", "suspended", "verified"]

    def generate_clean_record(self, record_id: int) -> Dict[str, Any]:
        """Generates a clean, perfectly structured data record."""
        return {
            "id": record_id,
            "full_name": random.choice(self.sample_names),
            "account_balance": round(random.uniform(100.0, 50000.0), 2),
            "status": random.choice(self.sample_statuses),
            "is_flagged": False
        }

    def inject_edge_case_mutation(self, clean_record: Dict[str, Any], mutation_type: str) -> Dict[str, Any]:
        """
        Intentionally corrupts a clean record based on specified QA test scenarios 
        to test system recovery and error handling.
        """
        mutated = clean_record.copy()
        
        if mutation_type == "missing_required_field":
            # Remove a critical key
            mutated.pop("id", None)
            
        elif mutation_type == "type_mismatch":
            # Pass string where float is expected
            mutated["account_balance"] = "INVALID_CURRENCY_STRING"
            
        elif mutation_type == "out_of_bounds":
            # Pass negative balance or invalid status
            mutated["account_balance"] = -99999.99
            mutated["status"] = "unknown_status_flag"
            
        elif mutation_type == "null_payload":
            return {}
            
        return mutated

    def generate_test_suite(self, total_records: int = 10) -> List[Dict[str, Any]]:
        """Produces a mixed batch of clean and intentionally corrupted test payloads."""
        suite = []
        mutation_types = ["missing_required_field", "type_mismatch", "out_of_bounds", "null_payload"]
        
        for i in range(1, total_records + 1):
            clean_rec = self.generate_clean_record(i)
            # 50% chance to mutate record for edge-case testing
            if i % 2 == 0:
                mut_type = random.choice(mutation_types)
                corrupted_rec = self.inject_edge_case_mutation(clean_rec, mut_type)
                suite.append({"test_id": i, "type": "corrupted", "mutation": mut_type, "payload": corrupted_rec})
            else:
                suite.append({"test_id": i, "type": "clean", "mutation": None, "payload": clean_rec})
                
        return suite

if __name__ == "__main__":
    generator = SyntheticDataGenerator()
    test_batch = generator.generate_test_suite(total_records=4)
    
    print("--- Generated QA Test Suite ---")
    print(json.dumps(test_batch, indent=2))
