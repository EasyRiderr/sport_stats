clean_db:
	rm -f sports.db

run:
	python3 feed_db.py

test:
	python3 -m unittest

check_style:
	find . -type f -name "*.py" | xargs python3 -m pylint
