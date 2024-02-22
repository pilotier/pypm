import subprocess
import time
import tempfile

cmd = "python test1.py"


outstream = tempfile.TemporaryFile()
errstream = tempfile.TemporaryFile()

def get_stdout(o):
    o.flush()
    o.seek(0)
    r = o.read()
    o.truncate(0)
    return r

process = subprocess.Popen(cmd, shell=True,
                           stdout=outstream)

# wait for the process to terminate
# out, err = process.communicate()
errcode = process.returncode
for i in range(20):
    time.sleep(1)
    print(i, get_stdout(outstream), get_stdout(errstream))
print(errcode)