import os

from dotenv import load_dotenv


def load_config(app_env):
    # app_env = os.environ.get("APP_ENV", "dev")
    if app_env == "dev":
        load_dotenv("development.env")
    elif app_env == "prod":
        load_dotenv(".env")
    else:
        raise EnvironmentError(f"Unknown environment: {app_env}")


if __name__ == "__main__":
    try:
        load_config()
    except EnvironmentError as e:
        print(f"Error during configuration: {e}")
