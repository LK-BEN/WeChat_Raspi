# -*- coding: utf-8 -*-
# filename: main.py
import web
from prph import * 
from handle import Handle

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    #read_data.init_dht()
    raspi_led.init_led(18)
    app.run()

# sudo python -m SimpleHTTPServer 80
