from app.api_cep import _get_somente_numeros, ApiCep
from unittest import TestCase
from unittest.mock import patch, Mock


class TestApiCep(TestCase):
    @patch('app.api_cep.re.sub', return_value='1345')
    def test__get_somente_numeros(self, mock_sub):
        dados = '1As3@45'

        resultado = _get_somente_numeros(dados)

        mock_sub.assert_called_once_with('[^0-9]', '', dados)
        self.assertEqual(resultado, '1345')

    @patch('app.api_cep.requests.get')
    @patch('app.api_cep._get_somente_numeros', return_value='20241250')
    def test_ApiCep(self, mock_get_somente_numeros, mock_requests_get):
        cep = '20241-250'
        json_return = {'cep': '20241-250', 'logradouro': 'Rua Santa Cristina', 'complemento': '',
                       'bairro': 'Santa Teresa', 'localidade': 'Rio de Janeiro', 'uf': 'RJ', 'unidade': '',
                       'ibge': '3304557', 'gia': ''}
        link_get = f'http://www.viacep.com.br/ws/20241250/json/'

        api = ApiCep()

        mock_requests_get.return_value = Mock(status_code=200)
        mock_requests_get.return_value.json = Mock(return_value=json_return)

        response = api.execute(cep)

        mock_get_somente_numeros.assert_called_once_with(cep)
        mock_requests_get.assert_called_once_with(link_get)
        mock_requests_get.return_value.json.assert_called_once_with()

        self.assertEqual(mock_requests_get.return_value.status_code, 200)
        self.assertEqual(response, json_return)
