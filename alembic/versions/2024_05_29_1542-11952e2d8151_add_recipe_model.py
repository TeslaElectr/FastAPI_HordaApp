"""add Recipe model

Revision ID: 11952e2d8151
Revises: 163475ec7c79
Create Date: 2024-05-29 15:42:29.889397

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "11952e2d8151"
down_revision: Union[str, None] = "163475ec7c79"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "recipes",
        sa.Column("recipe", sa.JSON(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "products", sa.Column("recipe_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key("products_recipe_id_fkey", "products", "recipes", ["recipe_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("products_recipe_id_fkey", "products", type_="foreignkey")
    op.drop_column("products", "recipe_id")
    op.drop_table("recipes")
    # ### end Alembic commands ###
