"""Added ContactMessage and AboutMe models

Revision ID: 0a82ceac06b8
Revises: ac15f4b2ff2b
Create Date: 2025-03-15 10:20:00.599965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a82ceac06b8'
down_revision: Union[str, None] = 'ac15f4b2ff2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
