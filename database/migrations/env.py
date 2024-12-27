from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from database.base import Base  # Importando o Base corretamente
from database.models import User, Permission, users_permissions  # Importando as models

# Configuração do Alembic
config = context.config

# Configuração de log
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Apontar para o metadata das suas classes
target_metadata = Base.metadata  # Usando Base.metadata agora


def run_migrations_offline() -> None:
    """Execução em modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Execução em modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
