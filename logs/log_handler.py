# This file is responsible for saving all the logs in db.
from logs.config import DJANGO_DB_LOGGER_ENABLE_FORMATTER
import logging
db_default_formatter = logging.Formatter()


class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        from .models import LogTable
        from . import serializers
        trace = None
        if record.exc_info:
            trace = db_default_formatter.formatException(record.exc_info)

        if DJANGO_DB_LOGGER_ENABLE_FORMATTER:
            msg = self.format(record)
        else:
            msg = record.getMessage()
        kwargs = {
            'log_type': record.levelno,
            'log_error_Message': msg,
        }
        serialized_obj = serializers.GetLogsSerializer(data=kwargs)
        if serialized_obj.is_valid():
            serialized_obj.save()
        else:
            print(serialized_obj.errors)

    def format(self, record):
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = db_default_formatter

        if type(fmt) == logging.Formatter:
            record.message = record.getMessage()

            if fmt.usesTime():
                record.asctime = fmt.formatTime(record, fmt.datefmt)

            # ignore exception traceback and stack info

            return fmt.formatMessage(record)
        else:
            return fmt.format(record)
