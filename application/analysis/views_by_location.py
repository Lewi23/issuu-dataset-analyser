import logging
import pycountry
import pycountry_convert as pc


continents = {
    'AF': 'Africa',
    'AN': 'Antarctica',
    'AS': 'Asia',
    'EU': 'Europe',
    'NA': 'North America',
    'OC': 'Oceania',
    'SA': 'South America', 
}

class views_by_location:
  """ Implements the logic to determine views by location (country and continent)
  """
  def __init__(self):
    self.views_by_country = {}
    self.views_by_continent = {}
    self.build_country_dict()
    self.build_continent_dict()
    
  def build_country_dict(self):
    """Builds a dictionary with an record for every country in the world

    :return: dictionary with a record for every country
    :rtype: dictionary
    """
    for i in range(len(pycountry.countries)):
      self.views_by_country[list(pycountry.countries)[i].name] = 0
    
    
    return self.views_by_country
  
  def build_continent_dict(self):
    """Builds a dictionary containing every continent
    """
    self.views_by_continent['Asia'] = 0
    self.views_by_continent['Africa'] = 0
    self.views_by_continent['North America'] = 0
    self.views_by_continent['South America'] = 0
    self.views_by_continent['Antarctica'] = 0
    self.views_by_continent['Europe'] = 0
    self.views_by_continent['Oceania'] = 0
    
    
    
  def process_json_line(self, line, document_id):
    """Processes a single line of the JSON file, adding the result to both country and continent dictionaries

    :param line: JSON line to procesess
    :type line: JSON
    :param document_id: document ID to check if the line is a match
    :type document_id: string
    """
    try:
      if document_id == line['subject_doc_id']:
        #country dict builder
        country = pycountry.countries.get(alpha_2=line['visitor_country'])
        self.views_by_country[country.name] += 1
      
        #continent dict builder
        continent_name = continents[pc.country_alpha2_to_continent_code(country.alpha_2)]
        self.views_by_continent[continent_name] += 1
    except KeyError:
      # Could not read data from this JSON line
      pass

      
  def remove_emtpy_dict_items(self, dictonary):
    """ Removes empty records from a dictionary

    :param dictonary: The dictionary to remove empty records from
    :type dictonary: dictionary
    :return: Inputted dictionary with empty records(value = 0 ) removed
    :rtype: dictionary
    """
    return {key:val for key, val in dictonary.items() if val != 0}
  
  def get_country_dict(self):
    """Returns the country dictionary

    :return: Country dictionary
    :rtype: dictionary
    """
    return self.remove_emtpy_dict_items(self.views_by_country)
  
  def get_continent_dict(self):
    """Returns the continent dictionary

    :return: Continent dictionary
    :rtype: dictionary
    """
    return self.remove_emtpy_dict_items(self.views_by_continent)
    






 
 


