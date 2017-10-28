import re

class CPFValidator():

    @staticmethod
    def is_valid(tested_cpf):
        """
        Tests wheter a CPF is valid or not.
        :returns True: if CPF is valid;
        :returns False: otherwise
        """
        cpf = ''.join(re.findall('\d', str(tested_cpf)))

        if (not cpf) or (len(cpf) < 11):
            return False

        # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam
        int_values = list(map(int, cpf))
        created_cpf = int_values[:9]
        
        while len(created_cpf) < 11:
            r = sum([(len(created_cpf)+1-i)*v for i,v in enumerate(created_cpf)]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            created_cpf.append(f)

        # Se o número gerado coincidir com o número original, é válido
        if created_cpf == int_values:
            return True
        return False
