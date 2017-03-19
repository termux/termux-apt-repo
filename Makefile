install:
	cp termux-apt-repo $(PREFIX)/bin/termux-apt-repo

pypi:
	rm -Rf dist/ build/ termux_apt_repo.egg-info/
	python3 setup.py sdist bdist_wheel egg_info
	twine upload dist/*

.PHONY: install pypi
