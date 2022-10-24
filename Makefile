install:
	pip install .


reinstall:
	pip uninstall -y search_data_explorer
	rm -fr build dist search_data_explorer.egg-info
	python setup.py bdist_wheel
	pip install dist/*
