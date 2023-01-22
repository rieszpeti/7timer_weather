# from unit import TestAPI
from timer_astro import dfs
from visualisation import apparentTempAndAvg, cloudCoverSeeing, budapestWindAndDirection

if __name__ == '__main__':
    apparentTempAndAvg()
    cloudCoverSeeing()
    budapestWindAndDirection(dfs)

    # Testing the API
    '''
    unittest.main()
    tester = TestAPI()
    if(tester.checkResponse()):          #you can only run the test if the connection good = true
        print(tester.checkcoordinates()) #print out the successful queries and the indexes of the unsuccessful ones
        print('Testing done')
    '''