install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py 
	black algoritmos/

lint:
	pylint --disable=R,C *.py
	pylint --disable=R,C,W0702 algoritmos/

all: install lint