import nidaqmx
import nidaqmx.constants as constants
import numpy as np


class DAQmxChannel:

    def __init__(self, dev, test = 0):

        self.dev = dev
        self.task = nidaqmx.Task()
        if test:  
            self._create_task()
        self.clock_src = ''
        self.clock_edge = constants.Edge.RISING
        self.trig_src = ''
        self.trig_edge = constants.Edge.RISING
        self.cont_buffer_size = 100000000

        self.isTimed = False
        self.read_all_samples = False

        self.grouping_mode = constants.GroupBy.CHANNEL

    def _create_task(self):
        self.task = nidaqmx.Task()  # todo: create a task and store the reference

    def reset(self):
        self._clear_task()
        self._create_task()
    
        self.isTimed = False

    def start(self):
        self.task.start()

    def stop(self):
        self.task.stop()
        self.task.task_control(nidaqmx.constants.TaskControl.UNRESERVE)
    
    def _clear_task(self):
        self.task.close()

    def set_sample_clock(self, src, edge, n):
        self.clock_src = src
        self.clock_edge = edge

        if n < self.cont_buffer_size:
            self.task.timing.cfg_samp_clk_timing(rate=1000, source=src, active_edge=edge, sample_mode=constants.AcquisitionType.FINITE, samps_per_chan=n)
        else:  # Use continuous sampling
            self.task.timing.cfg_samp_clk_timing(rate=1000000, source=src, active_edge=edge, sample_mode=constants.AcquisitionType.CONTINUOUS, samps_per_chan=self.cont_buffer_size)

        self.isTimed = True





    # todo: are the remaining functions necessary?

    '''


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

class DAQmxAnalogInput(DAQmxChannel):

    def __init__(self, dev, minval=-10.0, maxval=+10.0):
        super().__init__(dev)
        self._create_task(dev, minval, maxval)
        self.numchan = len(dev.split(','))

    def _create_task(self, minval=-10.0, maxval=+10.0):
        super()._create_task()
        self.task.ai_channels.add_ai_voltage_chan(self.dev, name_to_assign_to_channel="", min_val="", max_val="" )

    def get_voltage(self):
        readarray = self.get_voltages(1)
        return readarray[0]

    def get_voltages(self, n):
        readarray = np.zeros(self.numchan * n)
        readarray = self.task.read()
        return np.array(readarray)


class DAQmxAnalogOutput(DAQmxChannel):

    def __init__(self, dev, minval=-10, maxval=10):
        super().__init__(dev)
        self._create_task(dev, minval, maxval)

    def _create_task(self, dev, minval=-10, maxval=10):
        super()._create_task()
        self.minval = minval
        self.maxval = maxval

        # nidaqmx does not allow querying the analog output value, so we are keeping track of it in memory
        self.currentVoltage = 0.0
        self.lastSweepVoltage = 0.0
        # todo: call nidaqmx to add physical ai channel according to dev
        self.task.ao_channels.add_ao_voltage_chan(self.dev, name_to_assign_to_channel="", min_val="", max_val="" )
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
