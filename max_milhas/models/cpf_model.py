import datetime
from commons.sql_class import SQLMaxMilhas
from commons.cpf_validator import CPFValidator

class CPFModel():
    table = "Cpfs"

    def __init__(self, cpf: str, isblacklisted: bool, created_at: datetime.datetime = None):
        if CPFValidator.is_valid(cpf):
            self.cpf = cpf
        else:
            raise ValueError
        self.isblacklisted = isblacklisted
        self.created_at = created_at

    def __str__(self):
        if self.created_at:
            return "CPF: {}, BL: {}, Created_at: {}".format(self.cpf,
                                                            self.isblacklisted,
                                                            self.created_at)
        else:
            return "CPF: {}, BL: {}".format(self.cpf, self.isblacklisted)

    @classmethod
    def count(cls):
        """
        Returns the number of blacklisted cpfs
        """
        query = "SELECT count(*) from {} WHERE is_black_listed=true".format(CPFModel.table)
        return SQLMaxMilhas.fetch_one(query)[0]

    def get_dict(self):
        """
        Transforms a CPF object into a JSON
        """
        attr = {
            "cpf" : self.cpf,
            "is_black_listed" : self.isblacklisted
        }
        if self.created_at:
            attr["created_at"] = str(self.created_at)
        return attr

    def save_cpf(self):
        """
        Saves a CPF into the DB
        """
        query = \
            """
            INSERT INTO {}
                (cpf, is_black_listed)
            VALUES
                ("{}", {})
            ON DUPLICATE KEY UPDATE
                is_black_listed = VALUES(is_black_listed),
                created_at = VALUES(created_at)
            """.format(CPFModel.table, self.cpf, self.isblacklisted)
        return SQLMaxMilhas.commit_query(query)

    @staticmethod
    def get(private_key: str = None, fields: str = "*"):
        """
        Fetchs a CPF from the DB
        """
        if private_key is None:
            query = "SELECT {} FROM {}".format(fields, CPFModel.table)
        else:
            query = "SELECT {} FROM {} WHERE cpf='{}'".format(fields, CPFModel.table, private_key)

        data = SQLMaxMilhas.fetch_all(query)
        returned_data = []
        for i in data:
            try:
                cpf_resp = CPFModel(i[0], i[1], i[2]).get_dict()
                returned_data.append(cpf_resp)
            except ValueError:
                print("malformed cpf")
        return returned_data

    @staticmethod
    def delete_cpf(private_key: str):
        """
        Deletes a CPF from the DB
        """
        query = "DELETE FROM {} WHERE cpf='{}'".format(CPFModel.table, private_key)
        return SQLMaxMilhas.commit_query(query)
