"""increase_services_and_details_name_length

Revision ID: b4fdd3ee0593
Revises: 7c516b786eee
Create Date: 2026-10-14 22:02:51.032811

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b4fdd3ee0593"
down_revision: Union[str, Sequence[str], None] = "7c516b786eee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "details",
        "name_detail",
        existing_type=sa.VARCHAR(length=40),
        type_=sa.String(length=100),
        existing_nullable=False,
    )
    op.alter_column(
        "services",
        "name_service",
        existing_type=sa.VARCHAR(length=30),
        type_=sa.String(length=100),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "services",
        "name_service",
        existing_type=sa.String(length=100),
        type_=sa.VARCHAR(length=30),
        existing_nullable=False,
    )
    op.alter_column(
        "details",
        "name_detail",
        existing_type=sa.String(length=100),
        type_=sa.VARCHAR(length=40),
        existing_nullable=False,
    )
