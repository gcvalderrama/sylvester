setup-dev:
	python3 -m venv .venv

install-dev:   
	pip install -r requirements.txt

run-local-case-a:
	locust -f CaseA.py -H http://localhost:3000 --headless --users 5 --spawn-rate 1 --csv case-a --skip-log-setup

run-aws-case-a:
	rm -f case-a*.csv
	locust -f CaseA.py -H ${host} -t 300s  --headless --users 200 --spawn-rate 5 --csv case-a --skip-log-setup
