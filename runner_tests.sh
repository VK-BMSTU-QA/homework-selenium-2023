export LOGIN=$1
export PASSWORD=$2
echo $LOGIN $PASSWORD

pytest --numprocesses=1 testsbase/test_person.py
pytest --numprocesses=1 testsbase/test_collection.py

pytest --numprocesses=1 testsbase/test_login.py
pytest --numprocesses=1 testsbase/test_signup.py
pytest --numprocesses=1 testsbase/test_profile.py

pytest --numprocesses=1 testsbase/test_navigation.py
pytest --numprocesses=1 testsbase/test_mainpage.py
pytest --numprocesses=1 testsbase/test_premierepage.py

pytest --numprocesses=1 testsbase/test.py
