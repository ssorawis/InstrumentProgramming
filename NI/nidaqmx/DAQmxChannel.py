import nidaqmx


class DAQmxChannel:

    def __init__(self, dev):

        self.dev = dev
        self._create_task()

    def _create_task(self):
        self.task = None  # todo: create a task and store the reference

    def reset(self):
        pass  # todo: close the task and create a new one

    def start(self):
        pass
        # pydaqmx.DAQmxStartTask(self.th) # todo

    def stop(self):
        pass
        # pydaqmx.DAQmxStopTask(self.th) # todo

    # todo: are the remaining functions necessary?

    '''
    def set_sample_clock(self, src, edge, n):
        self.clock_src = src
        self.clock_edge = edge

        if n < self.cont_buffer_size:
            pydaqmx.DAQmxCfgSampClkTiming(self.th, src, 1000, edge, pydaqmx.DAQmx_Val_FiniteSamps, n)
        else:  # Use continuous sampling
            pydaqmx.DAQmxCfgSampClkTiming(self.th, src, 1000000, edge, pydaqmx.DAQmx_Val_ContSamps, self.cont_buffer_size)

        self.isTimed = True

    def set_int_clock(self, rate, n):
        if n < self.cont_buffer_size:
            pydaqmx.DAQmxCfgSampClkTiming(self.th, 'OnboardClock', rate, pydaqmx.DAQmx_Val_Rising, pydaqmx.DAQmx_Val_FiniteSamps, n)
        else:  # Use continuous sampling
            pydaqmx.DAQmxCfgSampClkTiming(self.th, 'OnboardClock', rate, pydaqmx.DAQmx_Val_Rising, pydaqmx.DAQmx_Val_ContSamps, self.cont_buffer_size)
        self.isTimed = True

    def set_n_sample(self, n):
        if self.clock_src == '':
            print('No Clock Src Assigned')
        else:
            self.setSampleClock(self.clock_src, self.clock_edge, n)

    def set_read_all_samples(self, b):  # This should be named something more like read_only_available_samples
        pydaqmx.DAQmxSetReadReadAllAvailSamp(self.th, b)
        self.read_all_samples = b

    def set_start_trigger(self, src, edge=pydaqmx.DAQmx_Val_Rising):
        pydaqmx.DAQmxCfgDigEdgeStartTrig(self.th, src, edge)

    def set_arm_start_trigger(self, src, edge=pydaqmx.DAQmx_Val_Rising):
        pydaqmx.DAQmxSetArmStartTrigType(self.th,pydaqmx.DAQmx_Val_DigEdge)
        pydaqmx.DAQmxSetDigEdgeArmStartTrigSrc(self.th,src)
        pydaqmx.DAQmxSetDigEdgeArmStartTrigEdge(self.th,edge)

    def set_finite_samples(self, n):
        pydaqmx.DAQmxCfgImplicitTiming(self.th, pydaqmx.DAQmx_Val_FiniteSamps, n)

    def set_retriggerable(self, b):
        pydaqmx.DAQmxSetStartTrigRetriggerable(self.th, b)

    def wait_until_done(self):
        pydaqmx.DAQmxWaitUntilTaskDone(self.th, -1)
    '''

class DAQmxAnalogInput(DAQmxChannel.DAQmxChannel):

    def __init__(self, dev, minval=-10.0, maxval=+10.0):
        super().__init__(dev)
        self._create_task(dev, minval, maxval)
        self.numchan = len(dev.split(','))

    def _create_task(self, minval=-10.0, maxval=+10.0):
        super()._create_task()
        # todo: call nidaqmx to add physical ai channel according to dev
        # pydaqmx.DAQmxCreateAIVoltageChan(self.th, self.dev, '', pydaqmx.DAQmx_Val_Diff, minval, maxval, pydaqmx.DAQmx_Val_Volts, '')

    # todo: are these functions necessary?

    '''
    def get_voltage(self):
        return self.task.read()

    def get_voltages(self, n):
        read = ctypes.c_int32()
        readarray = np.zeros((self.numchan*n,), dtype=np.float64)
        pydaqmx.DAQmxReadAnalogF64(self.th, n, -1, pydaqmx.DAQmx_Val_GroupByChannel, readarray, self.numchan*n, read, None)

        return readarray
    '''

class DAQmxAnalogOutput(DAQmxChannel.DAQmxChannel):

    def __init__(self, dev, minval=-10, maxval=10):
        super().__init__(dev)
        self._create_task(dev, minval, maxval)

    def _create_task(self, dev, minval=-10, maxval=10):
        super().create_task()
        self.minval = minval
        self.maxval = maxval

        # nidaqmx does not allow querying the analog output value, so we are keeping track of it in memory
        self.currentVoltage = 0.0
        self.lastSweepVoltage = 0.0
        # todo: call nidaqmx to add physical ai channel according to dev
        # pydaqmx.DAQmxCreateAOVoltageChan(self.th, self.dev, '', self.minval, self.maxval, pydaqmx.DAQmx_Val_Volts, '')

    # todo: are these functions necessary?
    '''
    def set_voltage(self, v):
        if v < self.minval:
            print('V < Vmin. Setting Vmin')
            self.setVoltage(self.minval)
        elif v > self.maxval:
            print('V > Vmax. Setting Vmax')
            self.setVoltage(self.maxval)
        else:
            autostart = 1
            timeout = -1
            # print(v)
            # print(self.dev)
            pydaqmx.DAQmxWriteAnalogScalarF64(self.th, autostart, timeout, v, None)
            self.currentVoltage = v

    def get_voltage(self):
        return self.currentVoltage

    def set_voltages(self, v):
        if min(v) < self.minval or max(v) > self.maxval:
            print('value out of range')
        else:
            autostart = 0
            timeout = -1
            writeval = ctypes.c_int32()
            pydaqmx.DAQmxWriteAnalogF64(self.th, len(v), autostart, timeout, pydaqmx.DAQmx_Val_GroupByChannel, v, writeval, None)
        self.lastSweepVoltage = v[-1]
    '''
