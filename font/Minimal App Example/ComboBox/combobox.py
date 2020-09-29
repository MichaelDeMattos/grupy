#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("combobox.ui")

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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # -->  Variáveis globais
    
		# >> ComboBox Opção
		self.cb_op = builder.get_object("cb_op")
		self.lst_op = builder.get_object("lst_op")
		
		# >> ComboBox Categoria
		self.cb_cat = builder.get_object("cb_cat")
		self.lst_cat = builder.get_object("lst_cat")
		self.cat_default = (1, "- - - - - - -")
		self.lst_cat.append(self.cat_default)
		self.cb_cat.set_active(0)
		
		# >> Janela principal
		self.window = builder.get_object("main_window")
		self.window.set_title("GtkComboBox")
		self.window.show_all()
		
		# >> Categoria correspondente
		self.categoria = {"SALADA": "1 - FOLHAS",
                          "CENOURA": "2 - LEGUMES"}
		
	def on_cb_op_changed(self, *args):
		# >> Ao ser selecionado a opção a ListStore
		# >> é resetada para receber um novo valor 
		self.lst_cat.clear()
		
		# >> Instância da ComboBox Opção
		combo = self.cb_op
		
		# >> Recupera o modelo de dados da ComboBox Opção
		# >> passando o id ativo recupera o valor
		# >> selecionado atual
		dados = combo.get_model()[combo.get_active()][1]
		
		# >> Recupera o código e categoria
		# >> correspondente ao valor
		# >> recuperado da ComboBox Opção	
		cod_cat = self.categoria[dados].split()[0]
		categoria = self.categoria[dados].split()[2]
		
		# >> Monta a lista e adciona ao modelo da ListStore
		# >> da combo categoria
		lst_cat = (int(cod_cat), categoria)
		self.lst_cat.append(lst_cat)
		
		# >> Define o ID padrão selecionado na ComboBox Categoria
		self.cb_cat.set_active(0)
				
	def on_main_window_destroy(self, *args):
		Gtk.main_quit()
		
if __name__ == '__main__':
	builder.connect_signals(Handler())
	Gtk.main()
