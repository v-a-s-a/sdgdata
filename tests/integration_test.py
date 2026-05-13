import unittest

from pyunsdg import UNSDClient

class TestUNSDClientIntegration(unittest.TestCase):
    def setUp(self):
        self.client = UNSDClient()

    def test_get_geo_areas(self):
        print("\nTesting get_geo_areas...")
        areas = self.client.get_geo_areas()
        print(f"Received {len(areas)} areas.")
        if len(areas) > 0:
            print(f"Sample area: {areas[0]}")
        self.assertTrue(len(areas) > 0)
        self.assertIsNotNone(areas[0].geoAreaCode)
        self.assertIsNotNone(areas[0].geoAreaName)

    def test_get_targets(self):
        print("\nTesting get_targets...")
        targets = self.client.get_targets()
        print(f"Received {len(targets)} targets.")
        if len(targets) > 0:
            print(f"Sample target: {targets[0].code} - {targets[0].title}")
        self.assertTrue(len(targets) > 0)

    def test_get_series_codes(self):
        print("\nTesting get_series_codes for target '3.8'...")
        series = self.client.get_series_codes(target_code="3.8")
        print(f"Received {len(series)} series for target 3.8.")
        if len(series) > 0:
            print(f"Sample series: {series[0].code} - {series[0].description}")
        self.assertTrue(len(series) > 0)
        # We know they are from target 3.8 because we filtered for it in get_series_codes
        # Some series might have s.target as None in the nested response
        for s in series:
            self.assertIsNotNone(s.code)
            self.assertIsNotNone(s.description)

    def test_get_series_data(self):
        print("\nTesting get_series_data...")
        # Use get_series_codes to find valid series codes from target 3.8
        series = self.client.get_series_codes(target_code="3.8")
        self.assertTrue(len(series) > 0, "No series found for target 3.8")
        
        series_codes = [s.code for s in series if s.code]
        self.assertTrue(len(series_codes) > 0, "No series codes found for target 3.8")
        
        # Test with up to 2 series
        test_codes = series_codes[:2]
        print(f"Querying for series: {test_codes}")

        # Now fetch data for these series (Area 4 is Afghanistan)
        data = self.client.get_series_data(test_codes, area_code="4", start_period="2015", end_period="2020")
        
        print(f"Received {len(data)} observations")
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        if data:
            self.assertIsInstance(data[0], dict)

if __name__ == '__main__':
    unittest.main()
