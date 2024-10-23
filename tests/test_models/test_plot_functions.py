import unittest
from unittest.mock import patch, MagicMock
import json
from datetime import datetime
from models.plot_functions import today_date, plot_home_page_charts, plot_servicing_page_charts


class TestPlotFunctions(unittest.TestCase):

    @patch('models.plot_functions.datetime')
    def test_today_date(self, mock_datetime):
        mock_datetime.today.return_value = datetime(2023, 10, 14)
        expected_date = 'Sat, 14 October 2023'

        result = today_date()

        self.assertEqual(result, expected_date)

    @patch('models.projects.ProjectsData.projects_data_to_dict_list')
    def test_plot_home_page_charts(self, mock_projects_data):
        mock_projects_data.return_value = [
            {
                "contract_number": "001",
                "physical_progress_percentage": 50,
                "financial_progress_percentage": 60,
                "year": 2021,
                "project_status": "Completed",
                "project_manager": "Alice",
                "contract_type": "Type A"
            },
            {
                "contract_number": "002",
                "physical_progress_percentage": None,
                "financial_progress_percentage": 70,
                "year": 2022,
                "project_status": "In Progress",
                "project_manager": "Bob",
                "contract_type": "Type B"
            },
            {
                "contract_number": "003",
                "physical_progress_percentage": 80,
                "financial_progress_percentage": 90,
                "year": 2021,
                "project_status": "Stopped",
                "project_manager": "Alice",
                "contract_type": "Type A"
            },
        ]

        graph1JSON, graph2JSON, graph3JSON, graph4JSON, graph5JSON = plot_home_page_charts()

        self.assertIsInstance(graph1JSON, str)
        self.assertIsInstance(graph2JSON, str)
        self.assertIsInstance(graph3JSON, str)
        self.assertIsInstance(graph4JSON, str)
        self.assertIsInstance(graph5JSON, str)

        graph1 = json.loads(graph1JSON)
        self.assertIn('data', graph1)
        self.assertEqual(len(graph1['data']), 1)

    @patch('models.projects.ContractType.contract_type_data_dict')
    def test_plot_servicing_page_charts(self, mock_contract_data):
        mock_contract_data.return_value = [
            {
                "contract_name": "Contract 1",
                "contractor": "Contractor A",
                "link": "http://example.com",
                "water_progress": 20,
                "sewer_progress": 30,
                "roads_progress": 40,
                "storm_drainage_progress": 50,
                "public_lighting_progress": 60,
                "physical_progress_percentage": 70
            },
            {
                "contract_name": "Contract 2",
                "contractor": "Contractor B",
                "link": "http://example.com",
                "water_progress": 10,
                "sewer_progress": 20,
                "roads_progress": 30,
                "storm_drainage_progress": 40,
                "public_lighting_progress": 50,
                "physical_progress_percentage": 60
            }
        ]

        servicing_charts = plot_servicing_page_charts()

        self.assertIsInstance(servicing_charts, list)
        self.assertEqual(len(servicing_charts), 2)

        chart1 = json.loads(servicing_charts[0])
        self.assertIn('data', chart1)

    @patch('models.projects.ContractType.contract_type_data_dict')
    def test_plot_servicing_page_charts_no_data(self, mock_contract_data):
        mock_contract_data.return_value = []

        servicing_charts = plot_servicing_page_charts()

        self.assertEqual(servicing_charts, [])


if __name__ == '__main__':
    unittest.main()
