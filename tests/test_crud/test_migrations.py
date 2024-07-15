import pytest
from app.db import sessionmanager

@pytest.mark.test_alembic_migrations
def test_alembic_migration():
    sessionmanager.upgrade_head()
    sessionmanager.downgrade_base()
    