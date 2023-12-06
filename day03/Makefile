.PHONY: ex00 ex01 ex02

PY = python3

ex00:
	cd $@ && $(PY) exploit.py

# ex01:
# 'make cons' in first terninal
# 'make prod' in second terninal
cons:
	$(PY) ./ex01/consumer.py -e 2222222222,4444444444

prod:
	$(PY) ./ex01/producer.py --mode 0


get_packs:	
	pip install -r requirements.txt

style:
	$(PY) -m pycodestyle .
	@echo "\033[32mstyle test passed successfully\033[0m"

tost:
	$(PY) -m black .

