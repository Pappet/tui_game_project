"""
logger.py

Provides a shared logging utility for the application.
"""

import logging
import sys

def setup_logger() -> logging.Logger:
    """
    Configures and returns a root logger for the application.
    """
    
    # This setup is basic. For Textual, logging to a file
    # or the Textual dev console is often preferred over stdout.
    
    logger = logging.getLogger("tui_game")
    logger.setLevel(logging.DEBUG) # Set to DEBUG for development
    
    # Avoid adding duplicate handlers if called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    logger.info("Logger configured (stub).")
    return logger

# Initialize a default logger for easy import
log = setup_logger()