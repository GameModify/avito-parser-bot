from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_init'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'search_queries',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('query', sa.Text(), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )

    op.create_table(
        'ads',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('ad_id', sa.String(length=64), nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('url', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('search_query_id', sa.Integer(), sa.ForeignKey('search_queries.id'), nullable=True),
        sa.UniqueConstraint('ad_id', name='uq_ads_ad_id'),
    )


def downgrade() -> None:
    op.drop_table('ads')
    op.drop_table('search_queries')


