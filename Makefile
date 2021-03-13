install:
	pip install .


reinstall:
	pip uninstall -y optimization_dashboards
	rm -fr build dist optimization_dashboards.egg-info
	python setup.py bdist_wheel
	pip install dist/*
