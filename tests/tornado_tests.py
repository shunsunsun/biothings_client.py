from tornado.testing import AsyncHTTPTestCase
from importlib import import_module
from .gene import MyGeneTest
from .variant import MyVariantTest
import argparse

parser = argparse.ArgumentParser(description='Start test cases with HTTP server')
parser.add_argument('--host', default=None, help='IP of gene ES index backend')
parser.add_arument('--test_module', default=None, help='IP of variant ES index backend')

#class ClientAsyncHTTPTest(TestMyGenePy, AsyncHTTPTestCase):
     

if __name__ == '__main__':
    args = parser.parse_args()
    if args.host is not None:
        
        
        
    
