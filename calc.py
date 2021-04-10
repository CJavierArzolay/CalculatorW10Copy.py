from tkinter import *
from math import sqrt
from calc_opt import *
#R = Root
R = Tk()
R.title("Calculadora W10")
R.geometry("472x657")
try:
	R.iconbitmap("favicon.ico")
except:
	pass

R.config(bg="#bbb")
R.resizable(False,False)
#aop == Aux-OPeration,
#ioperation == Labeling-OPeration.
global aop
global ioperation
ioperation = ""
aop = 0
#mp == MapPing,
#p == Possitioner.
for p,mp in enumerate(["cb","ub","mb","ob"]):
	
	#mpv == MapPing-Variable.
	mpv=Frame()
	mpv.config(width="472",height="56",bg="white")
	mpv.grid(row=p, column=0)
	#1'st: ub == Upper-Bars.
	if mp == "ub":
		entry=StringVar()
		mpv.config(height="140",bg="dark red")
		menu=Button()
		tx=Entry(R,font="Verdana 40",width="10",textvariable=entry,selectbackground="#d1d1d1")
		entry.set(0)
		tx.config(bg="#fff",fg="#303030",justify="right",bd=0)
		tx.grid(row=1,column=0,sticky="nwse",columnspan=5)
		menu.config(height="3", width="6")
		menu.grid(row=0,column=0,sticky="nws")
		exoperation = Label(bg="#aaa",fg="#303030",anchor="e",bd=0,font="Verdana 12",width="24")
		exoperation.place(x=52,y=36,width="420")
	#2'nd: mb == Memory-Buttons.
	elif mp == "mb":
		mpv.config(bg="#ffcccb")
		liste = []
		for c,mbl in enumerate(["MC","MR","M+","M-","MS"],0):
			#c == Counter
			#mbl == Memory-Buttons-Labeling,
			#mebv == MEmory-Buttons-Variable.
			mebv=Button(height="3",width="11",text=mbl,bd=0,bg="#fff")
			mebv.config(command= lambda button=mebv:work(button))
			mebv.grid(row=2,column=c,sticky="nsew")
	#3'rd/last: ob == Option-Buttons
	elif mp == "ob":
		#cpl == Columns-PLacing
		#rpl == Rows-PLacing
		cpl=0
		for obm in ["%","√","x²","¹/x"]:
			#obm == Options-Buttons-Mapping
			ob=Button(font=("Verdana","16"),width="16",height="4",text=obm,bd=0,bg="#fff",anchor="center")
			ob.place(x=cpl,y=255,width="118",height="67")
			ob.config(command= lambda button=ob:work(button))
			cpl+=118
		mpv.config(height="435",bg="#ccc")
		cpl=0
		rpl=322
		for obm in [["CE","C","<-","÷"],["7","8","9","X"],["4","5","6","-"],["1","2","3","+"],["±","0",",","="]]:
			#obm == Options-Buttons-Mapping
			for obsm in obm:
				ob=Button(height="4", width="16",text=obsm,bd=0,bg="#ccc",font=("Verdana","16"))
				ob.config(command= lambda button=ob:work(button))
				ob.place(x=cpl,y=rpl,width="118",height="67")
				cpl+=118
			cpl=0
			rpl+=67
	mpv.grid(columnspan=5,sticky="nw")



# def specfunt(ope):
# 	global aop
# 	global ioperation
# 	global specform


# 	if ioperation[ioperation.rfind(" ") - 1] == "+":
# 		aop += ope
# 	elif ioperation[ioperation.rfind(" ") - 1] == "-":
# 		aop -= ope
# 	elif ioperation[ioperation.rfind(" ") - 1] == "*":
# 		aop *= ope
# 	elif ioperation[ioperation.rfind(" ") - 1] == "/":
# 		try:
# 			aop /= ope
# 		except ZeroDivisionError:
# 			entry.set("Error x / 0")


def translate():
	e = ""
	for i in entry.get()[::-1].replace(".","").replace("-",""):
		e += i
		if entry.get().find(",") != -1:
			if e.count(",") == 0:
				print(e)
				continue
			else:
				if len(e.replace(".","").replace(e[:e.find(",")+1],"")) % 3 == 0 and len(e.replace(".","").replace(e[:e.find(",")+1],"")) != 0:
					e+="."
				else:
					print(e)
					continue
		else:
			if len(e.replace(".","")) % 3 == 0:
				e+="."
	if entry.get().find("-") != -1:
		e += "-"
	entry.set(e[::-1])
	if entry.get().replace("-","").find(".") == 0:
		entry.set(entry.get().replace(".","",1))

#so == Selected-Option.

def work(so):
	global exoperation
	global aop
	global ioperation
	global specform
#---------ZeroDivisionError-------------

	if entry.get() == "Error x / 0":
		if so.cget("text") == "CE" or so.cget("text") == "C":
			tx.delete(0,len(str(entry)))
			entry.set("0")
			for i in range(len(ioperation)):
				ioperation = ioperation[:-1]
			aop = 0
			print(ioperation)
			exoperation.config(text=ioperation)
		else:
			pass

#----------Add-A-Number----------------
	elif so.cget("text").isdigit() ==True:
		if ioperation.rfind(" ") == len(ioperation)-1 and len(ioperation)-1 != -1:
			entry.set(so.cget("text"))
			ioperation += so.cget("text")
			print(ioperation)
		elif entry.get() == "0" or ioperation == "":
			entry.set(so.cget("text"))
			ioperation = so.cget("text")
			print(ioperation)
		elif so.cget("text") == "0" and entry.get() =="0" or len(entry.get()) == 21:
			pass
		else:
			if entry.get().find(",") != -1:
				entry.set(entry.get()+str(so.cget("text")))
			else:
				entry.set(entry.get()+str(so.cget("text")))
				translate()
			ioperation += so.cget("text")
			print(ioperation)

#--------------ClearEntry--------------

	elif so.cget("text") == "CE":
		tx.delete(0,len(str(entry)))
		entry.set("0")
		for i in range(ioperation.rfind(" ")+1,len(ioperation)):
			ioperation = ioperation[:-1]
		print(ioperation)

#--------------Clear---------------

	elif so.cget("text") == "C":

		tx.delete(0,len(str(entry)))
		entry.set("0")
		for i in range(len(ioperation)):
			ioperation = ioperation[:-1]
		aop = 0
		print(ioperation)
		exoperation.config(text=ioperation)

#-----------Delete----------------

	elif so.cget("text") == "<-":
		if len(entry.get().replace("-","")) == 1:
			entry.set("0")
			ioperation = ioperation[:-1]
			print(ioperation)
		else:
			tx.delete(len(entry.get())-1)
			ioperation = ioperation[:-1]
			print(ioperation)
			translate()

#-----------------Comma-------------------

	elif so.cget("text") == ",":
		if entry.get().count(",") == 1:
			pass
		else:
			entry.set(entry.get() + ",")
			ioperation +="."

#-------------Reciprocal----------------------

	elif so.cget("text") == "¹/x":
		try:
			if exoperation.cget("text") == "":
				print(exoperation.cget("text"))
				ioperation = "( 1 / {})".format(entry.get().replace(".","").replace(",","."))
				if str(eval(ioperation)).find(".") == -1:
					entry.set(int(eval(ioperation)))
				else:
					entry.set(eval(ioperation))
			else:
				try:
					if ioperation[ioperation.find("( 1 / ")-1] < -1:
						ioperation = "( 1 / {})".format(entry.get().replace(".","").replace(",","."))
						if str(eval(ioperation)).find(".") == -1:
							entry.set(eval(ioperation))
						else:
							entry.set(int(eval(ioperation)))
				except IndexError:
					print("work")
					ioperation = "( 1 / {})".format(ioperation)
					print(ioperation)
					if str(eval(ioperation)).find(".") == -1:
						entry.set(eval(ioperation))
					else:
						entry.set(int(eval(ioperation)))
					# ioperation += "( 1 / {})".format(entry.get().replace(".","").replace(",","."))
				translate()
		except ZeroDivisionError:
			entry.set("Error x / 0")
		exoperation.config(text=ioperation.replace("( 1 / ","reciproc("))
		print(ioperation)

#-------------Squaring----------------------

	elif so.cget("text") == "x²":
		aop = float(entry.get().replace(".","").replace(",",".")) ** 2
		try:
			if aop / int(aop) == 1:
				entry.set(str(int(aop)))
				translate()
				ioperation = "sqr({})".format(ioperation)
			else:
				entry.set(str(round(aop,10)).replace(".",","))
				translate()
				ioperation = "sqr({})".format(ioperation)
		except ZeroDivisionError:
			entry.set(str(int(aop)))
			e = "0"
		exoperation.config(text=ioperation)
		print(ioperation)

#-------------SquareRoot--------------------

	elif so.cget("text") == "√":
		aop = sqrt(float(entry.get().replace(".","").replace(",",".")))
		e = ""
		try:
			if aop / int(aop) == 1:
				entry.set(str(int(aop)))
				translate()
				ioperation = "sqrt({})".format(ioperation)
			else:
				entry.set(str(round(aop,10)).replace(".",","))
				translate()
				ioperation = "sqrt({})".format(ioperation)
		except ZeroDivisionError:
			entry.set(str(int(aop)))
			e = "0"
		exoperation.config(text=ioperation)
		print(ioperation)

#-------------Substract---------------


	elif so.cget("text") == "-":
		if exoperation.cget("text") == "":
			ioperation = entry.get().replace(".","").replace(",",".") +" - "
			print(ioperation)
	#--------------Substract Concat--------------
		else:
			try:
				if ioperation[ioperation.rfind(" ")+1]:
					pass
				ioperation += " - "
				entry.set(eval(ioperation[::-1].replace(" - ", "",1)[::-1]))
				translate()
				print(ioperation)
			except IndexError:
				pass
		exoperation.config(text=ioperation.replace("( 1 /","reciproc(").replace(".",","))

#--------------Division-------------------

	elif so.cget("text") == "÷":
		if exoperation.cget("text") == "":
			ioperation = entry.get().replace(".","").replace(",",".") +" / "
			print(ioperation)
	#--------------Division Concat--------------
		else:
			try:
				if ioperation[ioperation.rfind(" ")+1]:
					pass
				ioperation += " / "
				entry.set(eval(ioperation[::-1].replace(" / ", "",1)[::-1]))
				translate()
				print(ioperation)
			except IndexError:
				pass
		exoperation.config(text=ioperation.replace("( 1 /","reciproc(").replace(".",","))

#-----------Percentage---------

	elif so.cget("text") == "%":
		if entry.get() == "":
			pass
		elif ioperation.rfind(" ") == -1:
			print(True)
			if entry.get().count(",") == 1:
				entry.set(str((float(entry.get())*0)/100))
			else:
				entry.set(str((int(entry.get())*0)/100))
		elif ioperation[ioperation.rfind(" ")] == "*":
			entry.set(str((int(ioperation[int(0),int(ioperation.find(" "))])*int(entry.get()))/100))

#---------------Multiply----------

	elif so.cget("text") == "X":
		if exoperation.cget("text") == "":
			ioperation = entry.get().replace(".","").replace(",",".") +" * "
			print(ioperation)
	#--------------Multiply Concat--------------
		else:
			try:
				if ioperation[ioperation.rfind(" ")+1]:
					pass
				ioperation += " * "
				entry.set(eval(ioperation[::-1].replace(" * ", "",1)[::-1]))
				translate()
				print(ioperation)
			except IndexError:
				pass
		exoperation.config(text=ioperation.replace("( 1 /","reciproc(").replace(".",","))

#----------More Less--------------

	elif so.cget("text") == "±":
		if entry.get() == "0":
			pass
		elif entry.get()[0] == "-":
			entry.set(entry.get()[1:])
		else:
			entry.set("-"+entry.get())

#------------------Addition----------------

	elif so.cget("text") == "+":
		#--------------Standar Addition-------------
		if exoperation.cget("text") == "":
			ioperation = entry.get().replace(".","").replace(",",".") +" + "
			print(ioperation)

		#--------------Addition Concat--------------
		else:
			try:
				if ioperation[ioperation.rfind(" ")+1]:
					pass
				ioperation += " + "
				entry.set(eval(ioperation[::-1].replace(" + ", "",1)[::-1]))
				translate()
				print(ioperation)
			except IndexError:
				pass
		exoperation.config(text=ioperation.replace("( 1 /","reciproc(").replace(".",","))

#------------Equal----------------------

	elif so.cget("text") == "=":
		if ioperation == "":
			entry.set(entry.get())
		else:
			entry.set(str(eval(ioperation)).replace(".",","))
			print(ioperation)
			translate()
			ioperation = ""
			aop = 0
			exoperation.config(text="")


R.mainloop()