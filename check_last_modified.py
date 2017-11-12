import os
import time
filename = "/var/log/messages"
modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filename)))
print(modified)