import unittest
from doi_importer import convert_doi

class TestDoi(unittest.TestCase):
    def test_invalid_doi_link_raises_error(self):
        doi_link = "https://unicafe.fi/"
        self.assertRaises(Exception, convert_doi, doi_link)
        
        doi_link = "https://doi.org/10.asdfasdf/sadfasdf"
        self.assertRaises(Exception, convert_doi, doi_link)
        
        doi_link = "https://doi.org/10.1145/367473"
        self.assertRaises(Exception, convert_doi(doi_link))
        
    def test_article_doi_is_converted_to_article_reference(self):
        doi_link = "https://doi.org/10.1145/3651278"
        converted = convert_doi(doi_link)
        self.assertEqual("article", converted[0])
        
        doi_link = "https://doi.org/10.1145/3674735"
        converted = convert_doi(doi_link)
        self.assertEqual("article", converted[0])