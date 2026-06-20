from pathlib import Path
import unittest

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml"


def load_template():
    with TEMPLATE_PATH.open(encoding="utf-8") as template_file:
        return yaml.safe_load(template_file)


class FeatureRequestTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = load_template()
        cls.body = cls.template["body"]
        cls.fields = {field.get("id"): field for field in cls.body if "id" in field}

    def test_template_metadata_routes_feature_requests(self):
        self.assertEqual(self.template["name"], "Feature Request")
        self.assertEqual(self.template["title"], "[FEATURE] ")
        self.assertEqual(self.template["labels"], ["enhancement"])
        self.assertIn("governance context", self.template["description"])

    def test_body_fields_are_unique_and_ordered_for_triage(self):
        ids = [field.get("id") for field in self.body if "id" in field]

        self.assertEqual(
            ids,
            [
                "organ",
                "outcome",
                "problem",
                "acceptance",
                "alternatives",
                "tier",
                "governance",
                "context",
            ],
        )
        self.assertEqual(len(ids), len(set(ids)))

    def test_required_fields_capture_minimum_feature_spec(self):
        required_ids = {
            field_id
            for field_id, field in self.fields.items()
            if field.get("validations", {}).get("required") is True
        }

        self.assertEqual(required_ids, {"organ", "outcome", "problem", "acceptance"})
        for field_id in required_ids:
            self.assertIn("label", self.fields[field_id]["attributes"])
            self.assertTrue(self.fields[field_id]["attributes"]["label"])

    def test_organ_dropdown_contains_expected_routing_choices(self):
        organ = self.fields["organ"]
        options = organ["attributes"]["options"]

        self.assertEqual(organ["type"], "dropdown")
        self.assertIn("ORGAN-IV (Taxis)", options)
        self.assertIn("META-ORGANVM", options)
        self.assertIn("Cross-organ", options)
        self.assertEqual(len(options), len(set(options)))

    def test_acceptance_criteria_prompt_is_testable(self):
        acceptance = self.fields["acceptance"]
        value_lines = [
            line.strip()
            for line in acceptance["attributes"]["value"].splitlines()
            if line.strip()
        ]

        self.assertEqual(acceptance["type"], "textarea")
        self.assertIn("3-7 testable criteria", acceptance["attributes"]["description"])
        self.assertEqual(value_lines, ["- [ ]", "- [ ]", "- [ ]"])

    def test_governance_gates_cover_high_risk_feature_changes(self):
        governance = self.fields["governance"]
        gate_labels = [
            option["label"] for option in governance["attributes"]["options"]
        ]

        self.assertEqual(governance["type"], "checkboxes")
        self.assertIn("Changes CI/CD workflows", gate_labels)
        self.assertIn("Modifies governance rules or promotion logic", gate_labels)
        self.assertIn(
            "Affects data classification (Public/Internal/Confidential/Regulated)",
            gate_labels,
        )
        self.assertIn("Requires seed.yaml update", gate_labels)
        self.assertEqual(len(gate_labels), len(set(gate_labels)))


if __name__ == "__main__":
    unittest.main()
