.PHONY: ex00 ex01 ex02

PY = python3

ex00:
	@cat $@/data_hashes_10lines.txt | $(PY) $@/blocks.py 10

ex01:
	@python3 $@/decypher.py "Have you delivered eggplant pizza at restored keep?"
	@python3 $@/decypher.py "Zebra especially first teacher your really strength tiger"

ex02:
	@python3 $@/mfinder.py $@/m_true.txt

style:
	python3 -m pycodestyle .
	@echo "\033[32mstyle test passed successfully\033[0m"

tost:
	python3 -m black .
