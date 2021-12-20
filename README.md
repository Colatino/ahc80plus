# The library

This is a simple Python library that uses PySerial to read temperatures (dry and wet bulbs) and relative humidity from a **FullGauge AHC 80 plus controller**.

# Instalation

Just copy the [library](./ahc80plus.py) to your project folder

# Usage example

**Code**
```python
  from ahc80plus import AHC80plus
  
  ahc80=AHC80plus(1,'COM3',1)
  ahc80.read()
  print("Dry temp",ahc80.t_dry,"Wet temp",ahc80.t_wet,"Rel. Hum",ahc80.r_h)  
```

**Output**
```
   Dry temp 27.1 Wet temp 26.8 Rel. Hum 97.0
```

# FullGauge AHC 80 plus

[FullGauge's AHC 80 plus](https://www.fullgauge.com.br/produto-ahc-80-plus) is a relative humidity controller based on the principle of [Psychrometry](https://en.wikipedia.org/wiki/Psychrometrics). Very useful if you want to monitor and control the conditions of a high moisture content room, like a concrete sample curing room, where electronic humidity sensors just won't work reliably or are very expensive due to condensation.

# Dependencies
This code depends on the [PySerial](https://pyserial.readthedocs.io/en/latest/index.html#) library
