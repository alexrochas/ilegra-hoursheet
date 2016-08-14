import os
import unittest

from lancamento_horas import parser

CSV_FILE = os.path.join(os.path.dirname(__file__), '../fixtures/to_import_file.csv')


class TestParser(unittest.TestCase):
    def test_should_parse_csv_file(self):
        expected_file = dict(
            data="08/08/1988",
            hora_inicio="08:30",
            hora_fim="12:30",
            projeto="1981",
            sub_projeto="SELECIONE...",
            grupo="",
            descricao="Descricao aleatoria",
            tipo_atividade="20"
        )
        with open(CSV_FILE) as file:
            parsed_file = parser.parse_csv(file)
        self.assertEqual(parsed_file, [expected_file])
