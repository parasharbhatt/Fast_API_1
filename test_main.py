import unittest
from datetime import datetime
from pathlib import Path
import sys
from uuid import uuid4

from fastapi.testclient import TestClient
from sqlalchemy import text

import database
import main

REPORT_PATH = Path(__file__).with_name("test_report.txt")


def _iter_test_cases(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from _iter_test_cases(test)
        else:
            yield test


def _write_test_report(cases, result):
    failed = {test.id() for test, _ in result.failures}
    errors = {test.id() for test, _ in result.errors}
    skipped = {test.id() for test, _ in result.skipped}
    expected_failures = {test.id() for test, _ in result.expectedFailures}
    unexpected_successes = {test.id() for test in result.unexpectedSuccesses}
    lines = [
        "Test execution report",
        f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"Python: {sys.executable}",
        "Database: Movies",
        "",
        f"Ran: {result.testsRun}",
        f"Passed: {result.testsRun - len(failed) - len(errors) - len(skipped) - len(expected_failures) - len(unexpected_successes)}",
        f"Failures: {len(failed)}",
        f"Errors: {len(errors)}",
        f"Skipped: {len(skipped)}",
        "",
        "Test cases:",
    ]

    for test in cases:
        test_id = test.id()
        if test_id in errors:
            status = "ERROR"
        elif test_id in failed:
            status = "FAIL"
        elif test_id in skipped:
            status = "SKIP"
        elif test_id in expected_failures:
            status = "EXPECTED FAILURE"
        elif test_id in unexpected_successes:
            status = "UNEXPECTED SUCCESS"
        else:
            status = "PASS"
        lines.append(f"{status}: {test_id}")

    details = [
        ("FAILURES", result.failures),
        ("ERRORS", result.errors),
        ("EXPECTED FAILURES", result.expectedFailures),
    ]
    for heading, outcomes in details:
        if outcomes:
            lines.extend(["", f"{heading}:"])
            for test, traceback in outcomes:
                lines.extend([test.id(), traceback])

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


class ReportingTestSuite(unittest.TestSuite):
    def run(self, result, debug=False):
        cases = list(_iter_test_cases(self))
        super().run(result, debug)
        _write_test_report(cases, result)
        print(f"\nTest report saved to: {REPORT_PATH}")
        return result


def load_tests(loader, standard_tests, pattern):
    return ReportingTestSuite(standard_tests)


class DatabaseApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(main.app)

    def test_create_and_get_user_then_return_404_after_cleanup(self):
        name = "API integration test"
        email = f"api-test-{uuid4().hex}@example.test"
        user_id = None

        try:
            create_response = self.client.post(
                "/users/",
                params={"name": name, "email": email},
            )
            self.assertEqual(create_response.status_code, 200, create_response.text)

            created_user = create_response.json()
            user_id = created_user["id"]
            self.assertEqual(created_user["name"], name)
            self.assertEqual(created_user["email"], email)

            get_response = self.client.get(f"/users/{user_id}")
            self.assertEqual(get_response.status_code, 200, get_response.text)
            self.assertEqual(get_response.json(), created_user)
        finally:
            with database.engine.begin() as connection:
                connection.execute(
                    text("DELETE FROM users WHERE email = :email"),
                    {"email": email},
                )

        not_found_response = self.client.get(f"/users/{user_id}")
        self.assertEqual(not_found_response.status_code, 404)
        self.assertEqual(not_found_response.json(), {"detail": "User not found"})

    def test_get_film_details_for_existing_film_id(self):
        with database.engine.connect() as connection:
            film_id = connection.execute(
                text("SELECT TOP (1) FilmID FROM FilmDetail ORDER BY FilmID")
            ).scalar()

        self.assertIsNotNone(film_id, "FilmDetail must contain a film for this test")

        response = self.client.get(f"/film-details/{film_id}")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["FilmID"], film_id)

    def test_get_film_details_returns_404_for_unknown_film_id(self):
        response = self.client.get("/film-details/2147483647")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Film not found"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
