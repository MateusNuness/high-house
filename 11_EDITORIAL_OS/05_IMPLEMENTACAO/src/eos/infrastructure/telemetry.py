"""
Telemetry and Logging for EOS.
Uses structlog for structured JSON logging.
"""
import structlog
import logging
import sys

def setup_logging(level: str = "INFO"):
    """
    Configures structured logging for the multi-agent system.
    Outputs JSON logs that can be ingested by observability tools.
    """
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # Configure standard python logging to pipe to structlog
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, level.upper(), logging.INFO)
    )

def get_logger(name: str):
    """Returns a structlog logger instance."""
    return structlog.get_logger(name)
