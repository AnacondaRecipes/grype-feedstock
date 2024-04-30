import os
import json
import shutil
import subprocess

# the path to the executable
grype_path: str = os.environ.get("PKG_NAME", "")
# the version of the executable
grype_version: str = os.environ.get("PKG_VERSION", "")

assert grype_path
assert grype_version

if not shutil.which(grype_path):
    raise Exception(f'The executable was not found at: {grype_path}')

process = subprocess.run(
    args=[grype_path, "version", "--output", "json"],
    capture_output=True)
data = json.loads(process.stdout)

# print output
print("Version:", data)

# check version
assert "version" in data
assert data["version"]
assert data["version"] == grype_version
# check name
assert "application" in data
assert data["application"]
assert data["application"] == grype_path

print("Found:", data["application"], data["version"])
