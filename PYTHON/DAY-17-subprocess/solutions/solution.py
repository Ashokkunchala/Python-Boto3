# Reference solution — attempt the exercise first.
import subprocess
r=subprocess.run(['python','--version'], capture_output=True, text=True)
print(r.returncode, r.stdout or r.stderr)

