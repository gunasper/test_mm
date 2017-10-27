class SQLMaxMilhas():
    """
    SQL Singleton Interface created to comunicate with MySQLDB.
    We create this higher level interface in order to allow us to change our engine
    in future if we find this necessary to improve scalability or something else
    """
    __engine = None
    def __init__(self, sql_engine):
        if SQLMaxMilhas.__engine is None:
            SQLMaxMilhas.__engine = sql_engine

    @staticmethod
    def fetch_all(query):
        """
        Fetches a list of resources
        """
        cursor = SQLMaxMilhas.__engine.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    @staticmethod
    def fetch_one(query):
        """
        Fetches a single resource
        """
        cursor = SQLMaxMilhas.__engine.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        return data

    @staticmethod
    def commit_query(query):
        """
        Executes a query that demands a commit
        """
        try:
            cursor = SQLMaxMilhas.__engine.cursor()
            cursor.execute(query)
            SQLMaxMilhas.__engine.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def is_working():
        """
        TODO: melhorar isso
        """
        if SQLMaxMilhas.__engine:
            return True
        else:
            return False
