from sqlmodel import SQLModel, create_engine

# Arquivo SQLite
sqlite_file_name = "MotorHero.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Criar engine
engine = create_engine(sqlite_url, echo=True)

# Cria todas as tabelas definidas nos modelos
SQLModel.metadata.create_all(engine)
