#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations. No use of it if not connceted to the database, port 3306.
'''



configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www',
        'password': 'www',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
