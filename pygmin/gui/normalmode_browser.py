from PyQt4 import QtGui, QtCore, Qt
from  ui.ui_normalmode_explorer import Ui_MainWindow as UI
from pygmin.thermodynamics import normalmodes 
import numpy as np
import pickle
from dlg_params import DlgParams

class NormalmodeItem(QtGui.QListWidgetItem):    
    def __init__(self, normalmode):
        text="%.5e"%normalmode[0]
        self.normalmode = normalmode
        
        QtGui.QListWidgetItem.__init__(self, text)
        
    def get_mode(self):
        return self.normalmode[1]
    
    def get_freq(self):
        return self.normalmode[0]
    
    def __lt__(self, item2):
        #sort the energies in the list lowest to highest
        return self.normalmode[0] < item2.normalmode[0]
    
class NormalmodeBrowser(QtGui.QMainWindow):
    def __init__(self, parent=None, system=None, app=None):
        QtGui.QMainWindow.__init__(self, parent=parent)
        
        self.ui = UI()
        self.ui.setupUi(self)
        
        self.ui.view3D.setSystem(system)
        self.system = system
        self._params = dict()
        self._params["amplitude"]=1.0
        self._params["remove_known_zeroev"]=True
        export = self._params["export"] = dict()
        export["nframes"]=100
        
        self._params["nframes"] = 30
         
    def set_coords(self, coords, normalmodes=None):
        self.coords = coords
        self.normalmodes = normalmodes        
        
        if normalmodes is None:
            self._calculate_normalmodes()
        
        self._fill_normalmodes()
        
        self.ui.view3D.setCoords(coords)
        
    def _calculate_normalmodes(self):
#        pot = self.system.get_potential()
#        E, g, hess = pot.getEnergyGradientHessian(self.coords)
#        metric = self.system.get_metric_tensor(self.coords)
#        freq, mode = normalmodes(hess, metric = metric)
        freq, mode = self.system.get_normalmodes(self.coords)
        mode=np.real(mode.transpose())
        
        self.normalmodes = []
        #self.normalmodes.append((fre[0], m.flatten()))
        for f, m in zip(freq, mode):
            self.normalmodes.append((f, m)) #np.dot(metric, m)))
             
    def _fill_normalmodes(self):
        self.ui.listNormalmodes.clear()
        for n in self.normalmodes:
            self.ui.listNormalmodes.addItem(NormalmodeItem(n))
        
    def on_listNormalmodes_currentItemChanged(self, newsel):
        if newsel is None:
            self.currentmode = None
            return
        orthogopt = self.system.get_orthogonalize_to_zero_eigenvectors()
        mode = newsel.get_mode().copy()
        if self._params["remove_known_zeroev"]:
            mode = orthogopt(mode, self.coords)
         
        self.currentmode = mode
        
        # generate the configurations from the normal mode
        amp = self._params["amplitude"]
        vector = self.currentmode
        nframes = self._params["nframes"]
        coordspath = [self.coords + amp * vector * float(i) / nframes 
                      for i in xrange(nframes)]
        coordspath = np.array(coordspath)

        # get the energies of the configurations for the labels
        pot = self.system.get_potential()
        labels = ["energy="+str(pot.getEnergy(coords)) for coords in coordspath]
        
        self.ui.view3D.setCoordsPath(coordspath, labels=labels)
        self.ui.view3D.ui.btn_animate.hide()
        
    def on_actionRun_toggled(self, checked=None):
        if checked is None: return
        if checked:
            self.ui.view3D.start_animation()
        else:
            self.ui.view3D.stop_animation()

    def on_actionSave_triggered(self, checked=None):
        if checked is None:
            return
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.AnyFile)
        dialog.selectFile("mode.pickle")
        dialog.setAcceptMode(QtGui.QFileDialog.AcceptSave);
        if(not dialog.exec_()):
            return
        filename = dialog.selectedFiles()[0]
        path = []
        nframes = self._params["export"]["nframes"]
        for i in xrange(nframes):
            t = np.sin(i/float(nframes)*2.*np.pi)
            path.append(self.coords + self._params["amplitude"]*t*self.currentmode)
        pickle.dump(path, open(filename, "w"))

    def on_actionParameters_triggered(self, checked=None):
        if checked is None:
            return
        if not hasattr(self, "_paramsdlg"):
            self._paramsdlg = DlgParams(self._params, parent=self)
        self._paramsdlg.show()            
    
        
if __name__ == "__main__":
    from OpenGL.GLUT import glutInit
    import sys
    glutInit()
    app = QtGui.QApplication(sys.argv)
    from pygmin.systems import LJCluster
    natoms = 13
    system = LJCluster(natoms)
    system.params.double_ended_connect.local_connect_params.NEBparams.iter_density = 5.
    x1, e1 = system.get_random_minimized_configuration()[:2]
    db = system.create_database()
    match = system.get_compare_exact()
    min1 = db.addMinimum(e1, x1)
    
    com = match.measure.get_com(x1)
    match.transform.translate(x1, -com)
    wnd = NormalmodeBrowser(app=app, system=system)
    wnd.set_coords(x1)
    
    wnd.show()
    sys.exit(app.exec_())     