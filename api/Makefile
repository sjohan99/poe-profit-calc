.PHONY: run-local run-ninja test

run-local:
	cd poe_profit_calc && export POE_RUN_MODE=local && fastapi dev main.py

run-prod:
	cd poe_profit_calc && export POE_RUN_MODE=ninja && fastapi dev main.py

test:
	poetry run pytest