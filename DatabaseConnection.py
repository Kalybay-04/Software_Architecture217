import json
import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)

        self.hostname = config['hostname']
        self.username = config['username']
        self.password = config['password']
        self.database_name = config['database_name']

        print("Database connection established with the following parameters:")
        print("Hostname:", self.hostname)
        print("Username:", self.username)
        print("Database Name:", self.database_name)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls()
        return cls._instance

    def execute_query(self, sql):
        pass

    def get_connection_info(self):
        return {
            'hostname': self.hostname,
            'username': self.username,
            'database_name': self.database_name
        }


db_instance = DatabaseConnection.get_instance()
connection_info = db_instance.get_connection_info()
print("Connection info:", connection_info)
