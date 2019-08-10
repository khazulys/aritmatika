#!/bin/usr/python3

"""
	Program Aritmathika Sederhana
					"""

import os
import sys
from time import sleep

def main():
	try:
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print ("\033[1;30m	╔═╗┬─┐┬┌┬┐┌┬┐┌─┐┌┬┐┬ ┬┬┬┌─┌─┐	")
			print ("\033[1;31m	╠═╣├┬┘│ │ │││├─┤ │ ├─┤│├┴┐├─┤	")
			print ("\033[1;32m	╩ ╩┴└─┴ ┴ ┴ ┴┴ ┴ ┴ ┴ ┴┴┴ ┴┴ ┴	")
			print ("\033[1;36m	Coded By Khazul Yussery	")

			name = str(input("\n\033[1;32m[+]\033[1;35m Siapa nama kamu? "))
			if not name:
				exit("\033[1;31m[-]\033[1;33m Yahh kamu sombong banget sih. harus kasih tau nama dulu..")
			print ("\033[1;32m[√]\033[1;34m Hai " +name, "selamat menggunakan toolnya ya..")

			print ("\n\033[1;31m[+]\033[1;32m Menu Aritmathika tersedia dibawah ya: ")
			print ("\n\033[1;32m[01]\033[1;33m Penjumlahan ")
			print ("\033[1;32m[02]\033[1;33m Perkalian ")
			print ("\033[1;32m[03]\033[1;33m Pengurangan ")
			print ("\033[1;32m[04]\033[1;33m Pembagian ")
			pil = str(input("\n\033[1;31m[+]\033[1;32m Mau pilih yang mana: "))
			if pil == "1" or pil == "01":
				a1 = int(input("\n\033[1;35m[-]\033[1;36m Masukkan angka pertama:\033[1;33m "))
				a2 = int(input("\033[1;35m[-]\033[1;36m Masukkan Angka Kedua:\033[1;32m "))
				result = a1 + a2
				print ("\033[1;31m[√]\033[1;32m Result",a1,"+",a2,"=",result)
			elif pil == "2" or pil == "02":
				a1 = int(input("\n\033[1;35m[-]\033[1;36m Masukkan Angka Pertama:\033[1;33m "))
				a2 = int(input("\033[1;35m[-]\033[1;36m Masukkan Angka Kedua:\033[1;32m "))
				result = a1 * a2
				print ("\033[1;31m[√]\033[1;32m Result",a1,"x",a2,"=",result)
			elif pil == "3" or pil == "03":
				a1 = int(input("\n\033[1;35m[-]\033[1;36m Masukkan Angka Pertama:\033[1;33m "))
				a2 = int(input("\033[1;35m[-]\033[1;36m Masukkan Angka Kedua:\033[1;32m "))
				result = a1 - a2
				print ("\033[1;31m[√]\033[1;32m Result",a1,"-",a2,"=",result)
			elif pil == "4" or pil == "04":
				a1 = int(input("\n\033[1;35m[-]\033[1;36m Masukkan Angka Pertama:\033[1;33m "))
				a2 = int(input("\033[1;35m[-]\033[1;36m Masukkan Angka Kedua:\033[1;32m "))
				result = float( a1 / a2)
				print ("\033[1;31m[√]\033[1;32m Result",a1,"÷",a2,"=",result)

			break
	except KeyboardInterrupt:
		print ("Goodbye")
main()
try:
		while True:
			ul = input("\n\033[1;36m[?]\033[1;34m Mau ulang lagi?(y/n):\033[1;33m ")
			if ul == "y":
				main()
			if ul == "n":
				exit("\033[1;31m[!] Sampai ketemu lagi.. ")
except KeyboardInterrupt:
	print ("\033[1;31m[*]\033[1;35m Goodbyee..")
