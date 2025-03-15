"""Added portfolio model with categories"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = "7a560d834582"
down_revision = "3e30a663dd4f"
branch_labels = None
depends_on = None

def upgrade():
    # Use batch mode to modify constraints
    with op.batch_alter_table("portfolio", schema=None) as batch_op:
        batch_op.add_column(sa.Column("category_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key("fk_portfolio_category", "category", ["category_id"], ["id"])

def downgrade():
    with op.batch_alter_table("portfolio", schema=None) as batch_op:
        batch_op.drop_constraint("fk_portfolio_category", type_="foreignkey")
        batch_op.drop_column("category_id")
