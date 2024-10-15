# insurance_plan.py
from datetime import datetime
from typing import Optional


class InsurancePlan:
    def __init__(self, plan_name: str, coverage_details: str, provider: 'InsuranceProvider', 
                 max_coverage: float, created_at: Optional[datetime] = None):
        self.plan_name = plan_name
        self.coverage_details = coverage_details
        self.provider = provider  # Reference to an InsuranceProvider instance
        self.max_coverage = max_coverage
        self.created_at = created_at or datetime.now()
        self.updated_at = None  # To be updated later

    def update_plan(self, plan_name: str, coverage_details: str, max_coverage: float):
        """Update the details of the insurance plan."""
        self.plan_name = plan_name
        self.coverage_details = coverage_details
        self.max_coverage = max_coverage
        self.updated_at = datetime.now()

    def __str__(self):
        return f"InsurancePlan(plan_name={self.plan_name}, max_coverage={self.max_coverage})"
