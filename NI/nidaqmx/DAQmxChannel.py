import nidaqmx
import nidaqmx.constants as constants
import numpy as np
import time


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

    def set_start_trigger(self, src, edge=nidaqmx.constants.Edge.RISING):
        self.task.triggers.start_trigger.cfg_dig_edge_start_trig(source=src, trigger_edge=edge)


    def wait_until_done(self):
        self.task.wait_until_done(timeout=-1)

    def wait_until_done_thd(self, thd):
        daqmx_running = 1
        while daqmx_running != 0 and not thd.cancel:
            try:
                daqmx_running = not self.th.is_task_done()
            except:
                time.sleep(0.01)

        if thd.cancel:
            return 1
        else:
            return 0

class DAQmxAnalogInput(DAQmxChannel):

    def __init__(self, dev, minval=-10.0, maxval=+10.0):
        super().__init__(dev)
        self._create_task(dev, minval, maxval)
        self.numchan = len(dev.split(','))

    def _create_task(self, minval=-10.0, maxval=+10.0):
        super()._create_task()
        self.task.ai_channels.add_ai_voltage_chan(self.dev, min_val=minval, max_val=maxval )

    def get_voltage(self):
        read_voltage = self.task.read(number_of_samples_per_channel=1)
        return read_voltage[0]

    def get_voltages(self, n):
        readarray = np.zeros(self.numchan * n)
        read_voltage = self.task.read(number_of_samples_per_channel=readarray)
        return np.array(read_voltage)


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
        self.task.ao_channels.add_ao_voltage_chan(dev, min_val=self.minval, max_val=self.maxval )

    def set_range(self, minval, maxval):
        self.minval = minval
        self.maxval = maxval
        self._clear_task()
        self._create_task()  

    def set_voltage(self, v):
        if v < self.minval:
            v = self.minval
        elif v > self.maxval:
            v = self.maxval

        self.task.write(v, auto_start=True)

    def set_voltages(self, v):
        if min(v) < self.minval or max(v) > self.maxval:
            print('value out of range')
        else:
            self.task.write(v, auto_start=True)


