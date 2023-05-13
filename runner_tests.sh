export LOGIN=$1
export PASSWORD=$2
echo $LOGIN $PASSWORD

# pytest --numprocesses=1 testsbase/test_person.py
# pytest --numprocesses=1 testsbase/test_collection.py
pytest --numprocesses=1 testsbase/test.py
