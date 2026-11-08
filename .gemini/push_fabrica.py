import subprocess
import os

os.environ["GH_CONFIG_DIR"] = os.path.expanduser("~/.config/gh-multfacil")

# Get token
token_res = subprocess.run(["gh", "auth", "token", "--hostname", "github.com"], capture_output=True, text=True)
token = token_res.stdout.strip()

clone_dir = os.path.expanduser("~/.gemini/tmp/fabrica-clone")
os.chdir(clone_dir)

remote_url = f"https://{token}@github.com/Djalma0multfacil/fabrica-de-software.git"
subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)
push_res = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print("Push stdout:", push_res.stdout)
print("Push stderr:", push_res.stderr)
print("Push returncode:", push_res.returncode)
