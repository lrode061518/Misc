# !/usr/bin

echo "rdr pass inet proto tcp from any to any port 80 -> 192.168.64.4 port 80" | sudo pfctl -ef -
# sudo pfctl -F all -f /etc/pf.conf
