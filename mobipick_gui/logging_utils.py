"""Shared logging helpers for the Mobipick GUI stack."""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

_LOGGER_ROOT = "mobipick"


class _DebugFormatter(logging.Formatter):
    """Formatter that renders debug lines in dark green."""

    _GREEN = "\x1b[32m"
    _RESET = "\x1b[0m"

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401 - inherited docstring
        message = super().format(record)
        if record.levelno <= logging.DEBUG:
            return f"{self._GREEN}{message}{self._RESET}"
        return message


def configure_logging(debug: bool, *, log_file: Optional[Path] = None) -> Optional[Path]:
    """Configure the shared logger.

    When *debug* is true a stream handler and file handler are registered.
    Debug output is printed in dark green and persisted to *log_file* (or a
    default file in the current working directory). When *debug* is false a
    ``NullHandler`` is installed so modules can log safely without producing
    terminal noise.
    """

    logger = logging.getLogger(_LOGGER_ROOT)
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    if not debug:
        logger.addHandler(logging.NullHandler())
        return None

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = _DebugFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file is None:
        log_file = Path.cwd() / "mobipick_debug.log"
    else:
        log_file = Path(log_file)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    )
    logger.addHandler(file_handler)

    logger.debug("Debug logging enabled; writing to %s", log_file)
    return log_file


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a module-scoped logger under the shared root."""

    if name:
        return logging.getLogger(f"{_LOGGER_ROOT}.{name}")
    return logging.getLogger(_LOGGER_ROOT)


__all__ = ["configure_logging", "get_logger"]
