#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

builder = gtk.Builder()
builder.add_from_file("simplegui.ui")

"""
Requirements: python3-gi, python3-gi-cairo, gir1.2-gtk-3.0

Copyright (C) 
Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.

Author: Michael de Mattos
"""

class Handler(object):
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)	
        # -- Window 
        window = builder.get_object("main_window")
        window.set_title("My first GUI")
        window.show_all()
        
        # -- Label
        self.label = builder.get_object("label")
        
        # -- Button
        self.bt_click_me = builder.get_object("bt_click_me")
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	#-- Ao botão ser pressionado muda o texto padrão da Label
    def on_bt_click_me_clicked(self, *args):
        if self.label.get_text() == "Hello World":
            self.label.set_text("Welcome to Gtk")
        else:
            self.label.set_text("Hello World")

            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #-- Finaliza execução da aplicação
    def on_main_window_destroy(self, *args):
        gtk.main_quit()
		
if __name__=='__main__':
    builder.connect_signals(Handler())
    gtk.main()
