def avgRoomAirTemp():
  RATemp = (RATempN + RATempS + RATempE + RATempW) / 4
  calcRAHeat()
  calcRACool()

def calcRAHeat():
  RAHeatPercent = RAHeatPID.update(RATemp)
  DAHeatTemp = map(RAHeatPercent)
  DAHeatSP = max(DAHeatTemp, DACoolSP)
  DAHeatPID.setPoint(DAHeatSP)
  calcDAHeat()
  
def calcDAHeat():
  DAHeatPercent = DAHeatPID.update(DAHeatSense)
  HWSetPoint = map(DAHeatPercent)
  requests.put(heat_valve/valve/pv,DAHeatPercent)
