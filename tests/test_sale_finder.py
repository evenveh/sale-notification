import unittest
from unittest.mock import patch, MagicMock
from sale_finder import get_sales


class TestGetSales(unittest.TestCase):

    @patch("sale_finder.webdriver.Chrome")
    def test_get_sales(self, mock_webdriver):
        """Test get_sales function with mocked Selenium"""

        mock_driver = MagicMock()
        mock_webdriver.return_value.__enter__.return_value = mock_driver

        mock_driver.find_elements.return_value = [
            MagicMock(
                find_element=MagicMock(
                    side_effect=lambda by, name: MagicMock(
                        text="Gibson Les Paul" if "AddHeader1" in name else "20% off")
                )
            )
        ]

        url = "https://www.example.com"
        result = get_sales(url)

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Gibson Les Paul: 20% off", result)


if __name__ == "__main__":
    unittest.main()
