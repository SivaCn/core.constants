# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
__import__('pkg_resources').declare_namespace(__name__)

import logging
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #


__all__ = [
    # All public symbols go here.
]


AMQP_CONNECTION_STRING = 'amqp://%(username)s:%(password)s@%(host)s:%(port)s'

# ------------------- START: File Logger ------------------ #
LOG_FORMAT = '[%(asctime)s]: %(levelname)s: %(message)s'

central_logger_settings = {
    'LOG_FILE_NAME': 'central_logger.log',
    'LOG_FILE_MAX_BYTES': 1024 * 512,
    'LOG_FILE_BACKUP_COUNT': 5,
    'LOG_LEVEL': logging.INFO,
}
# -------------------- END: File Logger ------------------- #
