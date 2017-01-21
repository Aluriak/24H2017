


init_lumio:
	socat /dev/ttyUSB0,b230400,raw -

t: test
test:
	pytest . --ignore=venv -v

init_tty:
	stty -F /dev/ttyUSB0 -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke