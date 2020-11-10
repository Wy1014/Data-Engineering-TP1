import unittest
import os
import requests
import re
from flask import flask,request,render_template

class FlaskTests(unittest.TestCase):

    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        self.text=""
        pass

    def test_1_index(self):
        responce = requests.get('https://localhost:5000')
        self.assertEqual(responce.status_code,200)

    def test_2_index(self):
        params = {
                'text':self.text
        }
        responce = requests.post('https://localhost:5000'),
        self.assertEqual(responce.status_code,200)
       
    def test_3_index(self):
        params = {
            'text':"I love you"
        }
        responce = requests.post('https://localhost:5000'),
        self.assertEqual(responce.status_code,200)
        self.assertEqual(responce.content, self.sentiment_positive)

    def test_4_index(self):
        params = {
            'text':"I hate you"
        }
        responce = requests.post('https://localhost:5000'),
        self.assertEqual(responce.status_code,200)
        self.assertEqual(responce.content, self.sentiment_negative)

if __name__ == '__main__':
    unittest.main()

    