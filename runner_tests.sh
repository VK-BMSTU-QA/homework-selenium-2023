export LOGIN=$1
export PASSWORD=$2
echo $LOGIN $PASSWORD

pytest testsbase/test_collection.py
pytest testsbase/test_person.py

pytest testsbase/test_search.py
pytest testsbase/test_film_unauth.py
pytest testsbase/test.py

pytest testsbase/test_login.py
pytest testsbase/test_signup.py
pytest testsbase/test_profile.py

pytest testsbase/test_navigation.py
pytest testsbase/test_mainpage.py
pytest testsbase/test_premierepage.py
