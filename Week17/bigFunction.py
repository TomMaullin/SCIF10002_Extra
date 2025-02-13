import numpy as np
import warnings
warnings.filterwarnings("ignore")

#=================================================================================================================================
# About this function:
#
# NEVER code like this! This code is deliberately ambiguous because it is part of an exercise. It also turns off warnings which
# really you should not do. If you code like this people will not like you.
#=================================================================================================================================

def getxy(t):
	x = ((-7/48*np.sin(10/11 - 14*t) + 2540/7*np.sin(t + 49/29) + 809/23*np.sin(2*t + 25/13) + 285/31*np.sin(3*t + 177/106) + 91/8*np.sin(4*t + 70/29) + 103/23*np.sin(5*t + 44/27) + 40/11*np.sin(6*t + 140/37) + 16/3*np.sin(7*t + 33/16) + 30/11*np.sin(8*t + 60/13) + 227/85*np.sin(9*t + 91/44) + 110/47*np.sin(10*t + 26/7) + 29/22*np.sin(11*t + 45/37) + 52/33*np.sin(12*t + 89/24) + 14/25*np.sin(13*t + 135/52) + 56/41*np.sin(15*t + 122/35) + 4/21*np.sin(16*t + 208/89) + 149/20)*np.heaviside(95*np.pi - t,1)*np.heaviside(t - 91*np.pi,1) + (-46/19*np.sin(14/25 - 2*t) + 264/23*np.sin(t + 1/10) + 125/29*np.sin(3*t + 11/25) + 85/23*np.sin(4*t + 72/23) + 122/43*np.sin(5*t + 15/23) + 377/32*np.sin(6*t + 83/18) + 169/24*np.sin(7*t + 42/23) + 52/15*np.sin(8*t + 37/33) + 407/27*np.sin(9*t + 27/29) + 35/8*np.sin(10*t + 55/31) + 33/17*np.sin(11*t + 109/29) + 193/46*np.sin(12*t + 13/16) - 10560/59)*np.heaviside(91*np.pi - t,1)*np.heaviside(t - 87*np.pi,1) + (-19/24*np.sin(9/19 - 11*t) - 139/29*np.sin(11/26 - 9*t) - 103/6*np.sin(21/20 - 6*t) - 785/112*np.sin(8/15 - 2*t) + 75/34*np.sin(t + 14/33) + 79/38*np.sin(3*t + 27/46) + 313/87*np.sin(4*t + 17/24) + 65/22*np.sin(5*t + 152/35) + 266/71*np.sin(7*t + 139/44) + 118/45*np.sin(8*t + 117/28) + 23/19*np.sin(10*t + 64/33) + 82/33*np.sin(12*t + 75/31) + 1527/13)*np.heaviside(87*np.pi - t,1)*np.heaviside(t - 83*np.pi,1) + (-44/21*np.sin(3/8 - 9*t) - 1370/457*np.sin(43/47 - 8*t) - 173/20*np.sin(13/32 - 5*t) + 7375/42*np.sin(t + 1653/826) + 3902/53*np.sin(2*t + 49/37) + 3229/190*np.sin(3*t + 211/66) + 127/13*np.sin(4*t + 181/63) + 1169/292*np.sin(6*t + 97/35) + 35/24*np.sin(7*t + 261/112) + 53/17*np.sin(10*t + 43/13) + 123/29*np.sin(11*t + 3/17) + 80/29*np.sin(12*t + 36/11) + 16667/36)*np.heaviside(83*np.pi - t,1)*np.heaviside(t - 79*np.pi,1) + (-22/15*np.sin(5/16 - 11*t) - 1244/113*np.sin(27/20 - 5*t) - 127/15*np.sin(1/7 - 4*t) - 261/10*np.sin(15/16 - 2*t) + 1657/20*np.sin(t + 167/41) + 292/23*np.sin(3*t + 66/17) + 234/31*np.sin(6*t + 266/69) + 173/27*np.sin(7*t + 73/16) + 111/29*np.sin(8*t + 71/28) + 31/13*np.sin(9*t + 85/32) + 3/4*np.sin(10*t + 236/51) + 21/23*np.sin(12*t + 106/23) - 19200/37)*np.heaviside(79*np.pi - t,1)*np.heaviside(t - 75*np.pi,1) + (-34/41*np.sin(42/37 - 12*t) + 7208/61*np.sin(t + 139/93) + 195/23*np.sin(2*t + 91/33) + 86/11*np.sin(3*t + 65/33) + 79/27*np.sin(4*t + 199/99) + 253/28*np.sin(5*t + 47/33) + 43/33*np.sin(6*t + 7/2) + 107/30*np.sin(7*t + 73/61) + 21/31*np.sin(8*t + 120/37) + 68/35*np.sin(9*t + 34/21) + 15/53*np.sin(10*t + 68/21) + 104/41*np.sin(11*t + 29/40) + 29/40*np.sin(13*t + 23/19) + 16/45*np.sin(14*t + 155/37) + 9/14*np.sin(15*t + 435/218) - 277/35)*np.heaviside(75*np.pi - t,1)*np.heaviside(t - 71*np.pi,1) + (1826/43*np.sin(t + 49/59) + 232/65*np.sin(2*t + 25/34) + 11627/31)*np.heaviside(71*np.pi - t,1)*np.heaviside(t - 67*np.pi,1) + (1241/19*np.sin(t + 69/59) + 214/71*np.sin(2*t + 31/23) + 64/35*np.sin(3*t + 56/13) + 61/27*np.sin(4*t + 62/53) + 1062/29)*np.heaviside(67*np.pi - t,1)*np.heaviside(t - 63*np.pi,1) + (12307/142*np.sin(t + 7/6) + 227/31*np.sin(2*t + 129/28) + 355/32*np.sin(3*t + 46/43) + 109/33*np.sin(4*t + 136/37) + 85/21*np.sin(5*t + 27/34) + 135/41*np.sin(6*t + 71/20) + 90/41*np.sin(7*t + 26/27) + 83/36*np.sin(8*t + 83/25) + 34/23*np.sin(9*t + 17/21) + 25/13*np.sin(10*t + 107/34) + 13/18*np.sin(11*t + 17/24) + 49/27*np.sin(12*t + 60/19) + 324)*np.heaviside(63*np.pi - t,1)*np.heaviside(t - 59*np.pi,1) + (-18/23*np.sin(17/11 - 12*t) - 16/19*np.sin(6/29 - 9*t) - 4/13*np.sin(26/17 - 7*t) - 250/51*np.sin(77/54 - 6*t) - 206/27*np.sin(26/51 - 4*t) - 49/2*np.sin(16/31 - 2*t) + 3718/23*np.sin(t + 10/9) + 199/8*np.sin(3*t + 25/21) + 245/29*np.sin(5*t + 58/49) + 55/13*np.sin(8*t + 178/41) + 118/47*np.sin(10*t + 73/16) + 19/16*np.sin(11*t + 437/438) + 26/37*np.sin(13*t + 22/15) + 26/41*np.sin(14*t + 45/11) + 1/26*np.sin(15*t + 65/54) - 128/3)*np.heaviside(59*np.pi - t,1)*np.heaviside(t - 55*np.pi,1) + (-56/9*np.sin(17/35 - 26*t) - 171/44*np.sin(29/26 - 23*t) - 98/25*np.sin(29/26 - 19*t) - 224/23*np.sin(34/61 - 12*t) - 6397/43*np.sin(15/19 - 7*t) - 737/13*np.sin(33/49 - 6*t) - 764/27*np.sin(15/14 - 2*t) + 13798/35*np.sin(t + 77/38) + 3989/20*np.sin(3*t + 1/84) + 356/19*np.sin(4*t + 55/26) + 2183/30*np.sin(5*t + 255/56) + 442/21*np.sin(8*t + 82/33) + 1092/43*np.sin(9*t + 33/46) + 587/52*np.sin(10*t + 4/19) + 174/5*np.sin(11*t + 65/21) + 1411/94*np.sin(13*t + 73/20) + 129/13*np.sin(14*t + 5/4) + 231/29*np.sin(15*t + 2/29) + 149/15*np.sin(16*t + 45/16) + 519/67*np.sin(17*t + 73/19) + 73/53*np.sin(18*t + 71/16) + 153/53*np.sin(20*t + 4) + 283/41*np.sin(21*t + 3/26) + 73/23*np.sin(22*t + 31/18) + 87/22*np.sin(24*t + 5/33) + 190/29*np.sin(25*t + 27/7) + 57/16*np.sin(27*t + 3/2) + 151/39*np.sin(28*t + 1190/397) + 199/50*np.sin(29*t + 26/33) - 5967/56)*np.heaviside(55*np.pi - t,1)*np.heaviside(t - 51*np.pi,1) + (-6/35*np.sin(13/18 - 11*t) - 9/13*np.sin(9/23 - 9*t) - 47/34*np.sin(23/29 - 7*t) - 98/37*np.sin(37/32 - 5*t) - 115/14*np.sin(44/41 - 3*t) - 39/41*np.sin(15/23 - 2*t) - 2179/21*np.sin(48/35 - t) + 23/25*np.sin(4*t + 7/12) + 41/37*np.sin(6*t + 43/31) + 24/25*np.sin(8*t + 59/30) + 15/19*np.sin(10*t + 45/19) + 62/123*np.sin(12*t + 39/16) - 9717/53)*np.heaviside(51*np.pi - t,1)*np.heaviside(t - 47*np.pi,1) + (2617/50*np.sin(t + 59/46) + 101/40*np.sin(2*t + 55/24) + 64/17*np.sin(3*t + 135/32) + 28/45*np.sin(4*t + 18/17) + 6361/49)*np.heaviside(47*np.pi - t,1)*np.heaviside(t - 43*np.pi,1) + (2662/35*np.sin(t + 25/29) + 71/13*np.sin(2*t + 52/25) + 219/41*np.sin(3*t + 121/35) + 53/19*np.sin(4*t + 20/29) + 73/26*np.sin(5*t + 52/17) + 3923/28)*np.heaviside(43*np.pi - t,1)*np.heaviside(t - 39*np.pi,1) + (-22/21*np.sin(22/51 - 4*t) + 1408/19*np.sin(t + 23/21) + 48/29*np.sin(2*t + 40/31) + 33/19*np.sin(3*t + 95/23) + 18/31*np.sin(5*t + 33/14) - 6441/35)*np.heaviside(39*np.pi - t,1)*np.heaviside(t - 35*np.pi,1) + (1659/17*np.sin(t + 24/41) + 59/17*np.sin(2*t + 15/29) + 48/11*np.sin(3*t + 80/31) + 2/25*np.sin(4*t + 80/159) - 5771/31)*np.heaviside(35*np.pi - t,1)*np.heaviside(t - 31*np.pi,1) + (-132/41*np.sin(3/37 - 12*t) - 123/40*np.sin(47/31 - 7*t) - 63/11*np.sin(49/32 - 5*t) - 130/7*np.sin(12/13 - 2*t) + 7294/15*np.sin(t + 41/39) + 816/43*np.sin(3*t + 5/21) + 299/24*np.sin(4*t + 103/36) + 59/8*np.sin(6*t + 19/21) + 67/45*np.sin(8*t + 7/38) + 75/13*np.sin(9*t + 155/36) + 41/10*np.sin(10*t + 38/53) + 67/18*np.sin(11*t + 42/13) - 2071/13)*np.heaviside(31*np.pi - t,1)*np.heaviside(t - 27*np.pi,1) + (-769/71*np.sin(1/91 - 13*t) - 365/21*np.sin(43/31 - 12*t) - 1033/53*np.sin(22/35 - 7*t) - 1459/29*np.sin(15/29 - 6*t) - 1023/14*np.sin(16/11 - 4*t) - 685/8*np.sin(37/30 - t) + 1145/13*np.sin(2*t + 61/39) + 382/27*np.sin(3*t + 55/16) + 3185/54*np.sin(5*t + 25/22) + 1485/31*np.sin(8*t + 409/102) + 809/41*np.sin(9*t + 77/24) + 816/53*np.sin(10*t + 78/19) + 197/23*np.sin(11*t + 269/62) + 104/19*np.sin(14*t + 15/41) + 245/37*np.sin(15*t + 109/54) + 120/29*np.sin(16*t + 45/28) + 112/27*np.sin(17*t + 17/31) + 13/9*np.sin(18*t + 13/16) + 159/40*np.sin(19*t + 47/24) + 17/26*np.sin(20*t + 116/35) + 53/12*np.sin(21*t + 42/83) + 56774/117)*np.heaviside(27*np.pi - t,1)*np.heaviside(t - 23*np.pi,1) + (-27/17*np.sin(39/40 - 19*t) - 76/29*np.sin(682/681 - 11*t) - 179/9*np.sin(29/27 - 5*t) - 3509/28*np.sin(29/23 - 2*t) - 2092/17*np.sin(10/23 - t) + 3427/39*np.sin(3*t + 13/14) + 1106/41*np.sin(4*t + 111/29) + 336/23*np.sin(6*t + 127/35) + 1051/73*np.sin(7*t + 51/26) + 203/32*np.sin(8*t + 37/31) + 37/5*np.sin(9*t + 13/43) + 121/19*np.sin(10*t + 19/10) + 249/125*np.sin(12*t + 100/31) + 17/40*np.sin(13*t + 83/69) + 101/37*np.sin(14*t + 159/68) + 51/28*np.sin(15*t + 14/19) + 20/9*np.sin(16*t + 19/28) + 19/24*np.sin(17*t + 123/47) + 11/13*np.sin(18*t + 50/151) + 25/38*np.sin(20*t + 22/17) - 23965/43)*np.heaviside(23*np.pi - t,1)*np.heaviside(t - 19*np.pi,1) + (-46/39*np.sin(11/27 - 3*t) + 3379/18*np.sin(t + 47/32) + 153/19*np.sin(2*t + 54/35) + 327/77*np.sin(4*t + 21/17) + 104/33*np.sin(5*t + 118/29) + 100/29*np.sin(6*t + 31/33) + 118/41*np.sin(7*t + 124/33) + 5455/101)*np.heaviside(19*np.pi - t,1)*np.heaviside(t - 15*np.pi,1) + (-37/21*np.sin(13/40 - 15*t) - 67/33*np.sin(10/13 - 12*t) - 869/290*np.sin(4/3 - 11*t) - 388/31*np.sin(109/78 - 5*t) - 411/38*np.sin(14/25 - 3*t) + 6756/23*np.sin(t + 70/93) + 725/31*np.sin(2*t + 190/69) + 573/46*np.sin(4*t + 43/40) + 56/45*np.sin(6*t + 81/35) + 31/9*np.sin(7*t + 142/43) + 72/35*np.sin(8*t + 32/23) + 61/11*np.sin(9*t + 9/13) + 25/31*np.sin(10*t + 13/48) + 85/29*np.sin(13*t + 29/24) + 22/25*np.sin(14*t + 21/29) + 35/27*np.sin(16*t + 12/73) + 9/7*np.sin(17*t + 77/19) + 6/37*np.sin(18*t + 73/18) + 909/34)*np.heaviside(15*np.pi - t,1)*np.heaviside(t - 11*np.pi,1) + (20189/113*np.sin(t + 207/52) + 201/25*np.sin(2*t + 21/26) + 180/47*np.sin(3*t + 159/50) + 158/41*np.sin(4*t + 2/35) - 1106/47)*np.heaviside(11*np.pi - t,1)*np.heaviside(t - 7*np.pi,1) + (-39/68*np.sin(7/12 - 12*t) - 1/2*np.sin(70/69 - 10*t) - 905/78*np.sin(9/22 - 5*t) - 822/23*np.sin(20/23 - 3*t) - 14600/43*np.sin(55/41 - t) + 9/11*np.sin(2*t + 37/15) + 24/71*np.sin(4*t + 173/65) + 1/3*np.sin(6*t + 133/37) + 436/83*np.sin(7*t + 3/40) + 11/37*np.sin(8*t + 159/35) + 79/26*np.sin(9*t + 28/47) + 88/49*np.sin(11*t + 49/44) - 3013/35)*np.heaviside(7*np.pi - t,1)*np.heaviside(t - 3*np.pi,1) + (-291/13*np.sin(20/23 - 3*t) - 703/33*np.sin(1/517 - 2*t) + 18020/37*np.sin(t + 50/57) + 122/23*np.sin(4*t + 59/18) + 318/35*np.sin(5*t + 169/46) + 115/22*np.sin(6*t + 59/35) + 68/39*np.sin(7*t + 79/31) + 161/37*np.sin(8*t + 17/22) + 107/33*np.sin(9*t + 143/31) + 34/25*np.sin(10*t + 41/42) + 84/37*np.sin(11*t + 269/67) + 65/42*np.sin(12*t + 390/389) - 4625/29)*np.heaviside(3*np.pi - t,1)*np.heaviside(t + np.pi,1))*np.heaviside(np.sqrt(np.sign(np.sin(t/2))),1)
	y = ((-191/106*np.sin(10/9 - 9*t) + 2661/67*np.sin(t + 25/28) + 3358/101*np.sin(2*t + 35/16) + 1875/32*np.sin(3*t + 39/25) + 535/29*np.sin(4*t + 216/47) + 477/17*np.sin(5*t + 41/25) + 133/39*np.sin(6*t + 51/13) + 119/20*np.sin(7*t + 22/13) + 265/43*np.sin(8*t + 93/47) + 91/18*np.sin(10*t + 62/27) + 102/73*np.sin(11*t + 35/36) + 81/101*np.sin(12*t + 38/11) + 134/37*np.sin(13*t + 117/50) + 17/25*np.sin(14*t + 51/11) + 19/11*np.sin(15*t + 56/23) + 43/38*np.sin(16*t + 175/117) - 8893/19)*np.heaviside(95*np.pi - t,1)*np.heaviside(t - 91*np.pi,1) + (-237/35*np.sin(21/22 - 11*t) - 2723/190*np.sin(5/36 - 6*t) - 37/18*np.sin(23/26 - 2*t) + 290/23*np.sin(t + 83/39) + 215/41*np.sin(3*t + 66/23) + 207/50*np.sin(4*t + 131/34) + 113/20*np.sin(5*t + 39/41) + 43/5*np.sin(7*t + 48/13) + 308/67*np.sin(8*t + 71/29) + 105/4*np.sin(9*t + 79/32) + 273/34*np.sin(10*t + 43/14) + 209/25*np.sin(12*t + 45/19) + 17847/29)*np.heaviside(91*np.pi - t,1)*np.heaviside(t - 87*np.pi,1) + (-267/37*np.sin(15/28 - 7*t) - 206/29*np.sin(10/27 - 5*t) - 287/34*np.sin(1/11 - t) + 193/37*np.sin(2*t + 37/22) + 309/50*np.sin(3*t + 47/21) + 671/67*np.sin(4*t + 38/11) + 753/25*np.sin(6*t + 16/33) + 75/41*np.sin(8*t + 52/21) + 156/35*np.sin(9*t + 11/20) + 123/37*np.sin(10*t + 38/11) + 115/33*np.sin(11*t + 20/33) + 31/11*np.sin(12*t + 28/9) + 12552/19)*np.heaviside(87*np.pi - t,1)*np.heaviside(t - 83*np.pi,1) + (-77/38*np.sin(17/59 - 12*t) - 105/29*np.sin(18/25 - 10*t) - 407/29*np.sin(28/25 - 3*t) + 8407/97*np.sin(t + 177/46) + 819/11*np.sin(2*t + 51/22) + 265/19*np.sin(4*t + 59/33) + 626/29*np.sin(5*t + 44/13) + 1811/151*np.sin(6*t + 137/30) + 83/18*np.sin(7*t + 22/17) + 124/71*np.sin(8*t + 73/20) + 127/31*np.sin(9*t + 21/5) + 99/38*np.sin(11*t + 21/19) + 1976/9)*np.heaviside(83*np.pi - t,1)*np.heaviside(t - 79*np.pi,1) + (-37/29*np.sin(4/25 - 11*t) - 103/44*np.sin(30/59 - 7*t) - 148/49*np.sin(63/62 - 5*t) - 1089/19*np.sin(34/39 - t) + 6598/91*np.sin(2*t + 65/38) + 176/29*np.sin(3*t + 17/27) + 184/37*np.sin(4*t + 123/38) + 103/15*np.sin(6*t + 11/37) + 106/25*np.sin(8*t + 159/44) + 15/4*np.sin(9*t + 89/22) + 83/24*np.sin(10*t + 35/32) + 41/22*np.sin(12*t + 119/30) + 15729/29)*np.heaviside(79*np.pi - t,1)*np.heaviside(t - 75*np.pi,1) + (-119/46*np.sin(132/131 - 11*t) + 1189/25*np.sin(t + 79/27) + 877/17*np.sin(2*t + 130/29) + 734/37*np.sin(3*t + 43/15) + 355/22*np.sin(4*t + 526/117) + 17/3*np.sin(5*t + 145/72) + 303/22*np.sin(6*t + 25/21) + 89/52*np.sin(7*t + 99/26) + 24/5*np.sin(8*t + 58/13) + 79/45*np.sin(9*t + 67/30) + 77/32*np.sin(10*t + 3/5) + 28/65*np.sin(12*t + 27/53) + 19/29*np.sin(13*t + 80/21) + 58/49*np.sin(14*t + 51/14) + 11/24*np.sin(15*t + 71/28) + 34459/33)*np.heaviside(75*np.pi - t,1)*np.heaviside(t - 71*np.pi,1) + (-78/77*np.sin(10/11 - 2*t) - 4118/79*np.sin(37/33 - t) - 1199/39)*np.heaviside(71*np.pi - t,1)*np.heaviside(t - 67*np.pi,1) + (-3/2*np.sin(13/24 - 4*t) - 73/27*np.sin(17/21 - 3*t) - 31/12*np.sin(6/5 - 2*t) - 626/11*np.sin(7/13 - t) - 8873/39)*np.heaviside(67*np.pi - t,1)*np.heaviside(t - 63*np.pi,1) + (-28/17*np.sin(13/29 - 11*t) - 96/43*np.sin(25/74 - 9*t) - 157/48*np.sin(11/27 - 7*t) - 229/37*np.sin(13/20 - 5*t) - 479/33*np.sin(19/20 - 3*t) - 70/27*np.sin(65/49 - 2*t) - 7049/52*np.sin(35/27 - t) + 19/15*np.sin(4*t + 90/37) + 64/41*np.sin(6*t + 91/33) + 27/20*np.sin(8*t + 55/21) + 83/62*np.sin(10*t + 31/12) + 25/18*np.sin(12*t + 64/23) + 520/23)*np.heaviside(63*np.pi - t,1)*np.heaviside(t - 59*np.pi,1) + (-7/10*np.sin(7/43 - 9*t) - 16/23*np.sin(37/51 - 5*t) - 94/9*np.sin(16/19 - 3*t) - 401/29*np.sin(2/35 - 2*t) - 5189/23*np.sin(24/19 - t) + 205/31*np.sin(4*t + 45/58) + 103/41*np.sin(6*t + 24/17) + 133/67*np.sin(7*t + 76/17) + 73/37*np.sin(8*t + 83/36) + 51/44*np.sin(10*t + 30/17) + 49/44*np.sin(11*t + 76/59) + 8/5*np.sin(12*t + 43/32) + 23/52*np.sin(13*t + 147/88) + np.sin(14*t + 97/58) + 6/19*np.sin(15*t + 61/14) - 615/7)*np.heaviside(59*np.pi - t,1)*np.heaviside(t - 55*np.pi,1) + (-32/27*np.sin(50/51 - 25*t) - 354/31*np.sin(2/13 - 24*t) - 149/28*np.sin(15/13 - 21*t) - 501/26*np.sin(12/35 - 18*t) - 113/14*np.sin(44/31 - 17*t) - 1063/80*np.sin(10/23 - 16*t) - 854/39*np.sin(33/50 - 15*t) - 2097/20*np.sin(27/31 - 3*t) + 16563/34*np.sin(t + 115/32) + 10150/51*np.sin(2*t + 11/20) + 691/28*np.sin(4*t + 104/49) + 5699/35*np.sin(5*t + 129/31) + 463/10*np.sin(6*t + 37/20) + 432/17*np.sin(7*t + 52/105) + 706/25*np.sin(8*t + 19/14) + 1093/15*np.sin(9*t + 91/25) + 298/41*np.sin(10*t + 41/24) + 1123/24*np.sin(11*t + 83/30) + 2189/134*np.sin(12*t + 202/55) + 421/24*np.sin(13*t + 63/20) + 198/23*np.sin(14*t + 37/25) + 167/13*np.sin(19*t + 257/79) + 89/24*np.sin(20*t + 13/6) + 115/17*np.sin(22*t + 1/24) + 491/82*np.sin(23*t + 59/15) + 88/19*np.sin(26*t + 23/21) + 45/14*np.sin(27*t + 66/25) + 259/43*np.sin(28*t + 19/41) + 145/72*np.sin(29*t + 27/14) - 15675/23)*np.heaviside(55*np.pi - t,1)*np.heaviside(t - 51*np.pi,1) + (-329/72*np.sin(15/26 - 4*t) - 122/7*np.sin(19/13 - 2*t) + 757/33*np.sin(t + 13/45) + 265/37*np.sin(3*t + 23/36) + 101/32*np.sin(5*t + 46/55) + 41/27*np.sin(6*t + 35/88) + 39/23*np.sin(7*t + 16/17) + 18/31*np.sin(8*t + 77/24) + 7/6*np.sin(9*t + 12/11) + 2/13*np.sin(10*t + 53/14) + 11/24*np.sin(11*t + 38/33) + 7/22*np.sin(12*t + 59/16) + 139393/201)*np.heaviside(51*np.pi - t,1)*np.heaviside(t - 47*np.pi,1) + (-1790/23*np.sin(7/33 - t) + 25/21*np.sin(2*t + 186/41) + 128/29*np.sin(3*t + 125/48) + 53/46*np.sin(4*t + 16/27) + 36850/57)*np.heaviside(47*np.pi - t,1)*np.heaviside(t - 43*np.pi,1) + (-67/13*np.sin(24/37 - 4*t) - 47/24*np.sin(4/17 - 3*t) - 1093/12*np.sin(24/29 - t) + 1968/281*np.sin(2*t + 100/23) + 89/78*np.sin(5*t + 41/28) + 19528/31)*np.heaviside(43*np.pi - t,1)*np.heaviside(t - 39*np.pi,1) + (-35/38*np.sin(28/27 - 2*t) - 960/13*np.sin(33/83 - t) + 47/33*np.sin(3*t + 296/87) + 50/27*np.sin(4*t + 2/11) + 9/13*np.sin(5*t + 222/89) + 14327/24)*np.heaviside(39*np.pi - t,1)*np.heaviside(t - 35*np.pi,1) + (-49/16*np.sin(25/39 - 4*t) - 271/65*np.sin(23/25 - 2*t) - 3790/33*np.sin(29/31 - t) + 15/4*np.sin(3*t + 41/23) + 18911/33)*np.heaviside(35*np.pi - t,1)*np.heaviside(t - 31*np.pi,1) + (-119/29*np.sin(53/38 - 12*t) - 73/30*np.sin(1/106 - 10*t) - 1461/127*np.sin(10/61 - 6*t) - 506/27*np.sin(35/31 - 3*t) - 509/9*np.sin(24/37 - 2*t) - 23306/71*np.sin(25/39 - t) + 293/50*np.sin(4*t + 23/20) + 597/40*np.sin(5*t + 83/29) + 152/17*np.sin(7*t + 13/8) + 118/29*np.sin(8*t + 170/39) + 133/34*np.sin(9*t + 137/39) + 95/16*np.sin(11*t + 54/25) + 8357/18)*np.heaviside(31*np.pi - t,1)*np.heaviside(t - 27*np.pi,1) + (-262/31*np.sin(23/19 - 16*t) - 612/89*np.sin(67/48 - 15*t) - 1589/67*np.sin(5/13 - 6*t) - 1033/19*np.sin(1/75 - 4*t) + 2851/16*np.sin(t + 15/23) + 1471/10*np.sin(2*t + 48/11) + 2326/47*np.sin(3*t + 26/37) + 223/6*np.sin(5*t + 138/53) + 1529/32*np.sin(7*t + 4/25) + 182/23*np.sin(8*t + 91/50) + 218/51*np.sin(9*t + 243/146) + 898/63*np.sin(10*t + 21/11) + 306/23*np.sin(11*t + 55/12) + 260/23*np.sin(12*t + 240/241) + 109/22*np.sin(13*t + 58/35) + 350/43*np.sin(14*t + 3/11) + 119/64*np.sin(17*t + 122/33) + 56/13*np.sin(18*t + 31/18) + 74/27*np.sin(19*t + 13/38) + 87/25*np.sin(20*t + 75/29) + 41/15*np.sin(21*t + 81/32) + 12539/22)*np.heaviside(27*np.pi - t,1)*np.heaviside(t - 23*np.pi,1) + (-101/21*np.sin(17/32 - 16*t) - 35/34*np.sin(17/19 - 15*t) - 64/5*np.sin(45/34 - 9*t) - 71/17*np.sin(22/39 - 8*t) - 4913/89*np.sin(23/25 - 3*t) + 7057/32*np.sin(t + 627/157) + 1545/17*np.sin(2*t + 53/16) + 236/21*np.sin(4*t + 65/16) + 377/41*np.sin(5*t + 45/14) + 539/27*np.sin(6*t + 10/11) + 408/49*np.sin(7*t + 37/20) + 49/6*np.sin(10*t + 19/35) + 149/39*np.sin(11*t + 77/17) + 82/39*np.sin(12*t + 122/33) + 129/40*np.sin(13*t + 193/50) + 55/31*np.sin(14*t + 63/34) + 105/37*np.sin(17*t + 118/29) + 29/11*np.sin(18*t + 59/18) + 16/5*np.sin(19*t + 37/12) + 160/59*np.sin(20*t + 19/27) - 25342/45)*np.heaviside(23*np.pi - t,1)*np.heaviside(t - 19*np.pi,1) + (-130/33*np.sin(5/41 - 6*t) - 115/8*np.sin(1/8 - 2*t) - 1674/11*np.sin(2/23 - t) + 75/19*np.sin(3*t + 105/31) + 144/31*np.sin(4*t + 1/55) + 198/43*np.sin(5*t + 64/19) + 57/22*np.sin(7*t + 91/32) + 24873/61)*np.heaviside(19*np.pi - t,1)*np.heaviside(t - 15*np.pi,1) + (-8/27*np.sin(4/45 - 18*t) - 44/45*np.sin(19/13 - 14*t) - 184/31*np.sin(13/25 - 9*t) - 118/35*np.sin(5/19 - 7*t) - 3471/53*np.sin(8/29 - t) + 5861/59*np.sin(2*t + 5/44) + 963/25*np.sin(3*t + 165/38) + 1567/165*np.sin(4*t + 149/34) + 350/37*np.sin(5*t + 33/13) + 346/41*np.sin(6*t + 61/27) + 47/27*np.sin(8*t + 27/16) + 65/11*np.sin(10*t + 59/23) + 299/49*np.sin(11*t + 87/25) + 61/37*np.sin(12*t + 173/37) + 231/71*np.sin(13*t + 67/23) + 33/31*np.sin(15*t + 385/96) + 16/19*np.sin(16*t + 14/3) + 7/9*np.sin(17*t + 109/26) + 8297/26)*np.heaviside(15*np.pi - t,1)*np.heaviside(t - 11*np.pi,1) + (-164/23*np.sin(34/31 - 4*t) + 2702/19*np.sin(t + 5/2) + 312/31*np.sin(2*t + 75/23) + 527/39*np.sin(3*t + 107/108) + 31261/30)*np.heaviside(11*np.pi - t,1)*np.heaviside(t - 7*np.pi,1) + (-47/41*np.sin(29/24 - 11*t) - 160/59*np.sin(55/38 - 9*t) - 55/18*np.sin(4/21 - 8*t) - 88/29*np.sin(39/31 - 7*t) - 108/19*np.sin(3/7 - 6*t) - 144/25*np.sin(55/42 - 4*t) + 2550/101*np.sin(t + 127/33) + 540/29*np.sin(2*t + 14/3) + 378/55*np.sin(3*t + 80/19) + 62/11*np.sin(5*t + 209/46) + 31/17*np.sin(10*t + 5/18) + 55/48*np.sin(12*t + 23/41) + 38813/52)*np.heaviside(7*np.pi - t,1)*np.heaviside(t - 3*np.pi,1) + (-71/59*np.sin(31/30 - 12*t) - 11/3*np.sin(4/5 - 7*t) + 2195/8*np.sin(t + 90/43) + 5273/48*np.sin(2*t + 107/31) + 1879/39*np.sin(3*t + 38/27) + 33/5*np.sin(4*t + 125/39) + 196/11*np.sin(5*t + 2/31) + 281/28*np.sin(6*t + 136/33) + 350/57*np.sin(8*t + 244/75) + 56/13*np.sin(9*t + 39/31) + 16/11*np.sin(10*t + 334/223) + 58/31*np.sin(11*t + 23/41) + 7100/7)*np.heaviside(3*np.pi - t,1)*np.heaviside(t + np.pi,1))*np.heaviside(np.sqrt(np.sign(np.sin(t/2))),1)
	return(x,y)