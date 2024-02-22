import time
import sys


for i in range(3):
    print("looping...")
    print("ERROR ...", file=sys.stderr)
    sys.stdout.flush()
    time.sleep(1)
    