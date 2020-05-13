"""empty message

Revision ID: 5692a391377a
Revises: 
Create Date: 2020-05-13 20:09:35.359728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5692a391377a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_recommendations_title', table_name='recommendations')
    op.drop_table('recommendations')
    op.drop_index('ix_sections_letter', table_name='sections')
    op.drop_index('ix_sections_title', table_name='sections')
    op.drop_table('sections')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sections',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('letter', sa.CHAR(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_sections_title', 'sections', ['title'], unique=False)
    op.create_index('ix_sections_letter', 'sections', ['letter'], unique=False)
    op.create_table('recommendations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=128), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.Column('interpretation', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_recommendations_title', 'recommendations', ['title'], unique=False)
    # ### end Alembic commands ###