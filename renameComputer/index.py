import subprocess
from tkinter import ttk, Tk, LabelFrame, Label, Entry, W, E
from tkinter.ttk import Progressbar


class Main:
    def __init__(self, window):
        self.wind = window
        self.wind.resizable(width=False, height=False)
        self.wind.title("Rename Computer")

        #Frame Container
        frame = LabelFrame(self.wind, text = 'Cambiar nombre de equipo')
        frame.grid(row=0, column=0, columnspan=3, pady = 20)

        #input
        Label(frame, text = 'Destino (IP o nombre de equipo)').grid(row=1, column=0)
        self.destino = Entry(frame)
        self.destino.focus()
        self.destino.grid(row=1, column=1)

        Label(frame, text='Nombre nuevo').grid(row=2, column=0)
        self.nuevoNombre = Entry(frame)
        self.nuevoNombre.grid(row=2, column=1)
        
        ttk.Button(frame, text = 'Aceptar', command = lambda: Main.rename(self, self.destino.get(), self.nuevoNombre.get()) ).grid(row=3, columnspan=3)
        #ttk.Button(frame, text = 'Salir', command = lambda: quit(self) ) .grid(row=3, column=1)


        self.salida = Label(text = 'Resultado', fg = 'red')
        self.salida.grid(row=1, column=0, columnspan=3)


    def rename(self, dato1, dato2):
        self.salida['text'] = 'Procesando...'
        try:
            comando = "netdom RENAMECOMPUTER " + dato1 + " /newname:" + dato2 + " /UserD:user /PasswordD:password /FORCE"
            res = subprocess.run(comando, shell=True)
            completed = res.returncode

            if completed == 53:
                self.salida['text'] = 'No se pudo establecer una conexión con el equipo ' + dato1
            elif completed == 87:
                self.salida['text'] = 'Campos incompletos'
            elif completed == 5:
                self.salida['text'] = 'Acceso Denegado'
            elif completed == 0:
                self.salida['text'] = 'Realizado, al reiniciar el equipo se aplicaran los cambios'
            else:
                self.salida['text'] = 'Error desconocido'
            self.destino['text'] = ''
            self.nuevoNombre['text'] = ''
        except ValueError:
            self.salida['text'] = 'Sin acceso a ' + dato1

    def quit(self):
        self.root.destroy()


if __name__ == '__main__':
    window = Tk()
    app = Main(window)
    window.mainloop()

