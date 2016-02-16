def avgRoomAirTemp():
  RATemp = (RATempN + RATempS + RATempE + RATempW) / 4

def calcRAHeat():
  RAHeatPercent = RAHeatPID.update(RATemp)
  DAHeatTemp = map(RAHeatPercent)
  DAHeatSP = max(DAHeatTemp, DACoolSP)
  calcDAHeat()
