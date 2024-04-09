from sys import argv, platform
import subprocess

from esp_pwsh_check.pwsh_checker import checker

# Get the file paths from command-line arguments
file_paths = argv[1:]

def main() -> None:
	# Test PowerShell installation
	try:
		if platform == 'win32':
			subprocess.call(["powershell"])
		else:
			subprocess.call(["pwsh"])
	except FileNotFoundError:
		raise SystemError("[ERROR] For checking PowerShell scripts the PowerShell has to be installed.")

	# Run PowerShell script checker
	if platform == 'win32':
		process = subprocess.run(["pwsh", "-Command", checker(file_paths)], stdout=subprocess.PIPE , stderr=subprocess.PIPE)
		if process.stderr:
			print(f'stderr - {(process.stderr).decode("utf-8")}')
	else:
		process = subprocess.run(["pwsh", "-Command", checker(file_paths)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	if process.returncode != 0:
		print((process.stdout).decode('utf-8'))
		raise SystemError("[ERROR] PowerShell Script error")


if __name__ == '__main__':
    main()
