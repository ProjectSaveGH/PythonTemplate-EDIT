# TCPYLib

The `TCPYLib` module is a collection of utilities and functions designed to support various tasks in the project. Below is an overview of the submodules and their functionalities.

## Submodules

### `lib.cli`

- **arguments.py**
  - `add_arg(parser: ArgumentParser, name: str, help_text: str, default: str | None = None, action: str | None = None, required: bool = False) -> None`
  - `parse_args(parser: ArgumentParser) -> dict[str, str]`
- **shell.py**
  - `clear_console()`
  - `run_command(cmd)`

### `lib.config`

- **config.json**
  - Configuration file containing logging settings and paths.
- **loader.py**
  - `load_config() -> dict`
  - `CONFIG: dict`

### `lib.core`

- **parser.py**
  - `parse_custom_time(time_str: str)`
- **time.py**
  - `get_timestamp()`
  - `format_date(date: datetime, fmt: str = "%Y-%m-%d %H:%M:%S")`

### `lib.logger`

- **logger.py**
  - `Logger`
    - `debug(self, msg: str) -> None`
    - `info(self, msg: str) -> None`
    - `warn(self, msg: str) -> None`
    - `error(self, msg: str) -> None`
    - `critical(self, msg: str, exit: bool = False, exit_code: int = 0) -> None`

### `lib.math`

- **advanced.py**
  - `clamp(value, min_value, max_value)`
- **random.py**
  - `random_string(length=10)`

### `lib.network`

- **ip.py**
  - `get_ip()`
  - `ping(host: str)`

### `lib.screens`

- **download.py**
  - `run_download_screen(...)`
- **error.py**
  - `run_error_screen(...)`
- **info.py**
  - `run_info_screen(...)`
- **warn.py**
  - `run_warn_screen(...)`

### `lib.startup`

- **functions.py**
  - `clean_pycaches(root_dir, show: bool = False)`
  - `check_environment()`
  - `backup_config()`
  - `pre_tasks()`
  - `log_performance(execution_time)`
  - `cleanup_resources()`
  - `post_tasks(execution_time)`

### `lib.utils`

- **file_ops.py**
  - `create_folder(path)`
  - `delete_folder(path)`
  - `read_file(file_path)`
  - `write_file(file_path, content)`
  - `append_file(file_path, content)`
  - `delete_file(file_path)`
- **passwords.py**
  - `input_pwsd(prompt: str, mask: str = "*") -> str`
  - `hash_password(password: str, salt: str = "") -> str`
  - `generate_password(length: int = 12, use_digits: bool = True, use_special: bool = True) -> str`
  - `strong_password_check(password: str, min_length: int = 8) -> bool`
- **decorators.py**
  - `deactive(reason="Diese Funktion ist deaktiviert.")`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.