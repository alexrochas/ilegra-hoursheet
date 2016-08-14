import unittest
from collections import OrderedDict

import tabulate

from lancamento_horas import export


class TestExport(unittest.TestCase):

    def test_should_beautify_csv_input(self):
        given_input = [OrderedDict(
            data="08/08/1988",
            hora_inicio="08:30",
            hora_fim="12:30",
            projeto="1981",
            sub_projeto="SELECIONE...",
            grupo="",
            descricao="Descricao aleatoria",
            tipo_atividade="20"
        )]
        output = export.beautify(given_input)
        self.assertEqual(output, tabulate.tabulate(given_input, headers="keys", tablefmt="fancy_grid"))
