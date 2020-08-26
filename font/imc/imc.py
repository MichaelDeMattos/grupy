#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import sys
import sqlite3
import traceback
import zlib
import base64

gi.require_version('Gtk', '3.0')
DEBUG = False
if DEBUG == True:
	os.system("rm -rf ~/grupy/font/imc/UtilGtk; ln -s ~/grupy/util/compiled/ UtilGtk")

from gi.repository import Gtk, Gdk
from UtilGtk.mikeUtil import MikeGtk

builder = Gtk.Builder()

if DEBUG == True:
	builder.add_from_file("imc.ui")
else:
	builder.add_from_string(zlib.decompress(base64.b64decode(b'eJztW19v2zYQf++n0PQ6uE7SFhgG28WarUGBdhiabHskaOlicaZEh6TsuF9oH2RfbEdJcWSLtCX5T5zUL4Zl3ZF39zsej8dz7/19zL0pSMVE0vfPX5/5HiSBCFky6vt/3nzs/OS/H7zq/dDpeFeQgKQaQm/GdOSNOA3Be/P64uL1udfpIBFLNMhbGsDglef1JNylTILyOBv2/ZEe/+g/ToRsZ343oxPDfyDQXsCpUn3/So8/M6WvtZDgeyzs+xwfCYsD31AjfSB4Gicqf8JnI1r+WyehMXjZh5GneJ+/8/R8AihGEFFJpaTzfHbrCEEqJSSazICNIr3dWNEOxkDltx6AIBIpbyJIr1uydK+bw2RH7G+WhGKWwxVQHqQc3aSM2USKCUg9z8AxNAm5FUGq/MFHyhX0ug8EdnqUnX2jQw416UO4pagsmbFQR/7g7buzuhw5XHYWxUYJ5QsGDho6MEVH8b2IJiEH2fdFQpYMQHI6UtCpGZ1MAK2UiIWZg4jxcAHKhOP6iQQPQT7i8EixQl1B4oO4z2GIhsJ/IKuqO2WKZea8kWnFmm0Qs/EIyVBpqnHB+wNc+ZqhaayMS0rZFbsRgg+pzJWLKUuILn4p81WFMJ/+oKC1Td7KPG1NZOMrZCNKz82UQ6EjJ2vFUG5jfUi1RsNn9hpqYluWW5tgGzPYeDkdAvc9LWmiUFaz4vv+HHCoy1x86X36ctlkxFQBSRNcTJwlLZRRWgRjwkJ/gPtX55sQcYclawdYChIBZ8EYwuX4sAoGWVBZokNp5FIEXhaZBmPcrTcrA/cTFKMFLJGIxQg3f2FAXW9CfGMTZymGufWx69JKj1WmW8Z5s/U8EYrlsauyFTh1rehZJ7RdSXSwbJ2OzLcjCk0R5ejO/iAAk9ltG5U+Z6v7SENPTOUINxUOt7j7v2vBKfPEoQ2rFpN2jLhXaBE35HUH2d9FDD+vW9vbRiBjXUK1pkHkXFV2TjRRHcb64efkti/Gbf8AJTyqU8qfgfOen5z35Lwl5/2F61TSZ+C4F4d13N8SLed5VgTmK8kPcgdx5KasL9WPd+x6a0LfUW34FddbrgeenPC7dMIDb9wVJ4xOzvf9Ot9ONt9nVHFxGGpXFZfrQArOISzuLfZbcWnCpiKKAhFzJeMP3JXG2nVgCfAXg+JmRuPTFJ8OWAFuHEdEaI4rD1d+TVghMVk1MSU0Yoq9an0p/dGMXnZtmVDeyR4RBOBoxswPKywuK18veCqFW8dG4MbRPYvB8jK7lLOKZokhTCOCrlrPOtusF88u4iVw/hVMtR3kDdzr3O1k9kuev1uMUwyGkU6yYapBuUjKRA/qmUlMerh44Ry/u2kCJ0juXeA4kX0shxwU35UkeS9In5+QrtYODoqyyUJ1tB90L07oltHdcNO5Xjq7hGuhNVnBXnB9c8K1jOvXrBEH87xNd9nr5bTLugnhog1oP0C/PTqg7Qx7ORs1SfO3ORo5joKbj0bLKpZe1u/tyvpuZuVD0xN3dl007+yysax0diktxXy5aaOkOVkQHLSb6/5FtXPZ7qUcrVsmkB5l41a9olfLglerYlfbQtcu+7CeUZVpz309qx14eZsXUZrK1Tqu3fWH2QCH8v0mbBICYFNQpIiuzbhf0MKp1+5XRr5Wu1/dAt+nmI6KNnkWj8xcNu9q7S0bPKbxhb9pddVsQrJ00RpeOLtLwaN3KfMmVFIvEDH896+7c/dFpnitq98tU7wvoBT60a+McjEqMj01ImH+vJtEz5S0ScQS9M183E0MefDD4cW4QtoiyapUeafllMqeej1V/rR6KYCwI+qO1N+hHs2q0YRKoEvRwLVNLevbVmcbX+3u4WoWMhepfuiLxyNsw+uQql84ls3uRnmS5KcRyw6ynxpRptct/Rfsf+A2j3g=')).decode("utf-8"))
	
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
		sql_search_imc_history = (" select name, current_weight,"
								  " height, imc, imc_result"
								  " from history_imc")
		self.cursor.execute(sql_search_imc_history)
		search_imc_history = self.cursor.fetchall()
		for imc_history in search_imc_history:
			name = imc_history[0]
			current_weight = str(round(imc_history[1],2))
			heigth = str(round(imc_history[2],2))
			imc = str(round(imc_history[3],2))
			imc_result = imc_history[4]
			
			lst_imc_history = (name, current_weight, heigth, imc, imc_result)
			self.list_imc.append(lst_imc_history)
			
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# -- Ao fechar a janela calcular imc
	def on_calculate_imc_delete_event(self, *args):
		window = self.calculate_imc
		window.hide()
		return True
		
if __name__ == '__main__':
    builder.connect_signals(Handler())
    Gtk.main()
