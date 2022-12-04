import notable_assessment
import unittest

class TestTransformString(unittest.TestCase):
    # Run in terminal with: python -m unittest .\notable_assessment_tests.py
    def test_transform_string(self):
        input_str = "Patient presents today with several issues. Number one BMI has increased by 10 since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks Number next patient is taking drug number five several times a week"
        transformed_str = notable_assessment.transform_string(input_str)
        expected_str = "Patient presents today with several issues.\n1.  Bmi has increased by 10 since their last visit\n2.  Patient reports experiencing dizziness several times in the last two weeks.\n3.  Patient has a persistent cough that hasn’t improved for last 4 weeks\n4.  Patient is taking drug number five several times a week"
        #self.assertEqual(transformed_str, expected_str)
        self.assertEqual(expected_str, transformed_str)

    def test_transform_string_start_from_diff_number(self):
        input_str = "Patient presents today with several issues. Number five BMI has increased by 10 since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks Number next patient is taking drug number five several times a week"
        transformed_str = notable_assessment.transform_string(input_str)
        expected_str = "Patient presents today with several issues.\n5.  Bmi has increased by 10 since their last visit\n6.  Patient reports experiencing dizziness several times in the last two weeks.\n7.  Patient has a persistent cough that hasn’t improved for last 4 weeks\n8.  Patient is taking drug number five several times a week"
        #self.assertEqual(transformed_str, expected_str)
        self.assertEqual(expected_str, transformed_str)

    def test_transform_string_exception_emptystr(self):
        input_str = ""
        self.assertRaises(Exception, notable_assessment.transform_string, input_str)