#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Reciver
# Generated: Tue Oct  3 19:45:36 2023
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time


class FM_reciver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Reciver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Reciver")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "FM_reciver")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tune = tune = 105.5e6
        self.sample_rate = sample_rate = 614985
        self.rf_gain = rf_gain = 150

        ##################################################
        # Blocks
        ##################################################
        self._sample_rate_range = Range(150e3, 56e6, 1, 614985, 200)
        self._sample_rate_win = RangeWidget(self._sample_rate_range, self.set_sample_rate, "sample_rate", "counter_slider", float)
        self.top_layout.addWidget(self._sample_rate_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(sample_rate)
        self.uhd_usrp_source_0.set_center_freq(105.5e6, 0)
        self.uhd_usrp_source_0.set_gain(5, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_bandwidth(970e3, 0)
        self._tune_range = Range(70e6, 6e9, 1, 105.5e6, 200)
        self._tune_win = RangeWidget(self._tune_range, self.set_tune, "frequency", "counter_slider", float)
        self.top_layout.addWidget(self._tune_win)
        self._rf_gain_range = Range(100, 200, 1, 150, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, "rf_gain", "counter_slider", float)
        self.top_layout.addWidget(self._rf_gain_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	105.5e6, #fc
        	194e3, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label("Relative Gain", "dB")
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	105.5e6, #fc
        	2e6, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label("Relative Gain", "dB")
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	100, sample_rate, 50e3, 30e3, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	100, sample_rate, 30e3, 20e3, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	100, sample_rate, 20e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=sample_rate*4,
        	audio_decimation=10,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 50)
        self.analog_agc2_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0_1, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "FM_reciver")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tune(self):
        return self.tune

    def set_tune(self, tune):
        self.tune = tune

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.uhd_usrp_source_0.set_samp_rate(self.sample_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(100, self.sample_rate, 50e3, 30e3, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(100, self.sample_rate, 30e3, 20e3, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(100, self.sample_rate, 20e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.sample_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain


def main(top_block_cls=FM_reciver, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
