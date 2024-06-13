"""empty message

Revision ID: 1191c16836a7
Revises: 
Create Date: 2024-05-28 08:33:44.417446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1191c16836a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_envio', sa.DateTime(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('assunto', sa.String(), nullable=True),
    sa.Column('mensagem', sa.String(), nullable=True),
    sa.Column('respondido', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('sobrenome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=True),
    sa.Column('mensagem', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_comentarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_criação', sa.DateTime(), nullable=True),
    sa.Column('comentario', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_comentarios')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('contato')
    # ### end Alembic commands ###
