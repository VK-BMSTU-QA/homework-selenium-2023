import unittest

from pages.pagePremiere import PagePremieres


class TestPremieresPage(unittest.TestCase, PagePremieres):
    EXPECTED_PREMIERES_TITLE = 'Премьеры'
    EXPECTED_FILM_ABOUT = """В эфире
On the Line
6.7
2023
18+
Режиссёр:
Ромуальд Буланже 
В ролях:
Мэл Гибсон, 
Уильям Моусли 
Трейлер"""

    def test_premieres_exist(self):
        self.render_page()

        actual_title = self.get_premiere_title()
        self.assertEqual(actual_title, self.EXPECTED_PREMIERES_TITLE, "premieres not available")

        actual_date_premiere = self.get_premiere_date()
        self.assertIsNotNone(actual_date_premiere, "premiere date not available")

    def test_premiers_film_poster_redirect(self):
        self.render_page()

        self.move_to_premiere_film()

        actual_film_about = self.get_premiere_film_about()
        self.assertEqual(actual_film_about, self.EXPECTED_FILM_ABOUT, "premiere film about not available")
