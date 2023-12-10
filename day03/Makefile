.PHONY: ex00 ex01 ex02

RM = rm -rf
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

ex02: clean
	cd $@ && $(PY) gen_ansible.py

get_packs:
	pip install -r requirements.txt

style:
	$(PY) -m pycodestyle .
	@echo "\033[32mstyle test passed successfully\033[0m"

# tost:
# 	$(PY) -m black .

clean:
	$(RM) ex02/common.py
	$(RM) ex02/consumer.py
	$(RM) ex02/deploy.yml
	$(RM) ex02/exploit.py
	$(RM) ex02/script.html
	$(RM) ../materials/evilcorp_hacked.html
