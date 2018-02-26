import unittest
import mock
import world_manager
import storage_service

class WorldManagerTester(unittest.TestCase):

    @mock.patch('storage_service.StorageService')
    def test_retrieve_world_data(self, mock_s3):
        reference = world_manager.WorldManager(mock_s3)

        mock_s3.get_area.return_value = "11111\n11011\n10001\n11011\n11111"
        reference.get_area("middle_earth", "tavern")
        mock_s3.get_area.assert_called()

if __name__ == '__main__':
    unittest.main()