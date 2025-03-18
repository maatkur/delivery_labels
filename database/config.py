from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database.base import Base  # Importando o Base correto
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# URL do banco de dados (no caso, SQLite)
# DATABASE_URL = r"sqlite:///C:/Users/mathe/PycharmProjects/delivery_labels/delivery_labels.db"
DATABASE_URL = r"sqlite:///C:/Users/mathe/desktop/delivery_labels.db"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_session():
    """Context manager para a sessão do banco de dados."""
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()  # Se ocorrer um erro, faz rollback
        raise e
    finally:
        session.close()


class RepositoryConfig:
    def __init__(self, table_name):
        self.table_name = table_name

    def execute_and_commit(self, instance):
        """
        Adiciona um objeto ao banco de dados e faz commit.
        """
        try:
            with get_session() as session:
                session.add(instance)  # Adiciona a instância
                print(instance)
                session.commit()  # Realiza o commit
        except SQLAlchemyError as e:
            print(f"Erro ao inserir dados: {e}")
            raise

    def search(self, model, query):
        """
        Realiza uma busca no banco de dados e retorna os resultados.
        """
        try:
            with get_session() as session:
                result = session.query(model).filter_by(**query).all()  # Filtra os dados
                return result
        except SQLAlchemyError as e:
            print(f"Erro ao buscar dados: {e}")
            return []

    def select(self, model, filters=None, order_by=None, limit=None, offset=None):
        """
        Seleciona dados a partir de um modelo e opções passadas.
        """
        try:
            with get_session() as session:
                query = session.query(model)

                if filters:
                    query = query.filter_by(**filters)  # Aplica filtros

                if order_by:
                    query = query.order_by(order_by)  # Aplica ordenação

                if limit:
                    query = query.limit(limit)  # Aplica limite de resultados

                if offset:
                    query = query.offset(offset)  # Aplica offset

                return query.all()
        except SQLAlchemyError as e:
            print(f"Erro ao selecionar dados: {e}")
            return []

    def update(self, model, filters, update_data):
        """
        Atualiza os dados com base nos filtros passados.
        """
        try:
            with get_session() as session:
                # Realiza a busca do objeto
                obj = session.query(model).filter_by(**filters).first()
                if obj:
                    for key, value in update_data.items():
                        setattr(obj, key, value)  # Atualiza os atributos
                    session.commit()
                    return obj
                else:
                    return None
        except SQLAlchemyError as e:
            print(f"Erro ao atualizar dados: {e}")
            session.rollback()
            return None

    def delete(self, model, filters):
        """
        Deleta dados com base nos filtros passados.
        """
        try:
            with get_session() as session:
                obj = session.query(model).filter_by(**filters).first()
                if obj:
                    session.delete(obj)
                    session.commit()
                    return True
                else:
                    return False
        except SQLAlchemyError as e:
            print(f"Erro ao deletar dados: {e}")
            session.rollback()
            return False
