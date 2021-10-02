z=None
y='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
x='eng'
w='15'
v=list
m='white'
Za='[-]'
Ya=' is not install on your python'
l=sum
k=round
U=False
T=int
G=range
E=True
D=print
C=len
B=quit
n='''
┌─────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────┐
│ Corsair-Warzone (CorZone)                           │  ▄████████  ▄██████▄     ▄████████  ▄███████▄   ▄██████▄  ███▄▄▄▄      ▄████████ │
│                                                     │ ███    ███ ███    ███   ███    ███ ██▀     ▄██ ███    ███ ███▀▀▀██▄   ███    ███ │
│ Le programme suivant est le corp principale pour la │ ███    █▀  ███    ███   ███    ███       ▄███▀ ███    ███ ███   ███   ███    █▀  │
│ sycronisation des LEDs Corsair avec le jeu Warzone. │ ███        ███    ███  ▄███▄▄▄▄██▀  ▀█▀▄███▀▄▄ ███    ███ ███   ███  ▄███▄▄▄     │
├─────────────────────────────────────────────────────┤ ███        ███    ███ ▀▀███▀▀▀▀▀     ▄███▀   ▀ ███    ███ ███   ███ ▀▀███▀▀▀     │
│ Fonction:                                           │ ███    █▄  ███    ███ ▀███████████ ▄███▀       ███    ███ ███   ███   ███    █▄  │
│   [1] - Détection du décompte de Warzone            │ ███    ███ ███    ███   ███    ███ ███▄     ▄█ ███    ███ ███   ███   ███    ███ │
│   [2] - Etteind les LEDs quand le décompte est a 0  │ ████████▀   ▀██████▀    ███    ███  ▀████████▀  ▀██████▀   ▀█   █▀    ██████████ │
│   [3] - Allume les LEDs dès que la couleur moyenne  │                         ███    ███                                               │
│         de l'écran est à 100 pour le rouge et à 80  │                                                                                  │
│         pour le vert et bleu                        │             _                       ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ██ ▄█▀ │
│   [4] - Change la couleur des LEDs en fonction de la│            | |                     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀     ██▄█▒  │
│         moyenne des couleurs affiché sur l'écran    │            | |__  _   _           ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▓███▄░  │
│   [5] - Une fois dans l'hélicoptère il fait clignoté│            | |_) | |_| |          ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▓██ █▄  │
│         en rouge les LEDs                           │            |_.__/ \__, |          ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ▒██▒ █▄ │
│   [6] - Le programme attend la fin de la cinématique│                    __/ |           ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ▒ ▒▒ ▓▒ │
│         pour remettre les LEDs dans leurs fonctions │                   |___/             ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░   ░ ░▒ ▒░ │
│         précédentes                                 │                                   ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░░ ░  │
└─────────────────────────────────────────────────────┴─────────────────────────────────────────░───────░───░──────░──────░──────░──░────┘
'''
try:import tkinter as b
except:D(f'{Za} "tkinter"{Ya}');B()
try:import win32api as o
except:D(f'{Za} "win32api"{Ya}');B()
try:import win32con as M
except:D(f'{Za} "win32con"{Ya}');B()
try:import pywintypes as p
except:D(f'{Za} "pywintypes"{Ya}');B()
try:from pystray import MenuItem as c;import pystray as q
except:D(f'{Za} "pystray"{Ya}');B()
try:import cv2 as R
except:D(f'{Za} "CV2"{Ya}');B()
try:import time as P
except:D(f'{Za} "time"{Ya}');B()
try:import queue
except:D(f'{Za} "queue"{Ya}');B()
try:import numpy as d
except:D(f'{Za} "Numpy"{Ya}');B()
try:from cuesdk import CueSdk as S
except:D(f'{Za} "cuesdk"{Ya}');B()
try:from threading import Thread as N
except:D(f'{Za} "threading"{Ya}');B()
try:from datetime import datetime
except:D(f'{Za} "datetime"{Ya}');B()
try:from PIL import ImageGrab as V,Image
except:D(f'{Za} "PIL"{Ya}');B()
try:from pytesseract import pytesseract as W
except:D(f'{Za} "pytesseract"{Ya}');B()
D(n)
D('\n[+] Program is start')
F,A0,O=U,E,E
H,I,J=0,0,0
W.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def K():
	B=v();C=A.get_device_count()
	for D in G(C):E=A.get_led_positions_by_device_index(D);B.append(E)
	return B
def e(wave_duration,all_leds,x=0,limit=2):
	D=all_leds;E=2;H=C(D);I=E/wave_duration
	while x<limit:
		if not O:return
		J=T((1-(x-1)**2)*255)
		for F in G(H):
			if not O:return
			B=D[F]
			for K in B:
				if not O:return
				B[K]=J,0,0
			A.set_led_colors_buffer_by_device_index(F,B)
		A.set_led_colors_flush_buffer();P.sleep(E/1000);x+=I
def r():
	e(93.4/3,Q,1)
	while O:e(93.4/3,Q)
def A1(wave_duration,all_leds,x=0,limit=2):
	D=all_leds;E=2;H=C(D);I=E/wave_duration
	while x<limit:
		J=T((1-(x-1)**2)*255)
		for F in G(H):
			B=D[F]
			for K in B:B[K]=J,0,0
			A.set_led_colors_buffer_by_device_index(F,B)
		A.set_led_colors_flush_buffer();P.sleep(E/1000);x+=I
def A2():
	global A,F;A=S();L=A.connect();I=K();D=C(I);F=U
	while E:
		if F:break
		D=C(K())
		for H in G(D):
			B=K()[H]
			for J in B:B[J]=255,255,255
			A.set_led_colors_buffer_by_device_index(H,B);A.set_led_colors_flush_buffer()
def A3():
	global A,F;A=S();Q=A.connect();H=0;M=2;I=K();N=C(I);O=M/50
	while H<1:
		J=T((1-(H-1)**2)*255)
		for D in G(C(I)):
			B=I[D]
			for L in B:B[L]=255-J,255-J,255-J
			A.set_led_colors_buffer_by_device_index(D,B)
		A.set_led_colors_flush_buffer();P.sleep(M/1000);H+=O
	while E:
		if F:break
		N=C(K())
		for D in G(N):
			B=K()[D]
			for L in B:B[L]=0,0,0
			A.set_led_colors_buffer_by_device_index(D,B);A.set_led_colors_flush_buffer()
def f(text):
	try:return T(''.join([A for A in v(text)if A.isnumeric()]))
	except:pass
def X(precision=10):
	B=precision;global H,I,J;K,A=V.grab(),[]
	for L in G(0,1920-1,B):
		for M in G(0,1080-1,B):A.append(K.getpixel((L,M)))
	D=[A[B][0]for B in G(C(A))];E=[A[B][1]for B in G(C(A))];F=[A[B][2]for B in G(C(A))];H=k(l(D)/C(D));I=k(l(E)/C(E));J=k(l(F)/C(F))
def Y():
	global A,F;A=S();O=A.connect();D=K();M=C(D);X()
	while E:
		if F:break
		for L in G(M):
			B=D[L]
			for N in B:B[N]=H,I,J
			A.set_led_colors_buffer_by_device_index(L,B)
		A.set_led_colors_flush_buffer();X()
def s():A=b.Label(text='CORZONE \nby GAME K',font=('Arial Rounded MT Bold',w),fg='#EEEEEE',bg=m);A.master.overrideredirect(E);A.master.geometry('-5-5');A.master.lift();A.master.wm_attributes('-topmost',E);A.master.wm_attributes('-disabled',E);A.master.wm_attributes('-transparentcolor',m);B=p.HANDLE(T(A.master.frame(),16));C=M.WS_EX_COMPOSITED|M.WS_EX_LAYERED|M.WS_EX_NOACTIVATE|M.WS_EX_TOPMOST|M.WS_EX_TRANSPARENT;o.SetWindowLong(B,M.GWL_EXSTYLE,C);A.pack();A.mainloop()
class g:
	def exit_():icon.stop();B()
	def info():A=b.Label(text=n,font=('consolas',w),fg='#000',bg=m);A.master.title('CorZone - Information');A.master.iconbitmap('F:\\Pictures\\Icone\\CorZone.ico');A.master.geometry('+190+300');A.pack();A.mainloop()
def t():D='CorZone';A=Image.open('F:\\Pictures\\Logo\\CorZone.png');B=c('Information',g.info),c('Quit CorZone',g.exit_);C=q.Icon(D,A,D,B);C.run()
N(target=t).start()
A=S()
A4=A.connect()
Q=K()
h=C(Q)
while E:
	Z=V.grab(bbox=(930,200,990,250));L=f(W.image_to_string(R.cvtColor(d.array(Z),R.COLOR_BGR2GRAY),lang=x,config=y))
	if L!=z and L<20:
		i=L
		while E:
			Z=V.grab(bbox=(930,200,990,250));L=f(W.image_to_string(R.cvtColor(d.array(Z),R.COLOR_BGR2GRAY),lang=x,config=y))
			if L!=z:
				if L==i-1:
					P.sleep(L-1);N(target=s).start();N(target=Y).start()
					while H>2 and I>2 and J>2:0
					while H<170 and I<170 and J<170:0
					F=E;h=C(Q)
					for j in G(h):
						a=Q[j]
						for u in a:a[u]=255,255,255
						A.set_led_colors_buffer_by_device_index(j,a);A.set_led_colors_flush_buffer()
					F=U;N(target=Y).start()
					while H>5 and I>5 and J>5:0
					while H<10 and I<10 and J<10:0
					F,O=E,E;N(target=r).start()
					while H<110 and I<110 and J<110:X()
					O=U;F=U;N(target=Y).start();P.sleep(5.5);F=E;B()
				if L==i:0
				else:break