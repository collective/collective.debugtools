# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory
from collective.debugtools import constants
import logging
import os


_ = MessageFactory('collective.debugtools')
logger = logging.getLogger(__name__)

def is_true_value(val):
    result = False
    true_values = ['1', 'true', 'y']
    if val and val.lower() in true_values:
        result = True
    return result


debugpy_enabled = os.getenv(constants.DEBUGPY_ENABLED, None)
if is_true_value(debugpy_enabled):
    logger.info("*"*16)
    logger.info("Debugpy enabled.")
    logger.info("*"*16)
    import debugpy
    host = os.getenv(constants.DEBUGPY_HOST, "localhost")
    port = os.getenv(constants.DEBUGPY_PORT, "5678")

    try:
        port = int(port)
    except ValueError:
        port = 5678

    logger.info(f"Listening on {host}:{port}")
    debugpy.listen((host, port))

    wait_for_client = os.getenv(constants.DEBUGPY_WAIT_FOR_CLIENT, False)
    if is_true_value(wait_for_client):
        logger.info("Waiting for client to connect...")
        debugpy.wait_for_client()