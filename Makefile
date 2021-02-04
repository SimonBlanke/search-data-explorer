install:
	pip install .

reinstall:
	pip uninstall -y dashboard
	rm -fr build dist dashboard.egg-info
	python setup.py bdist_wheel
	pip install dist/*
