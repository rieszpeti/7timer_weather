import unittest
import requests
import pandas as pd
import random

# Create one unit test for the REST API endpoint.
# It shall pass, if there is intelligible weather data in the response for an arbitrary location request
'''
coordinates = {
    'Budapest': (47, 19),
    'London': (51, 0),
    'New York': (40, 73),
    'Tokyo': (35, 139),
    'Cape Town': (33, 18)
}
data = requests.get("https://www.7timer.info/bin/astro.php",params=dict(lat=coord[0], lon=coord[1], unit='metric', output='json'))

lon, lat – Geographic coordinates of the specified site, must be given as pure float numbers, such as +23.090 or -23.090. 
At this stage, the precision of any incoming coordinate float number is expected to be 0.001. Incoming float with higher precision will be rounded.
ac – Altitude Correction, only applicable in ASTRO forecast. Should be 0 (default), 2 or 7.
lang – Language. Not applicable in METEO product.
unit – Metric or British.
output – should be internal (for graphical output), xml or json.
tzshift – Adjustment of timezone, should be 0, 1 or -1.
'''
class TestAPI(unittest.TestCase):
    '''
    def test_weather_data(self):
        self.assertEqual(True, False)  # add assertion here
    '''

    #URL = "https://www.7timer.info/bin/astro.php"

    def test_checkResponse(self):
        return requests.get("http://api.open-notify.org/astros.json")
    def test_checkcoordinates(self):
        testDf = pd.read_csv('test.csv', delimiter=';')
        dfs = []
        errors = [] # save the input's lines
        for i, (a, b) in enumerate(zip(testDf['latitude'], testDf['longitude'])):
            randomX = round(random.uniform(-100000000,100000000), 3)
            randomY = round(random.uniform(-100000000,100000000), 3)
            #randomX = -11111111111111111111111
            #randomY = -11111111111111111111111
            randomV = random.randint(0, 1)
            if(randomV == 1):
                 try:
                    a = randomX
                    b = randomY
                    data = requests.get("https://www.7timer.info/bin/astro.php",
                                    params=dict(lat=a, lon=b, unit='metric', output='json'))
                    df = pd.DataFrame(data.json()['dataseries'])
                    dfs.append(df)
                 except Exception as exception:
                     print('capture the flag')
                     errors.append(i)
            else:
                data = requests.get("https://www.7timer.info/bin/astro.php",
                                    params=dict(lat=a, lon=b, unit='metric', output='json'))
                df = pd.DataFrame(data.json()['dataseries'])
                dfs.append(df)
        return dfs, errors

if __name__ == '__main__':
    unittest.main()
    tester = TestAPI()
    if(tester.test_checkResponse()):          #you can only run the test if the connection good = true
        print(tester.test_checkcoordinates()) #print out the successful queries and the indexes of the unsuccessful ones
        print('Testing done')
