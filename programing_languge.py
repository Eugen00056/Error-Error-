from PIL import Image
from tkinter import *
from tr import *
from tkinter import ttk
root = Tk()
root.title("...") 
root.geometry("1202x700")  
label = Label(text="")
label3 = Label(text="") 
label.place(x=340,y=0)
label4 = Label(text="")
label4.place(x=940,y=601)
label4 = Label(text="")
label4.place(x=940,y=501)
label5 = Label(text="Часть окна. здесь нужно построчно писать \nкод на питоне для вызова ошибки и написания\nглавного кода на Error?Error!(этот язык)")
label5.place(x=600,y=521)
label3.place(x=0,y=20)
comand = ''
entry = ttk.Entry()
entry.place(x=740,y=590)
entry2 = ttk.Entry()
entry2.place(x=50,y=650)
code = ''
c = 0
def delete():
    global code
    code = ""
    label4.config(text = code)
def add():
    global code
    code += entry.get()+'\n'
    label4.config(text = code)
def ask():
    global comand
    try:
        exec(code)
    except TypeError:
        comand += '  TypeError'
    except NameError:
        comand += '  NameError'
    except KeyError:
        comand += '  KeyError'
    except IndexError:
        comand += '  IndexError'
    except ZeroDivisionError:
        comand += '  ZeroDivisionError'
    except SyntaxError:
        comand += '  SyntaxError'
    except EOFError:
        comand += '  EOFError'
    except ValueError:
        comand += '  ValueError'
    except MemoryError:
        comand += '  MemoryError'
    except SystemExit:
        comand += '  SystemExit'
    except StopIteration:
        comand += '  StopIteration'
    except RecursionError:
        comand += '  RecursionError'
    except UnicodeEncodeError:
        comand += '  UnicodeEncodeError'
    label.config(text = comand)
    if len(comand.split('\n')[-1]) >120:
        comand += '\n'
def add2():
    comand += f'  {entry.get()}'
    if len(comand.split('\n')[-1]) >120:
        comand += '\n'

def help():
    global c
    if c == 0:
        label3.config(text = 'NameError: "."\nIndexError: ","\nTypeError: "<"\nKeyError: ">"\nZeroDivisionError: "-"\nSyntaxError: "+"\nValueError: "["\nStopIteration: "]"\nEOFError: переход на первую ячейку\nMemoryError: в текущую ячейку будет\n записан номер первого\n вхождения ord символа идущего\n после этой команды \nсреди ячеек\nUnicodeEncodeError: позволяет записать отдельный кусочек \nкода в специальную ячейку, закрывается "RecursionError"\nSystemExit: выполняет сохраненный кусочек кода')
        c=1
    else:
        label3.config(text = '')
        c=0
def plus_to_command1(text):
    global comand
    if text=='Backspace':
        comand = comand[:len(comand) - len(comand.split('  ')[-1])-2]
        label.config(text = comand)
def delete_all():
    global comand
    comand = ''
    label.config(text = comand)
def go():
    global comand
    txt = run(comand)
    label2.config(text = f'Результат:\n{txt}')
button1= ttk.Button(text="Backspace", command= lambda:  plus_to_command1('Backspace'))
button2= ttk.Button(text="Run", command= go)
button3= ttk.Button(text="help", command= help)
button4= ttk.Button(text="delete all", command= delete_all)
button5= ttk.Button(text="run for find an error", command= ask)
button6= ttk.Button(text="add to code", command= add)
button7= ttk.Button(text="add to main code", command= add2)
button8= ttk.Button(text="del code", command= delete)
label2 = Label(text=f"Результат:")
button1.place(x=450,y=650)
button2.place(x=350,y=650)
button3.place(x=0,y=0)
button4.place(x=260,y=650)
button5.place(x=790,y=650)
button6.place(x=700,y=650)
button8.place(x=700,y=620)
button7.place(x=150,y=650)
label2.place(x=380,y=470)
root.mainloop()