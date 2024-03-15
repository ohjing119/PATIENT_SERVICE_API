import json
import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

class SessionMaker(object):

    # singleton pattern
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SessionMaker, cls).__new__(cls)
        return cls.instance

    def get_db_credential(self):
        # Opening JSON file
        db_secret = open('.dbsecret.json')
        #print("HERE")
        return json.load(db_secret)
        #return ""
 
    def get_db_connection_string(self):
        """Get Db Connection String
        Returns:
            str: connection string
        """
        db_secret = self.get_db_credential()
        """
        db_username = db_secret["username"]
        db_password = db_secret["password"]
        db_database_name = db_secret["dbname"]
        db_host_name = db_secret["host"]
        db_port = int(db_secret["port"])
        connection_string = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host_name}:{db_port}/{db_database_name}"

        return connection_string
        """
        return "conn"

    def get_session_maker(self, existing_connection=None):
        if existing_connection is not None:
            engine = existing_connection
        else:
            # stored credentials contains secure string that is stored in secrets manager
            db_secret = self.get_db_credential()
            db_username = db_secret["username"]
            db_password = db_secret["password"]
            db_database_name = db_secret["dbname"]
            db_host_name = db_secret["host"]
            db_port = int(db_secret["port"])
            print(db_secret)

            engine = db.create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host_name}:{db_port}/{db_database_name}")

        # create a configured "Session" class
        Session = sessionmaker(bind=engine)
        return Session