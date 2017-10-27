
from commons.cpf_validator import CPFValidator
from commons.errors import INVALID_CPF, RESOURCE_NOT_FOUND,\
                           DATABASE_ERROR, MISSING_PARAMETER, INVALID_PARAMETER
from models.cpf_model import CPFModel
from .base import BaseHandler

class CPFsHandler(BaseHandler):
    """
    CRUD CPFs
    """
    async def get(self, cpf: str = ''):
        """
        Get one or more CPFs
        """
        if cpf:
            if CPFValidator.is_valid(cpf):
                data = CPFModel.get(cpf)
            else:
                self.write_error(INVALID_CPF)
                return
        else:
            data = CPFModel.get()

        response = {}
        if cpf:
            if data:
                response["cpf"] = data
            else:
                self.write_error(RESOURCE_NOT_FOUND)
                return
        else:
            response["cpfs"] = data
        self.write(response)


    async def post(self, cpf: str = ''):
        """
        Creates a CPFs
        """
        if cpf:
            self.write_error(INVALID_PARAMETER)
            return

        requested_keys = ["cpf", "is_black_listed"]
        data = self.get_data(req_keys=requested_keys, acc_keys=requested_keys)
        if data:
            try:
                cpf = CPFModel(data["cpf"], data["is_black_listed"])
                if cpf.save_cpf():
                    self.set_status(201)
                else:
                    self.write_error(DATABASE_ERROR)
            except ValueError:
                self.write_error(INVALID_CPF)


    async def put(self, cpf: str = ''):
        """
        Edits a CPF
        """
        if cpf == '':
            self.write_error(MISSING_PARAMETER("cpf"))
            return

        accepted_keys = ["is_black_listed"]
        data = self.get_data(acc_keys=accepted_keys)
        if data:
            try:
                cpf = CPFModel(cpf, data["is_black_listed"])
                if cpf.save_cpf():
                    self.set_status(201)
                else:
                    self.write_error(DATABASE_ERROR)
            except ValueError:
                self.write_error(INVALID_CPF)


    async def delete(self, cpf: str = ''):
        """
        Deletes a CPF
        """
        if cpf == '':
            self.write_error(MISSING_PARAMETER("cpf"))
            return

        CPFModel.delete_cpf(cpf)
