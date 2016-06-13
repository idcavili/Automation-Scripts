def avgRoomAirTemp():
  RATemp = (RATempN + RATempS + RATempE + RATempW) / 4
  calcRAHeat()
  calcRACool()
  updateVAV()

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
  
def calcRACool():
  RACoolPercent = RACoolPID.update(RATemp)
  DACoolTemp = map(RACoolPercent)
  DACoolSP = min(DACoolTemp, DADehumSP)
  DACoolPID.setPoint(DACoolSP)
  calcDACool()
  
def calcDACool():
  DACoolPercent = DACoolPID.update(DACoolSense)
  CWSetPoint = map(DACoolPercent)
  if supplyTemp > DACoolSense:
    ervRatio = 0
    requests.put(cool_valve/valve/pv, DACoolPercent)
  elif supplyTemp <= DACoolSense & supplyTemp > DACoolSP:
    ervRatio = 100
    requests.put(cool_valve/valve/pv, DACoolPercent)
  elif supplyTemp <= DACoolSP:
    ervRatio = DACoolPercent
    requests.put(cool_valve/valve/pv, 0)

