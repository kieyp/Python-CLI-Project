# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from original import Base, Factory, Manager, Employee, Shift
# import ipdb

# # Create an SQLAlchemy engine to interact with the database
# engine = create_engine('sqlite:///factory_data.db')

# # Create all tables in the engine
# Base.metadata.create_all(engine)

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Load the models and the session into IPython debugger
# ipdb.set_trace()
