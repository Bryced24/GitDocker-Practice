import unittest
from nearest_city import nearest, global_cities


class NearestCityTest(unittest.TestCase):

    def test_nearest_city_1(self) -> None:
        city = 'Mulathing'
        ans = nearest(city, global_cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)

    def test_nearest_city_2(self) -> None:
        city = 'Mosfellsbaer'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)

    def test_nearest_city_3(self) -> None:
        city = 'Reykjavik'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)

    def test_nearest_city_4(self) -> None:
        city = 'Akureyri'
        ans = nearest(city, global_cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)

    def test_nearest_city_5(self) -> None:
        city = 'Kopavogur'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)

    def test_nearest_city_6(self) -> None:
        city = 'Mosfellsbaer'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
