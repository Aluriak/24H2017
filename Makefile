


init_lumio:
	socat /dev/ttyUSB0,b230400,raw -

t: test
test:
	pytest . --ignore=venv -v
