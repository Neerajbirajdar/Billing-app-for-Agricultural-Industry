from tkinter import *
from datetime import datetime


root = Tk()
root.configure(bg='turquoise')
root.title("Billing App")
nov = datetime.now()
root.geometry("1350x1100")
Heading = Label(root, text="Billing for Resins Sortex Maachine", font="arial 30 bold", bg="turquoise", fg="black").place(
	relx=0.2, rely=.0)

######################Functions###############################
x = 0

def submit_data():
	path = 'Book1.xlsx'
	df1 = pd.read_excel(path)
	seriesA = df1['Name']
	seriesB = df1['Phone No.']
	seriesC = df1['Town']
	seriesD = df1['Total bill']
	
	A = pd.series(name.get())
	B = pd.series(phone.get())
	C = pd.series(town_var.get())
	D = pd.series(total_rate.get())
	
	seriesA = seriesA.append(A)
	seriesB = seriesB.append(B)
	seriesC = seriesC.append(C)
	seriesD = seriesD.append(D)
	
	df2 = pd.DataFrame({'Name': seriesA, '''Phone No.':seriesB,''''Town': seriesC,
	                    'Total bill': seriesD})
	df2.to_excel(path, index=False)

def total_bill():
	ntgq = float(nettgqnt.get())
	ntgr = float(nettgrate.get())
	nttt = (ntgq * ntgr * 15)
	ntt = str('%.2f' % nttt)
	nettdisp.set(ntt)
	
	wshr = float(washrate.get())
	wshq = float(washent.get())
	wshttt = (wshr * wshq * 15)
	wshtt = str('%.2f' % wshttt)
	washdisp.set(wshtt)
	
	tper = float(taperate.get())
	tpeq = float(tapeqty.get())
	tpett = (tper * tpeq)
	tpet = str('%.2f' % tpett)
	tapedisp.set(tpet)
	
	bxr = float(boxrate.get())
	bxq = float(boxqty.get())
	bxtt = (bxr * bxq)
	bxt = str('%.2f' % bxtt)
	boxdisp.set(bxt)
	
	cryr = float(caryrate.get())
	cryq = float(caryqty.get())
	cryrr = (cryr * cryq)
	cryrrr = str('%.2f' % cryrr)
	carydisp.set(cryrrr)
	
	diq = float(dipqty.get())
	dipr = float(diprate.get())
	dit = (diq * dipr)
	ditt = str('%.2f' % dit)
	dipdisp.set(ditt)
	
	carq = float(carbqty.get())
	carr = float(carbrate.get())
	cart = (carr * carq)
	cartt = str('%.2f' % cart)
	carbdisp.set(cartt)
	
	subtt = float(subt_var.get())
	
	totalt = (nttt + wshttt + tpett + bxtt + subtt + cart + dit + cryrr)
	totll = str('%.2f' % totalt)
	total_rate.set(totll)
	y = x + 1
	referr = "000", str('%d' % y)
	refer_var.set(referr)

def btnreset():
	town_var.set("")
	name.set("")
	phone.set("")
	washrate.set("0")
	washent.set("0")
	nettgrate.set("0")
	nettgqnt.set("0")
	taperate.set("0")
	tapeqty.set("0")
	boxqty.set("0")
	boxrate.set("0")
	nettdisp.set("0")
	washdisp.set("0")
	boxdisp.set("0")
	tapedisp.set("0")
	total_rate.set("0")
	subt_var.set("0")
	caryqty.set("0")
	caryrate.set("0")
	carydisp.set("0")
	dipqty.set("0")
	diprate.set("0")
	dipdisp.set("0")
	carbqty.set("0")
	carbrate.set("0")
	carbdisp.set("0")
	
	paidamt.set("0")
	
	wak1.set("")
	wak2.set("")
	wak3.set("")
	wak4.set("")
	wak5.set("")
	wak6.set("")
	wak7.set("")
	wak8.set("")
	wak9.set("")
	wak10.set("")
	wakno.set("0")
	wakno1.set("0")
	wakno2.set("0")
	wakno3.set("0")
	wakno4.set("0")
	wakno5.set("0")
	wakno6.set("0")
	wakno7.set("0")
	wakno8.set("0")
	wakno9.set("0")
	wakno10.set("0")
	finbl.set("0")

def paidamount():
	inibill = float(total_rate.get())
	givenbill = float(paidamt.get())
	
	finalbill = (inibill - givenbill)
	fin = "Rs", str('%.2f' % finalbill)
	finbl.set(fin)

# topframe=Frame()
############ Name ##########
name = StringVar()
phone = StringVar()
nettgqnt = StringVar()
nettgrate = StringVar()
washent = StringVar()
washrate = StringVar()
boxqty = StringVar()
boxrate = StringVar()
tapeqty = StringVar()
taperate = StringVar()
nettdisp = StringVar()
washdisp = StringVar()
boxdisp = StringVar()
tapedisp = StringVar()
total_rate = StringVar()
refer_var = StringVar()
town_var = StringVar()
subt_var = StringVar()
caryqty = StringVar()
caryrate = StringVar()
carydisp = StringVar()
dipqty = StringVar()
diprate = StringVar()
dipdisp = StringVar()
carbqty = StringVar()
carbrate = StringVar()
carbdisp = StringVar()

txtname = Label(root, text="      Name :", bg="turquoise", font="arial 15").place(relx=.0, rely=.1)
txtnameent = Entry(root, width=25, bg="powder blue", textvariable=name,
                   font="arial 15").place(relx=.1, rely=.1)

ph_lb = Label(root, text="    Mobile No :", bg="turquoise", font="arial 15").place(relx=0.3, rely=0.1)
ph_ent = Entry(root, width=12, bg="powder blue", textvariable=phone,
               font="arial 15").place(relx=0.4, rely=0.1)

# clock=Label(root,text=nov,font="arial 15").place(relx=0.7,rely=0.1)

############## Labels #############

qty = Label(root, text="Quantity", bg="turquoise", font="Arial 15").place(relx=0.1, rely=0.2)
price = Label(root, text="  Rate", bg="turquoise", font="Arial 15").place(relx=0.2, rely=0.2)
subtotal = Label(root, text="Sub Total", bg="turquoise", font="Arial 15").place(relx=0.3, rely=0.2)
reference = Label(root, text="    Receipt No.", bg="turquoise", font="Arial 15").place(relx=0.7, rely=0.0)
town_lab = Label(root, text="         Town:", bg="turquoise", font="Arial 15").place(relx=0.5, rely=0.1)

############### Ingredients ##################333

Netting = Label(root, text="NETTING   :", bg="turquoise", font="Arial 15").place(relx=0.0, y=200)
Netting_entq = Entry(root, font="Arial 15", textvariable=nettgqnt, width=7,
                     justify="right", bg="Powder blue").place(relx=0.1, y=200)
Netting_entr = Entry(root, font="Arial 15", textvariable=nettgrate, width=7,
                     justify="right", bg="Powder blue").place(relx=0.2, y=200)
Netting_disp = Entry(root, font="Arial 15", textvariable=nettdisp, width=10,
                     justify="right", bg="Powder blue").place(relx=0.3, y=200)

wash = Label(root, text="WASHING  :", bg="turquoise", font="Arial 15").place(relx=0.0, y=250)
wash_entq = Entry(root, font="Arial 15", textvariable=washent, width=7,
                  justify="right", bg="Powder blue").place(relx=0.1, y=250)
wash_entr = Entry(root, font="Arial 15", textvariable=washrate, width=7,
                  justify="right", bg="Powder blue").place(relx=0.2, y=250)
wash_disp = Entry(root, font="Arial 15", textvariable=washdisp, width=10,
                  justify="right", bg="Powder blue").place(relx=0.3, y=250)

box = Label(root, text="BOX          :", bg="turquoise", font="Arial 15").place(relx=0.0, y=300)
box_entq = Entry(root, font="Arial 15", textvariable=boxqty, width=7,
                 justify="right", bg="Powder blue").place(relx=0.1, y=300)
box_entr = Entry(root, font="Arial 15", width=7, textvariable=boxrate,
                 justify="right", bg="Powder blue").place(relx=0.2, y=300)
box_disp = Entry(root, font="Arial 15", textvariable=boxdisp, width=10,
                 justify="right", bg="Powder blue").place(relx=0.3, y=300)

tape = Label(root, text="TAPE         :", bg="turquoise", font="Arial 15").place(relx=0.0, y=350)
tape_entq = Entry(root, font="Arial 15", textvariable=tapeqty, width=7,
                  justify="right", bg="Powder blue").place(relx=0.1, y=350)
tape_entr = Entry(root, font="Arial 15", textvariable=taperate, width=7,
                  justify="right",
                  bg="Powder blue").place(relx=0.2, y=350)
tape_disp = Entry(root, font="Arial 15", textvariable=tapedisp, width=10,
                  justify="right", bg="Powder blue").place(relx=0.3, y=350)

cary = Label(root, text="CARRY BAG:", bg="turquoise", font="Arial 15").place(relx=0.0, y=400)
cary_entr = Entry(root, font="arial 15", textvariable=caryqty, width=7,
                  justify="right", bg="Powder blue").place(relx=0.1, y=400)
cary_rate = Entry(root, font="arial 15", textvariable=caryrate, width=7,
                  justify="right", bg="Powder blue").place(relx=0.2, y=400)
cary_disp = Entry(root, font="arial 15", textvariable=carydisp, width=10,
                  justify="right", bg="Powder blue").place(relx=0.3, y=400)

dip = Label(root, text="DIPPING OIL:", bg="turquoise", font="Arial 15").place(relx=0.0, y=450)
dip_entr = Entry(root, font="arial 15", textvariable=dipqty, width=7,
                 justify="right", bg="Powder blue").place(relx=0.1, y=450)
dipr_ate = Entry(root, font="arial 15", textvariable=diprate, width=7,
                 justify="right", bg="Powder blue").place(relx=0.2, y=450)
dip_disp = Entry(root, font="arial 15", textvariable=dipdisp, width=10,
                 justify="right", bg="Powder blue").place(relx=0.3, y=450)

carb32 = Label(root, text="CARBONATE:", bg="turquoise", font="Arial 15").place(relx=0.0, y=500)
carb_qty = Entry(root, font="arial 15", textvariable=carbqty, width=7,
                 justify="right", bg="Powder blue").place(relx=0.1, y=500)
carb_rate = Entry(root, font="arial 15", textvariable=carbrate, width=7,
                  justify="right", bg="Powder blue").place(relx=0.2, y=500)
carb_disp = Entry(root, font="arial 15", textvariable=carbdisp, width=10,
                  justify="right", bg="Powder blue").place(relx=0.3, y=500)

subtot = Entry(root, font="Arial 15", textvariable=subt_var, width=10,
               justify="right", bg="Powder blue").place(relx=0.3, y=550)

subt_var.set("0")

TOTAL = Entry(root, font="arial 18  bold", textvariable=total_rate, bg="white",
              justify="right", width=13).place(relx=0.3, rely=0.8)

ref = Entry(root, font="arial 18", textvariable=refer_var, bg="powder blue",
            width=10, justify="right").place(relx=0.8, rely=0.0)
town = Entry(root, font="arial 18", textvariable=town_var, bg="powder blue",
             width=15).place(relx=0.6, rely=0.1)
############################SET###############################
washrate.set("0")
washent.set("0")
nettgrate.set("0")
nettgqnt.set("0")
taperate.set("0")
tapeqty.set("0")
boxqty.set("0")
boxrate.set("0")
nettdisp.set("0")
washdisp.set("0")
boxdisp.set("0")
tapedisp.set("0")
total_rate.set("0")
subt_var.set("0")
caryqty.set("0")
caryrate.set("0")
carydisp.set("0")
dipqty.set("0")
diprate.set("0")
dipdisp.set("0")
carbqty.set("0")
carbrate.set("0")
carbdisp.set("0")
############################Buttons###########################

total = Button(root, text="TOTAL", bg="powder blue", fg="red", font="arial 18 bold",
               command=total_bill, width=6).place(relx=0.2, y=540)

Submit = Button(root, text="SUBMIT", bg="powder blue", fg="red", font="arial 20 bold",
                command=submit_data, width=14).place(x=1000, rely=0.8)

clear = Button(root, text="RESET", bg="powder blue", fg="red", font="arial 20 bold", width=14,
               command=btnreset).place(x=1000, y=520)

############################## Wakkal #########################

def enter():
	# wakno1
	no1 = int(wakno1.get())
	no2 = int(wakno2.get())
	no3 = int(wakno3.get())
	no4 = int(wakno4.get())
	no5 = int(wakno5.get())
	no6 = int(wakno6.get())
	no7 = int(wakno7.get())
	no8 = int(wakno8.get())
	no9 = int(wakno9.get())
	no10 = int(wakno10.get())
	# ntt=str('%.2f'%nttt)
	bo_tot = no1 + no2 + no3 + no4 + no5 + no6 + no7 + no8 + no9 + no10
	bo_toto = str('%d' % bo_tot)
	wakno.set(bo_toto)

wak1 = StringVar()
wak2 = StringVar()
wak3 = StringVar()
wak4 = StringVar()
wak5 = StringVar()
wak6 = StringVar()
wak7 = StringVar()
wak8 = StringVar()
wak9 = StringVar()
wak10 = StringVar()
wak_tot = StringVar()

wakno1 = StringVar()
wakno2 = StringVar()
wakno3 = StringVar()
wakno4 = StringVar()
wakno5 = StringVar()
wakno6 = StringVar()
wakno7 = StringVar()
wakno8 = StringVar()
wakno9 = StringVar()
wakno10 = StringVar()
wakno = StringVar()
finbl = StringVar()

wak = Label(root, text="   VAKKAL", bg="turquoise", font="Arial 30 bold", fg="BlACK").place(relx=0.5, rely=0.2)
wak_1 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak1).place(x=650, y=200)
wak_2 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak2).place(x=650, y=240)
wak_3 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak3).place(x=650, y=280)
wak_4 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak4).place(x=650, y=320)
wak_5 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak5).place(x=650, y=360)
wak_6 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak6).place(x=650, y=400)
wak_7 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak7).place(x=650, y=440)
wak_8 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak8).place(x=650, y=480)
wak_9 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak9).place(x=650, y=520)
wak_10 = Entry(root, font="arial 18", bg="powder blue", width=10, textvariable=wak10).place(x=650, y=560)

ent_but = Button(root, text="Enter", font="arial 18 bold", bg="powder blue", fg="red", width=10, command=enter).place(
	x=650, y=600)

wak_no1 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno1).place(x=850, y=200)
wak_no2 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno2).place(x=850, y=240)
wak_no3 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno3).place(x=850, y=280)
wak_no4 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno4).place(x=850, y=320)
wak_no5 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno5).place(x=850, y=360)
wak_no6 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno6).place(x=850, y=400)
wak_no7 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno7).place(x=850, y=440)
wak_no8 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno8).place(x=850, y=480)
wak_no9 = Entry(root, font="arial 18", bg="powder blue", width=10,
                justify="right", textvariable=wakno9).place(x=850, y=520)
wak_no10 = Entry(root, font="arial 18", bg="powder blue", width=10,
                 justify="right", textvariable=wakno10).place(x=850, y=560)

wak_tot = Entry(root, font="arial 18 bold", bg="white", width=10,
                justify="right", textvariable=wakno).place(x=850, y=600)

wakno1.set("0")
wakno2.set("0")
wakno3.set("0")
wakno4.set("0")
wakno5.set("0")
wakno6.set("0")
wakno7.set("0")
wakno8.set("0")
wakno9.set("0")
wakno10.set("0")

#################################### RadioButton ###########################################

pad = Radiobutton(root, text="PAID", bg="turquoise", fg="Red", font="arial 20 bold", value=1).place(x=1000, y=200)
unpad = Radiobutton(root, text="UNPAID", bg="turquoise", fg="red", font="arial 20 bold", value=2).place(x=1000, y=240)

##################################### Paid Amount ###########################################


paidamt = StringVar()
paidamt.set("0")
paident = Button(root, text="BILL", font="arial 18 bold", bg="powder blue",
                 fg="red", width=10, command=paidamount).place(x=1000, y=290)
pdamt = Entry(root, font="arial 18 bold", width=8, bg="white", fg="green",
              justify="right", textvariable=paidamt).place(x=1120, y=205)

finalbill = Entry(root, font="arial 18 bold", width=13, bg="black", fg="red",
                  justify="right", textvariable=finbl).place(x=1000, y=350)

##############################################################################################
root.mainloop()