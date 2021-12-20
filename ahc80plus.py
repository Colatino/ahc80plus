import serial,time

class AHC80plus:
    def __init__(self,address,port,timeout):
        _success=True
        if address<=0 or address>=247:
            print('Address must between 1 and 247')
            _success=False
        if timeout<0:
            print('Timeout must be >= 0 s')
            _success=False
        if _success:
            self._add=address
            self._port=port        
            self._read=[]
            self._timeout=timeout
            self._read_success=False
            self.td=0
            self.tw=0
            self.umi=0
            self.start()
        
    def start(self):
        try:
            self._instrument=serial.Serial(self._port,28800,parity='M')
            self.read()
        except ValueError as e:            
            print(e)
        except serial.SerialException as e:            
            print(e)
        
    def read(self):
        if not self._instrument.is_open:
            self._instrument.open()
        self._read_success=False
        self._instrument.parity='M'
        self._instrument.write(self._add.to_bytes(1,byteorder='big'))
        self._instrument.parity='S'
        self._instrument.write(b' ')
        time.sleep(0.5)
        t0=time.perf_counter()
        t1=t0
        while (self._instrument.in_waiting<48) and (t1-t0<self._timeout):
            t1=time.perf_counter()
            pass
        if t1-t0 > self._timeout:
            print('Connection timed out')
        else:
            self._read=list(self._instrument.read(self._instrument.in_waiting))
            self._read_success=True
            r=self._read
            self.t_dry=(256*r[8]+r[9])/10
            self.t_wet=(256*r[10]+r[11])/10
            self.r_h=(256*r[12]+r[13])/10
        self._instrument.close()
