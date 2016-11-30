#Python 3
#Created by Abdullah Shuaib on 11/29/16
#for SCoRe through Google Code-In
#Find the Resistance



#Resistor Values (First and second digits of resistance are given by color of first two bands)
FirstandSecondBandValues = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
#Third band's color tells how much to multiply the first two digits
MultiplierValues = {"black":1, "brown":10, "red":100, "orange":1000, "yellow":10000, "green":100000, "blue":1000000, "gold":0.1, "silver":0.01}
#Fourth Band Values tell precision of the resitor
PrecisionValues = {"brown":"+/- 1%","red":"+/- 2%","gold":"+/- 5%", "silver":"+/- 10%", "blank":"+/- 20%"}

def FindResistance(FirstBand,SecondBand,ThirdBand,FourthBand="blank"):
	""" Find Resistance Value of a resistor given the colors of the bands
        FirstBand: string, color of first band
        SecondBand: string, color of second band
        ThirdBand: string, color of third band
        FourthBand: string, color of fourth band, has a default value of blank

        returns a string giving the resistance value of the resistor in ohms with precision
	"""
	FirstBand = str(FirstandSecondBandValues[FirstBand])
	SecondBand = str(FirstandSecondBandValues[SecondBand])
	#Multiplying first two digits with Multiplier(Third Band) convert to string so it can be concatenated with the other strings 
	return(str(int(FirstBand+SecondBand)*MultiplierValues[ThirdBand])+ " ohms " + PrecisionValues[FourthBand])
#Test Statement
print FindResistance("brown","red","silver")
