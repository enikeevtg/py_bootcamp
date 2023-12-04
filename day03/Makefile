.PHONY: ex00 ex01 ex02

PY = python3

ex00:
	cd $@ && python3 exploit.py



get_packs:	
	pip install -r requirements.txt

style:
	$(PY) -m pycodestyle .
	@echo "\033[32mstyle test passed successfully\033[0m"

tost:
	$(PY) -m black .

