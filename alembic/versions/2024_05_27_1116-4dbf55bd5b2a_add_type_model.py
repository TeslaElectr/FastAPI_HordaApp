"""add Type model

Revision ID: 4dbf55bd5b2a
Revises: 4c65d6b983d0
Create Date: 2024-05-27 11:16:02.330192

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4dbf55bd5b2a"
down_revision: Union[str, None] = "4c65d6b983d0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "types",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("description"),
        sa.UniqueConstraint("name"),
    )
    op.add_column(
        "products", sa.Column("type_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key("products_type_id_fkey", "products", "types", ["type_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("products_type_id_fkey", "products", type_="foreignkey")
    op.drop_column("products", "type_id")
    op.drop_table("types")
    # ### end Alembic commands ###
