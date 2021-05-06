install:
	pip install .


reinstall:
	pip uninstall -y tabular_data_explorer
	rm -fr build dist tabular_data_explorer.egg-info
	python setup.py bdist_wheel
	pip install dist/*
