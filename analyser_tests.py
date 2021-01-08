from logging import exception
from os import read
from unittest.case import TestCase
import json, unittest, sys
from user_agents import parse

import application.analysis.views_by_location as vbl
import application.analysis.views_by_browser as vbb
import application.analysis.reader_profiles as rp
import application.analysis.also_likes as al


views_by_location = vbl.views_by_location()
views_by_browser = vbb.views_by_browser()
reader_profiles = rp.reader_profiles()
also_likes = al.also_likes()



# Testing sample data
sample_line_1 = '{"ts": 1393631989,"visitor_uuid": "745409913574d4c6","visitor_username": null,"visitor_source": "external","visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "impression",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause_type": "page" }'
sample_line_2 = '{"ts": 1393631989,    "visitor_uuid": "64bf70296da2f9fd",    "visitor_username": null,    "visitor_source": "internal",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0",    "visitor_ip": "06f49269e749a837",    "visitor_country": "VE",    "visitor_referrer": "64f729926497515c",    "env_type": "reader",    "env_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "env_adid": null,    "event_type": "pagereadtime",    "event_readtime": 797,    "subject_type": "doc",    "subject_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "subject_page": 10,    "cause": null }'
sample_line_invalid = '{"ts": 1393631989,"visitor_uuid": "745409913574d4c6","visitor_username": null,"visitor_source": "external","visitor_device": "browser",     "visitor_ip": "0e1c9cd3d6c22c65",     "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",      "env_adid": null,    "event_type": "impression",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause_type": "page" }'
document_id = '140228202800-6ef39a241f35301a9a42cd0ed21e5fb0'
user_id = '64bf70296da2f9fd'


class test_views_by_location(unittest.TestCase):
  

  def test_get_views_by_location_country_dict_empty(self):
    self.assertEqual(views_by_location.get_country_dict(), {})  

  def test_get_views_by_location_continent_dict_empty(self):
    self.assertEqual(views_by_location.get_continent_dict(), {}) 

  def test_build_country_dict(self):
    self.assertEqual(249,len(views_by_location.views_by_country)) 
    
  def test_build_continent_dict(self):
    self.assertEqual(7,len(views_by_location.views_by_continent)) 
    
  def test_procsess_line_continent(self):
    views_by_location = vbl.views_by_location()
    views_by_location.process_json_line(json.loads(sample_line_1), document_id)
    self.assertEqual(1,views_by_location.views_by_continent['North America']) 
  
  def test_procsess_line_country(self):
    views_by_location = vbl.views_by_location()
    views_by_location.process_json_line(json.loads(sample_line_1), document_id)
    self.assertEqual(1,views_by_location.views_by_country['Mexico'])
    
  def test_get_views_by_location_country_dict(self):
    views_by_location = vbl.views_by_location()
    views_by_location.process_json_line(json.loads(sample_line_1), document_id) 
    self.assertEqual(len(views_by_location.get_country_dict()), 1)  

  def test_get_views_by_location_continent_dict(self):
    views_by_location = vbl.views_by_location()
    views_by_location.process_json_line(json.loads(sample_line_1), document_id)
    self.assertEqual(len(views_by_location.get_continent_dict()), 1) 
  
  def test_procsess_line_key_error(self):
    views_by_location = vbl.views_by_location()
    views_by_location.process_json_line(json.loads(sample_line_invalid), document_id) 
    self.assertRaises(KeyError)
    
 
class test_views_by_browser(unittest.TestCase):
  
  def test_get_browser_verbose_dict_empty(self):
    self.assertEqual(views_by_browser.get_view_by_browser_verbose_dict(), {})  

  def test_get_browser_dict_empty(self):
    self.assertEqual(views_by_browser.get_views_by_browser_dict(), {})
  
  def test_procsess_line_verbose(self):
    views_by_browser = vbb.views_by_browser()
    views_by_browser.process_json_line(json.loads(sample_line_1))
    dictionary = views_by_browser.get_view_by_browser_verbose_dict()
    self.assertEqual(1, len(dictionary))
    
  def test_procsess_line(self):
    views_by_browser = vbb.views_by_browser()
    views_by_browser.process_json_line(json.loads(sample_line_1))
    dictionary = views_by_browser.get_views_by_browser_dict()
    self.assertEqual(1, dictionary["Facebook"])
  
  def test_process_line_key_error(self):
    views_by_browser = vbb.views_by_browser()
    views_by_browser.process_json_line(json.loads(sample_line_1))
    self.assertRaises(KeyError)
  
class test_reader_profiles(unittest.TestCase): 
   
  def test_get_top_ten_readers(self):
    
    custom_dict = {
      1:12,
      2:31,
      3:43,
      4:11,
      5:53,
      6:9,
      7:32,
      8:23,
      9:1,
      10:34,
      11:93,
      12:3,
    }
    
    reader_profiles.reader_profiles = custom_dict
    reader_profiles.top_ten_readers()
    self.assertEqual(10, len(reader_profiles.top_ten_readers()))

  def test_processes_line(self):
    reader_profiles = rp.reader_profiles()
    reader_profiles.process_json_line(json.loads(sample_line_2))
    dictionary = reader_profiles.reader_profiles
    self.assertEqual(797,dictionary[user_id])
    
  def test_processes_line_key_error(self):
    reader_profiles = rp.reader_profiles()
    reader_profiles.process_json_line(json.loads(sample_line_invalid))
    self.assertRaises(KeyError)

class test_also_likes(unittest.TestCase): 
  
  def test_get_document_readers_dict(self):
    self.assertEqual(also_likes.get_document_readers_dict(), {})  
  
  def test_get_read_by_vistor_dict(self):
    self.assertEqual(also_likes.get_read_by_vistor_dict(), {})  
  
  def test_sorting_function(self):
    custom_dict = {
      1:12,
      2:31,
      3:43,
      4:11,
      5:53,
      6:9,
      7:32,
      8:23,
      9:1,
      10:34,
      11:93,
      12:3,
    }
    
    also_likes.read_by_visitor_dict = custom_dict
    self.assertEqual([11, 5, 3, 10, 7, 2, 8, 1, 4, 6], also_likes.top_ten())
    
  def test_build_read_by_visitor(self):
    
    also_likes = al.also_likes()    
    also_likes.build_read_by_visitor(json.loads(sample_line_2),'64bf70296da2f9fd')
    dictionary = also_likes.read_by_visitor_dict
    self.assertEqual(0, len(dictionary))
  
  def test_build_read_by_visitor_key_error(self):
    also_likes = al.also_likes()    
    also_likes.build_read_by_visitor(json.loads(sample_line_invalid),'64bf70296da2f9fd')
    dictionary = also_likes.read_by_visitor_dict
    self.assertRaises(KeyError)
    
  
  def test_build_document_readers(self):
    also_likes = al.also_likes()
    also_likes.build_document_readers(json.loads(sample_line_2), '130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb')
    dictionary = also_likes.document_readers_dict
    self.assertEqual(1, dictionary['64bf70296da2f9fd'])
  
  def test_build_document_readers_key_error(self):
    also_likes = al.also_likes()
    also_likes.build_document_readers(json.loads(sample_line_invalid), '130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb')
    dictionary = also_likes.document_readers_dict
    self.assertRaises(KeyError)
    



# Source taken from
#https://stackoverflow.com/questions/5360833/how-do-i-run-multiple-classes-in-a-single-test-suite-in-python-using-unit-testin
def run_some_tests():
  
    test_classes_to_run = [test_views_by_location, test_views_by_browser, test_reader_profiles, test_also_likes]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
        
    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(big_suite)


if __name__ == '__main__':
  run_some_tests()