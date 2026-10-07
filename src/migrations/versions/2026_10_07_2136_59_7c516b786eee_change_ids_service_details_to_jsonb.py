"""change ids_service_details to jsonb

Revision ID: 7c516b786eee
Revises: 99f99130ad3e
Create Date: 2026-10-07 21:36:59.936785

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "7c516b786eee"
down_revision: Union[str, Sequence[str], None] = "99f99130ad3e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "orders",
        "ids_service_details",
        existing_type=sa.VARCHAR(length=100),
        type_=postgresql.JSONB(astext_type=sa.Text()),
        existing_nullable=True,
        postgresql_using="ids_service_details::jsonb"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "orders",
        "ids_service_details",
        existing_type=postgresql.JSONB(astext_type=sa.Text()),
        type_=sa.VARCHAR(length=100),
        existing_nullable=True,
        postgresql_using="ids_service_details::text"
    )
