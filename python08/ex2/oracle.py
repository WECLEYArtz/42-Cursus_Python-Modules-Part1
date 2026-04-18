import os

override = True
warns: dict[str, bool] = {
        'badconfig': False,
        'hardcode': False
        }
conf_names: dict[str, str | None] = {
        'MATRIX_MODE': None,
        'DATABASE_URL': "Connected to local instance",
        'API_KEY': "Authenticated",
        'LOG_LEVEL': None,
        'ZION_ENDPOINT': "Online",
        }


def load_env_vars() -> None:
    try:
        from dotenv import load_dotenv
        if (not load_dotenv(override=override)):
            print("No configuration loaded, exiting...")
            exit(1)
    except ImportError as e:
        print(e)
        exit(1)


def show_env_vars() -> None:
    from dotenv import dotenv_values

    print("Configuration loaded:")
    for config in conf_names:
        val = os.getenv(config)
        if not val:
            print("Missing config:", config)
            warns['badconfig'] = True
            continue
        print(config, end=': ')
        print(val if not conf_names[config] else conf_names[config])
        if (len(dotenv_values()) != len(conf_names)):
            warns['badconfig'] = True


def check_security() -> None:
    tmp1 = {*globals(), *locals()}
    tmp2 = tmp1.difference({n for n in conf_names})
    complete = True

    if (len(tmp1) != len(tmp2)):
        warns['hardcode'] = True

    if warns['hardcode']:
        print("[KO] Hardcoded detected")
        complete = False
    else:
        print("[OK] No hardcoded secrets detected")

    if warns['badconfig']:
        print("[KO] .env file missing keys or has extra ones")
        complete = False
    else:
        print("[OK] .env file properly configured")

    if not override:
        print("[KO] Production overrides disabled")
        complete = False
    else:
        print("[OK] Production overrides available")

    if not complete:
        exit(1)


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_env_vars()
    show_env_vars()

    print("\nEnvironment security check:")
    check_security()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
