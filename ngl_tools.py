from os import listdir
from time import sleep
import pytraj as pt
import nglview as nv
import ipywidgets as widgets
from ipywidgets import interact

data_folder  = None
filename_png = None
ngl_view     = None

def set_data_folder(folder):
    global data_folder
    data_folder = folder

def ngl_plot(filename):
    global filename_png, ngl_view, data_folder

    traj = pt.load(f'{data_folder}/'+filename)
    ngl_view = nv.show_pytraj(traj)
    display(ngl_view)
    ngl_view._set_sync_camera
    ngl_view._remote_call("setSize",target="Widget", args=["500px","500px"])
    ngl_view.center()
    ngl_view.render_image()
    # print(view)
    filename_png = str(filename[:-3])+'png'
    # print(filename_png)
    # return filename_png

def ngl_save():
    # traj = pt.load('data/'+filename)
    # view = nv.show_pytraj(traj)
    ngl_view.download_image(filename_png)