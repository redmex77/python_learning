import os
process_name = "rsyslogd"
tmp = os.popen("ps -Af").read()
if process_name not in tmp:
    print(process_name + " not running")
else:
    print(process_name + " running")