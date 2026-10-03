import os


def resolve_env_value(value):
    if not value.startswith("@env:"):
        return value

    name = value.removeprefix("@env:")
    env_value = os.environ.get(name)
    if not env_value:
        raise RuntimeError(
            f"Set {name} in your local .env file before running this scenario."
        )
    return env_value
