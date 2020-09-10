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
DEBUG = True
if DEBUG == True:
	os.system("rm -rf ~/grupy/font/imc/UtilGtk; ln -s ~/grupy/util/compiled/ ~/grupy/font/imc/UtilGtk")

from gi.repository import Gtk, Gdk
from UtilGtk.mikeUtil import MikeGtk

builder = Gtk.Builder()
init = 0

if DEBUG == True:
	builder.add_from_file("imc.ui")
else:
	builder.add_from_string(zlib.decompress(base64.b64decode(b'eJztXM1y2zYQvucpWPbYkf/SZDodS5naTTKZaTqd2G2PGIhckaghQgZA2+rr9JAH6CP4xbogKZkUQYqkfiy5unhEErtY7H5YLHYBn797GHPnDqRiIuq7p0cnrgORJ3wWBX339+sPvR/cd4NX59/0es5HiEBSDb5zz3ToBJz64Lw+Ojs7OnV6PWzEIg1yRD0YvHKccwm3MZOgHM6GfTfQN9+5Tx0h2Yl7nLQTw7/A047HqVJ996O++YUOgbsO8/suHxLNOJChJj5w0EDY2CMhU1rIqWvIkcFEiglIPXUiOoa+e8cUG3JwB9cyhvPj2Vd7Y49GZCS8WLmDD5Srpe15KpuWNFKcaood9d0pIPn7B4/jeEsMqNaSDWMNKn2Rf5UxHYlI93xQHiqI8hjfXCF750Jw3znN1IRkx0VW58ep5popUada9Cj3YhQ8UWSFAs1fd7DYeJlmnkntl6mM0vn0+XLHda+ASi/cLdRexMqjuwNanNhXOLUhUx4+5nHqCR6PoyeRjFNK3/WMTI5CF4H8jC/KWqRfHT2doHzBUAgONJrJZuGAjs90WM3CC6mkUtJpDZPkz0ocvFhKiDS5BxaENQNqwitcA4+VVWK8Ni4FMW8jyPlxzuD1wPmTRb64T1HTxMW1nUAoO/ubJvOzUXsfRhQHS+6Zr3HGvz05aUqRmstOolgQUT4nMOthD+4QKK4T0sjnIPuuiIpue7ZuZu3UPZ1MALUUibmavZBxf26UCccFPMRZDPLJDk8tFlqXLHEhHlIzhEPhzpq1dHddLGajEZLhoKnGiMMdYOihGaqmCaGaUA8DIHfwxtq6oAK7Gq7R1QypTFUxpiwiOnuTp6tae7O2ts47KbOrQm10mWxE6anpcih0WElaUlS1si5irdFMib4q4pSVVbCKGmy0TKF0EyE1xanVuudYAYkjnGacRR0ET9Z042ACwM4rY7w2LDGq9m4I890BRus9hQPrUeVBZDYDtXwKjsnjzLsBv+iTFsUi81YWj5TjnPP6Rcmpd4NSLR8TPExQjA7GDcVYBLjjEQ2ggV9s8hQc5/xl90mRufJs+7PLM2P92K7aBHbHd8prdVyXrbJn4K63zpawXdgc1Yn+QvBc2BN2B/EIA9/VIZxKsWewXZtPtg3IPphOA1kkGjHO24VqE6FYGsSW9gSVYy2Ns0nU+lEirpIZGZhfOxR1hpQjkN2B0lTqpkRDqsBMWCJxb2iP5e2asWsnTevsqIcaUxngLoPDSNcMtYZSpvvOLqRaTLoR4uZBi3FL2upk1q9iDD/WeYRVHZfRLqFaU7NSVcxFOyWqqAnhJhbbA2x3HLa/gRIO1THlewDe0wN4D+DNgfcnrmNJ9wC4Z9sF7vtIy2kaS4H5SdLM3laA3Jb0peJ4zdCrcX07teCXoFcsJ+0oCBtF+DbCl4reMm1STSKmTqb2AvdbjhVKuA8PeD/gfYt4X0uIsUfZqApFrSsbdeVJwTn4WXF/s9moNmQqpCgQMecW3AGLVi5/SoA/GGTHFzQ+3eFTw/JOVjDOiNog91kiTeGb7dzsYE8bUojMroOYxCQxST1VX3t+MoCTHEuMKO8lj2i+5JhQguASSZV9ruY0pXx4xar1JEDzXgwKLpMzL1bRLN7H1BGs+zIj8OPXx39EnYLqZbTLeQmcfwFTCwF5LYKAZ4e1ZPKOpMrFhcJ8WUwhFzgXKhOz9oXKhJ1lfXXiySb2NWH+vXzEra5RJiZFDNxBEtHPP1VLsKyLStzUib+LYPv28vFf/2ijSIMHXcCZh54kcZHVCOhkYW06Mivbwb7FxPpWrVuRLKmSHHymaaO1bM6h4H0MfYXzMQ3I7Pszep4Ul2cHXNoz59v1PcV8ykY80OuDpctp5q1a2WQPdLgZ635/sG7eupa7G82ls0tYa9qNxQ1vDnbN2/VLcuQfN8u22znN5bTLuszC2YWDzRj67c4Z2k6wkQRTm1zJKvmlinza8vxScYi5j81vkSRn9u/zmadnvkNy9qb1HRIbycIdEqWlmBYD39zIybzBVu+NPPyPL47YDjxU5PyM2206qbZ6WK9ZhaJjdaJTZaJrVaL5OYi6e6gZr/1J7G/4mOniXZ/02DFJKmGNoD9MGGwL+23IJHjA7kCRzBe3o35BE6fZlaC85RsdP29aU/k0pkGWmGbjIDnjbkFXZ7QsQUzrk2TmUp1mE5IEl1b3wtltDA69jZkzoZI6nhjD49fqO4IvMiDsXHDsGBB+BqUQRz8zykWQxYUqIH76vJ6w0FQRScjMDcKU7zKC1Pkhe3FTatohJCuVx+7yAZg9UNujaKs0PJqU8QiVQAveoGqZKo6365htdI0vYZWjkKmI9ewGLlTdAHqWgKMVyRoijgYz+/w4949p/gMEzXbH')).decode("utf-8"))
	
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