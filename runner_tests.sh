export LOGIN=$1
export PASSWORD=$2
echo $LOGIN $PASSWORD

# pytest testsbase/test_person.py
pytest --numprocesses=1 testsbase/test_collection.py
# pytest testsbase/test.py
