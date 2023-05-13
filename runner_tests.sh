export LOGIN=$1
export PASSWORD=$2
echo $LOGIN $PASSWORD

# pytest testsbase/test_person.py
pytest testsbase/test_collection.py
# pytest testsbase/test.py
