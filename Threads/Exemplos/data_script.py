import os
import subprocess

def run_encrypt(data):
    env = os.environ.copy()
    env["password"] = "zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1"
    proc = subprocess.Popen(
        ["openssl", "enc", "-des3", "-pass", "env:password"],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)
    
for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])