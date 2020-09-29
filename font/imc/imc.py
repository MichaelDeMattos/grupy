#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import sys
import sqlite3
import traceback
import zlib
import datetime
import base64
import time

gi.require_version('Gtk', '3.0')
DEBUG = False
if DEBUG == True:
	os.system("rm -rf ~/grupy/font/imc/UtilGtk; ln -s ~/grupy/util/compiled/ ~/grupy/font/imc/UtilGtk")

from gi.repository import Gtk, Gdk
from UtilGtk.mikeUtil import MikeGtk

builder = Gtk.Builder()
init = 0

if DEBUG == True:
	builder.add_from_file("imc.ui")
else:
	builder.add_from_string(zlib.decompress(base64.b64decode(b'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')).decode("utf-8"))
	
class Handler(MikeGtk):
	def __init__(self, *args, **kwargs):
		super(Handler, self).__init__(*args, **kwargs)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
		# -- Estilos
		self.screen = Gdk.Screen()
		if DEBUG == True:
			self.path_style = "../../util/static/style.css"
			self.path_ico = "../../util/icons/balanca.ico"
			self.path_database = "../../data/imc.db"
		else:
			self.path_style = "/usr/local/bin/grupy/util/static/style.css"
			self.path_ico = "/usr/local/bin/grupy/util/icons/balanca.ico"
			self.path_database = "/usr/local/bin/grupy/data/imc.db"
			
		self.style_app(style_path=self.path_style, set_screen=self.screen)
		
		# -- Janela principal
		self.main_window = builder.get_object("main_window")
		self.main_window.show_all()
		self.main_window.set_title("Calculate IMC")
		self.img_bt_start = builder.get_object("img_bt_start")
	
		self.img_bt_start.set_from_file(self.path_ico)
		self.on_bt_clicked = builder.get_object("on_bt_clicked_start")
		
		# -- Janela calcular imc
		self.calculate_imc = builder.get_object("calculate_imc")
		self.calculate_imc.set_title("Calculate IMC")
		self.treeview_imc = builder.get_object("treeview_imc")
		self.list_imc = builder.get_object("list_imc")
		self.entry_name = builder.get_object("entry_name")
		self.entry_current_weight = builder.get_object("entry_current_weight")
		self.entry_height = builder.get_object("entry_height")
		
		# -- Message Dialog
		self.msg_dialog = builder.get_object("msg_dialog")
		
		# -- Conexão com o banco de dados
		self.conexao = sqlite3.connect(self.path_database)
		self.cursor = self.conexao.cursor()
		
		# -- Variável global utilizada para excluir registro do IMC
		self.cod_imc_select = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao fechar a janela principal
	def on_main_window_destroy(self, *args):
		Gtk.main_quit()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao clicar em começar inicia uma nova interface/janela
	def on_bt_clicked_start_clicked(self, *args):
		self.calculate_imc.set_transient_for(self.main_window)
		self.calculate_imc.set_modal(True)
		self.calculate_imc.set_destroy_with_parent(True)
		self.calculate_imc.show_all()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao clicar em começar inicia uma nova interface/janela
	def on_bt_calculate_imc_clicked(self, *args):
		try:
			nome = self.entry_name.get_text()
			current_weight = self.entry_current_weight.get_text()
			height = self.entry_height.get_text()
			imc = (float(current_weight) / (float(height) ** 2))
			imc_result = self.calculate_ideal_weight(imc)
			
			sql_args = [nome, current_weight, height, imc, imc_result]
			sql_new_history_imc = (" insert into history_imc"
							       " (name, current_weight,"
							       " height, imc, imc_result)"
							       " values (?, ?, ?, ?, ?)")
			
			self.cursor.execute(sql_new_history_imc, sql_args)
			self.conexao.commit()
			self.update_treeview()
			self.simple_msg_box(self.msg_dialog,title="Sucesso!",
							    text=("IMC calculado com sucesso!"))
							    
		except Exception as ex:
			print(traceback.print_exc(file=sys.stdout))
			self.simple_msg_box(self.msg_dialog,title="Erro!",
							    text=("Erro ao calcular IMC\n%s" % str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Faz a comparação referente ao IMC e retorna o resultado
	def calculate_ideal_weight(self, ideal_imc):
		imc = ""
		
		if ideal_imc < 18.5:
			imc = "Abaixo do peso"
		
		elif ideal_imc >= 18.5 and ideal_imc < 25:
			imc = "Normal"
		
		elif ideal_imc >= 25 and ideal_imc < 30:
			imc = "Sobrepeso"
		
		elif ideal_imc >= 30 and ideal_imc < 35:
			imc = "Obesidade grau I"
			
		elif ideal_imc >= 35 and ideal_imc < 40:
			imc = "Obesidade grau II"
		
		elif ideal_imc > 40:
			imc = "Obesidade grau III"
		
		return imc

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Faz  a busca no banco de dados e mostra na grade o resultado
	def update_treeview(self, *args):
		self.list_imc.clear()
		sql_search_imc_history = (" select cod_history_imc, name,"
								  " current_weight,"
								  " height, imc, imc_result"
								  " from history_imc")
		self.cursor.execute(sql_search_imc_history)
		search_imc_history = self.cursor.fetchall()
		for imc_history in search_imc_history:
			select = False
			cod_imc = str(imc_history[0])
			name = imc_history[1]
			current_weight = str(round(imc_history[2],2))
			heigth = str(round(imc_history[3],2))
			imc = str(round(imc_history[4],2))
			imc_result = imc_history[5]
			
			lst_imc_history = (select, cod_imc, name, current_weight, heigth, imc, imc_result)
			self.list_imc.append(lst_imc_history)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao editar a coluna nome na grade
	def on_render_name_edited(self, *args):
		try:
			cols = {"select": 0, "cod_imc": 1, "name": 2,"current_weight": 3,
					"heigth": 4, "imc": 5, "imc_result": 6}
			line = args[1]
			new_value = args[2]
			cod_imc_history = self.treeview_imc.get_model()[line][cols["cod_imc"]]

			sql_update_name = (" update history_imc"
							   " set name = :name"
							   " where cod_history_imc = :cod_imc")
			
			sql_args = {"name": new_value, "cod_imc": cod_imc_history}
			
			self.cursor.execute(sql_update_name, sql_args)
			self.conexao.commit()
			self.simple_msg_box(self.msg_dialog,title="Sucesso!!",
							    text=("Registro atualizado com sucesso!"))
		
		except Exception as ex:
			self.simple_msg_box(self.msg_dialog,title="Erro!",
							    text=("Erro ao atualizar o registro!\n%s" % str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao selecionar um item na grade
	def on_render_select_toggled(self, *args):
		try:
			cols = {"select": 0, "cod_imc": 1, "name": 2,"current_weight": 3,
					"heigth": 4, "imc": 5, "imc_result": 6}
			
			line = args[1]
			value_default = False
			new_value = True
			now_value = self.treeview_imc.get_model()[line][cols["select"]]
			cod_imc = self.treeview_imc.get_model()[line][cols["cod_imc"]]
			
			if now_value == False:
				self.cod_imc_select.append(cod_imc)
				print(self.cod_imc_select)
				self.treeview_imc.get_model()[line][cols["select"]] = new_value
			else:
				self.treeview_imc.get_model()[line][cols["select"]] = value_default
				remove_value = self.treeview_imc.get_model()[line][cols["cod_imc"]]
				self.cod_imc_select.remove(remove_value)

		except Exception as ex:
			self.simple_msg_box(self.msg_dialog,title="Erro!",
							    text=("Erro ao selecionar o registro!\n%s" % str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao clicar no botão excluir historico IMC
	def on_bt_delete_history_imc_clicked(self, *args):
		try:
			if self.cod_imc_select != [] or self.cod_imc_select == None:
				for i in self.cod_imc_select:
					sql_delete_imc_history = (" delete from history_imc"
									  	      " where cod_history_imc"
									 	      " in (:cod_imc)")
					sql_args = {"cod_imc": i}

					self.cursor.execute(sql_delete_imc_history, sql_args)
					self.conexao.commit()
					self.simple_msg_box(self.msg_dialog,title="Sucesso!",
							    		text=("Registro's excluído's com sucesso!\n"))
					self.cod_imc_select.remove(i)
					self.update_treeview()

		except Exception as ex:
			self.simple_msg_box(self.msg_dialog,title="Erro!",
							    	text=("Erro ao excluir o registro!\n%s" % str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao clicar em buscar atualiza a grade
	def on_bt_search_clicked(self, *args):
		self.update_treeview()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao fechar a janela calcular imc
	def on_calculate_imc_delete_event(self, *args):
		window = self.calculate_imc
		window.hide()
		return True
		
if __name__ == '__main__':
	builder.connect_signals(Handler())
	Gtk.main()
