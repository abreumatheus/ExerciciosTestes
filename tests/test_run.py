from run import consulta_api_viacep, ApiCep
from unittest import TestCase
from unittest.mock import patch


class TestRun(TestCase):

    @patch('run.ApiCep.execute')
    @patch('run.print')
    @patch('run.input')
    def test_consulta_api_viacep(self, mock_input, mock_print, mock_apicep):
        cep = "20241250"
        json = {'cep': '20241-250', 'logradouro': 'Rua Santa Cristina', 'complemento': '',
                'bairro': 'Santa Teresa', 'localidade': 'Rio de Janeiro', 'uf': 'RJ', 'unidade': '',
                'ibge': '3304557', 'gia': ''}

        mock_input.return_value = cep
        mock_print.return_value = json
        mock_apicep.return_value = json

        consulta_api_viacep()

        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        mock_print.assert_called_once_with(json)
        mock_apicep.assert_called_once_with(cep)
