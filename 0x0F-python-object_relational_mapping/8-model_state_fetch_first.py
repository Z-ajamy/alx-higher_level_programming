#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Sess = sessionmaker(bind=engine)
    s = Sess()

    row1 = s.query(State).order_by(State.id).first()
    s.close()
    if row1:
        print('{}: {}'.format(row1.id, row1.name))
    else:
        print("Nothing")
