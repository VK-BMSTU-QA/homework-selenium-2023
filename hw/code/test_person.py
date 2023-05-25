import unittest

from pages.pagePerson import PersonPage


class TestPersonNotAuthorized(unittest.TestCase, PersonPage):
    EXPECTED_PERSON = "Хоакин Феникс"
    EXPECTED_FILM_ID = '28'

    def test_film_contains_person(self):
        self.render_page()

        actual_film_id = self.get_film_id_person()

        # check film_id
        self.assertEqual(actual_film_id, self.EXPECTED_FILM_ID, "this film not expected")

        # check film main person
        actual_person = self.get_film_main_actor()
        self.assertIn(self.EXPECTED_PERSON, actual_person, "this film without expected person")
