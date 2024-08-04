import logging
import pytest
from app.db import sessionmanager

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@pytest.mark.test_alembic_migrations
def test_alembic_migration():
    logger.debug(f"start test migrations")
    sessionmanager.upgrade_head()
    logger.debug(f"upgrade migrations done")
    sessionmanager.downgrade_base()
    logger.debug(f"migrations done")