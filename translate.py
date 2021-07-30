try:
    import requests,os,sys
    from time import sleep
    import time;
except:
    os.system("pip install requests")
# untuk me-print waktu saat ini local
localtime = time.asctime(time.localtime(time.time()))

# nanya ing to ind
def ing_to_ind():
	nanya = input(" \033[1;90m[\033[1;96m~\033[1;90m] \033[1;93mPlease Choose \033[1;90m[\033[1;95m1 \033[1;0m= \033[1;95mMENU\033[1;90m] \033[1;92m&& \033[1;90m[\033[1;95m2 \033[1;0m= \033[1;95mAGAINT\033[1;90m] \033[1;92m&& \033[1;90m[\033[1;95m0 \033[1;0m= \033[1;95mEXIT\033[1;90m] \033[1;93m: \033[1;96m")
	if nanya == "" or nanya == " " or nanya == "  ":
		print(" \033[1;90m[\033[1;96m!\033[1;90m] \033[1;91m*********")
		time.sleep(1)
		clear()
		ing_to_ind()
	elif nanya == "1" or nanya == "01":
		menu()
	elif nanya == "2" or nanya == "02":
		inggris_to_indonesia()
	elif nanya == "0" or nanya == "00":
		os.system("python2 exit.py")
	else:
		print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;91mNot Found")
		time.sleep(2)
		clear()
		ing_to_ind()

# nanya ind to ing
def ind_to_ing():
	nanya = input(" \033[1;90m[\033[1;96m~\033[1;90m] \033[1;93mMohon Pilih \033[1;90m[\033[1;95m1 \033[1;0m= \033[1;95mMENU\033[1;90m] \033[1;92m&& \033[1;90m[\033[1;95m2 \033[1;0m= \033[1;95mLAGI\033[1;90m] \033[1;92m&& \033[1;90m[\033[1;95m0 \033[1;0m= \033[1;95mKELUAR\033[1;90m] \033[1;93m: \033[1;96m")
	if nanya == "" or nanya == " " or nanya == "  " or nanya == "   ":
		print(" \033[1;90m[\033[1;96m!\033[1;90m] \033[1;91mJangan Kosong !")
		time.sleep(2)
		clear()
		ind_to_ing()
	elif nanya == "1" or nanya == "01":
		menu()
	elif nanya == "2" or nanya == "02":
		indonesia_to_inggris()
	elif nanya == "0" or nanya == "00":
		os.system("python2 exit.py")
	else:
		print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;91mTidak Ada")
		time.sleep(2)
		clear()
		ind_to_ing()
# untuk meng clear clear()
clear = lambda : os.system("clear")
def menu():
	clear()
	print("\033[1;0m\033[1;41mSUBREK\033[1;0m \033[1;96mCHANNEL AING DLU")
	os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
	time.sleep(1)
	clear()
	print("\033[1;96m        ____  ___   ___   ____ _     _____")
	print("       / ___|/ _ \ / _ \ / ___| |   | ____|")
	print("      | |  _| | | | | | | |  _| |   |  _|")
	print("      | |_| | |_| | |_| | |_| | |___| |___")
	print("       \____|\___/ \___/ \____|_____|_____|")
	print("                 \033[1;0m\033[1;41mTRANSLATE v1.\033[1;0m")
	print("\033[1;96m+\033[1;90m===============================================\033[1;96m+")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mAuthor      \033[1;91m: \033[1;93mAmmar_SP")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mYouTube     \033[1;91m: \033[1;93mAmmarBN")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mWhatsApp    \033[1;91m: \033[1;93m+62 877-0877-3367")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mTeam       \033[1;91m : \033[1;93mPython Cyber Team")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mGithub      \033[1;91m: \033[4;92mhttps://github.com/AmmarBN")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mJenis Tools \033[1;91m: \033[1;93mRequests/Google Translate v1")
	print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mWaktu       \033[1;91m:\033[1;93m",localtime)
	print("\033[1;96m+\033[1;90m===============================================\033[1;96m+")
	print("\t\033[1;91m[ \033[1;92mMENU \033[1;91m]")
	print(" \033[1;90m[\033[1;93m01\033[1;90m] \033[1;96mIndonesia To Inggris")
	print(" \033[1;90m[\033[1;93m02\033[1;90m] \033[1;96mInggris To Indonesia")
	print(" \033[1;90m[\033[1;93m00\033[1;90m] \033[1;96mKeluar/Exit\n")
	print("\t\033[1;91m[ \033[1;92mINPUT \033[1;91m]")
	pilih = input(" \033[1;90m[\033[1;96m~\033[1;90m] \033[1;93mChoose Menu \033[1;90m~\033[1;92m•\033[1;93m> \033[1;95m")
	try:
		if pilih == "01" or pilih == "1":
			indonesia_to_inggris()
		elif pilih == "02" or pilih == "2":
			inggris_to_indonesia()
		elif pilih == "00" or pilih == "0":
			os.system("python2 exit.py")
		elif pilih == "" or pilih == " " or pilih == "  ":
			print(" \033[1;90m[\033[1;96m!\033[1;90m] \033[1;91mJangan Kosong !")
			time.sleep(1)
			menu()
		else:
			print(" \033[1;90m[\033[1;96m!\033[1;90m] \033[1;91mTidak Ada")
			time.sleep(1)
			menu()
	except ValueError:
		pass
def inggris_to_indonesia():
	clear()
	try:
		print("\033[1;0m\t\033[1;91m  ____  ___   ___   ____ _     _____")
		print("\t / ___|/ _ \ / _ \ / ___| |   | ____|")
		print("\t| |  _| | | | | | | |  _| |   |  _|")
		print("\t| |_| | |_| | |_| | |_| | |___| |___")
		print("\t \____|\___/ \___/ \____|_____|_____|\n")
		print("\t \033[1;93m    [ \033[1;96mInggris To Indonesia \033[1;93m]\n")
		Trans = input(" \033[1;90m[\033[1;95m~\033[1;90m] \033[1;93mTranslate \033[1;92m> \033[1;95m")
		ss = requests.get(r"https://translate.google.com/translate_a/t?client=at&sc=1&v=2.0&sl=en&tl=id&hl=nl&ie=UTF-8&oe=UTF-8&text="+Trans).json()
		for x in ss["sentences"]:
			print("\033[1;91m=============================================")
			print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mBahasa inggris  \033[1;91m :\033[1;93m",Trans) 
			print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mBahasa indonesia \033[1;91m:\033[1;93m",x["trans"])
			print("\033[1;91m============================================")
			ing_to_ind()
	except requests.exceptions.ConnectionError:
		print(" \033[1;90m[\033[1;96m!\033[1;90m] \033[1;91mPlease Check Your Connection Internet !")
		time.sleep(3)
		ing_to_ind()
def indonesia_to_inggris():
	clear()
	try:
		print("\033[1;0m\t\033[1;91m  ____  ___   ___   ____ _     _____")
		print("\t / ___|/ _ \ / _ \ / ___| |   | ____|")
		print("\t| |  _| | | | | | | |  _| |   |  _|")
		print("\t| |_| | |_| | |_| | |_| | |___| |___")
		print("\t \____|\___/ \___/ \____|_____|_____|\n")
		print("\t     \033[1;93m [ \033[1;96mIndonesia To Inggris \033[1;93m]\n")
		Trans = input(" \033[1;90m[\033[1;95m~\033[1;90m] \033[1;93mTranslate \033[1;92m> \033[1;95m")
		if Trans == "apakah saya ganteng" or Trans == "apakah saya ini ganteng?":
			print(" \033[1;90m[\033[1;93m•\033[1;90m] \033[1;96mGoogle Pribadi \033[1;91m> \033[1;95mYa")
		ss = requests.get(r"https://translate.google.com/translate_a/t?client=at&sc=1&v=2.0&sl=id&tl=en&hl=nl&ie=UTF-8&oe=UTF-8&text="+Trans).json()
		for x in ss["sentences"]:
			print("\033[1;91m=======================================")
			print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mBahasa indonesia \033[1;91m:\033[1;93m",Trans) 
			print(" \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mBahasa inggris   \033[1;91m:\033[1;93m",x["trans"])
			print("\033[1;91m=======================================")
			ind_to_ing()
	except requests.exceptions.ConnectionError:
		print(" \033[1;90m[\033[1;96m!\033[1;90m] \033[1;91mMohon Periksa Koneksi Internet Anda !")
		time.sleep(3)
		ind_to_ing()
menu()


