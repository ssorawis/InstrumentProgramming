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

class DAQmxCounterInput(DAQmxChannel):
    def __init__(self, dev):
        super().__init__(dev)
        self.ext_src = ''
        self.decoding_type = ''
        self.zidx_enable = ''
        self.zidx_val = 0.1
        self.zidx_phase = constants.EncoderZIndexPhase
        self.units = constants.AngleUnits
        self.pulses_per_rev = 1
        self.initial_angle = 0.01

        self.min_val = 0.1
        self.max_val = 1.0

        self.edge = constants.Edge

    def ang_encoder(self):
        self.task.ci_channels.add_ci_ang_encoder_chan(self.dev, units=self.units)

    def ang_velocity(self):
        self.task.ci_channels.add_ci_ang_velocity_chan(self.dev)

    def count_edges(self):
        self.initial_count = 1
        self.count_direction = constants.CountDirection
        self.task.ci_channels.add_ci_count_edges_chan(self.dev, self.edge, self.initial_count, self.count_direction)

    def duty_cycle(self):
        self.min_freq = 0.1
        self.max_freq = 1.0
        self.task.ci_channels.add_ci_duty_cycle_chan(self.dev)

    def freq(self):
        self.meas_methods = constants.CounterFrequencyMethod
        self.meas_time = 1.0
        self.divisor = 1.0
        self.task.ci_channels.add_ci_freq_chan(self.dev, self.min_val, self.max_val, self.units, self.edge, self.meas_methods, self.meas_time, self.divisor)



class DAQmxCounterOutput(DAQmxChannel):

    def __init__(self, dev):
        super().__init__(dev)
        self.ext_src = ''
        self.src_term = ''
        
        self.units = constants.FrequencyUnits
        self.idle_state = constants.Level
        self.delay = 0.001
        self.freq = 0.000000001
        self.duty_cycle = 1
        self.low_ticks = 1
        self.high_ticks = 1
        self.low_time = 1.0
        self.high_time = 1.0
    
    def set_freq(self):
        self.task.co_channels.add_co_pulse_chan_freq(self.dev, self.units, self.idle_state, self.delay, self.freq, self.duty_cycle)
        
    def set_ticks(self):    
        self.task.co_channels.add_co_pulse_chan_ticks(self.dev, self.src_term, self.idle_state, self.delay, self.low_ticks, self.high_ticks)
        
    def set_times(self):
        self.task.co_channels.add_co_pulse_chan_time(self.dev, self.units, self.idle_state, self.delay, self.low_time, self.high_time)
