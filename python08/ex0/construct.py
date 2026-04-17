from os.path import basename
import site
import sys

success = '''
SUCCESS: You're in an isolated environment!")
Safe to install packages without affecting")
the global system.")
'''

warn = '''
WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows

Then run this program again.'''


def main() -> None:
    if sys.base_prefix == sys.prefix:
        print("\nMATRIX STATUS: You're still plugged in")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print(warn)
    else:
        print("\nMATRIX STATUS: Welcome to the construct")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment:", basename(sys.prefix))
        print("Environment Path:", sys.prefix)
        print()
        print(success)
        print("Package installation path:")
        print(site.getusersitepackages())


if __name__ == "__main__":
    main()
