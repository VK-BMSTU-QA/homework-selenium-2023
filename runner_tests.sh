export LOGIN=$1
export PASSWORD=$2
echo $LOGIN $PASSWORD

pytest hw/code/test_login.py
pytest hw/code/test_signup.py
pytest hw/code/test_profile.py

pytest hw/code/test_collection.py
pytest hw/code/test_person.py

pytest hw/code/test_search.py
pytest hw/code/test_film_unauth.py
pytest hw/code/test_film_auth.py

pytest hw/code/test_navigation.py
pytest hw/code/test_mainpage.py
pytest hw/code/test_premierepage.py
