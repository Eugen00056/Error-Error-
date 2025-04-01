from PIL import Image
from tkinter import *
from tr import *
from tkinter import ttk
import tkinter as tk
root = Tk()
root.title("...") 
root.geometry("1250x700")  
def ask():
    global comand
    try:
        code = text_input.get("1.0", "end-1c") # type: ignore
        exec(code)
        print('Плохой код. Нет ошибок')
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
    except:
        print('нипонятая ошибка')
    Main_code.config(text = comand) # type: ignore
    if len(comand.split('\n')[-1]) >120:
        comand += '\n'
def add():
    global comand
    comand += f'  {str(adding_ord.get())[0]}' # type: ignore
    Main_code.config(text = comand) # type: ignore
    if len(comand.split('\n')[-1]) >120:
        comand += '\n'
def plus_to_command1(text):
    global comand
    if text=='Backspace':
        comand = comand[:len(comand) - len(comand.split('  ')[-1])-2]
        Main_code.config(text = comand) # type: ignore
def delete_all():
    global comand
    comand = ''
    Main_code.config(text = comand) # type: ignore
def go():
    global comand
    txt = run(comand)
    if len(txt)> 23:
        txt_2 = ''
        for i in range(0,len(txt),23):
            txt_2 += txt[i:i+23]+ '\n'
        txt = txt_2

    result.config(text = f'Результат:\n{txt}') # type: ignore
def Made_all():
    Main_code = tk.Label(root, text="",justify=tk.LEFT)
    label3 = tk.Label(root, text="",justify=tk.LEFT)
    Main_code.place(x=340,y=0)
    label4 = tk.Label(root, text="",justify=tk.LEFT)
    label4.place(x=940,y=601)
    info = tk.Label(root, text="",justify=tk.LEFT)
    info.place(x=0,y=0)
    info.config(text = 'NameError: "."\nIndexError: ","\nTypeError: "<"\nKeyError: ">"\nZeroDivisionError: "-"\nSyntaxError: "+"\nValueError: "["\nStopIteration: "]"\nEOFError: переход на первую ячейку\nMemoryError: в текущую ячейку будет записан\nномер первого вхождения ord символа идущего\nпосле этой команды среди ячеек\nUnicodeEncodeError: позволяет записать отдельный\nкусочек кода в специальную ячейку, закрывается\n"RecursionError"\nSystemExit: выполняет сохраненный кусочек кода')
    comand = ''
    adding_ord = ttk.Entry()
    adding_ord.place(x=0,y=650)
    code = ''
    entry = tk.Frame(root)
    entry.place(x=750,y=460)
    scrollbar = tk.Scrollbar(entry)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_input = tk.Text(entry, 
                        height=10, 
                        width=50, 
                        yscrollcommand=scrollbar.set)
    text_input.pack(side=tk.LEFT)
    scrollbar.config(command=text_input.yview)
    Backspace_button= ttk.Button(text="Backspace", command= lambda:  plus_to_command1('Backspace'))
    Run_button= ttk.Button(text="Run", command= go)
    delete_all_button= ttk.Button(text="delete all", command= delete_all)
    run_for_find_an_error_button= ttk.Button(text="run for find an error", command= ask)
    add_to_main_code_one_symbol= ttk.Button(text="add to main code one symbol\nfor (MemoryError)", command= add)
    Backspace_button.place(x=520,y=650)
    Run_button.place(x=430,y=650)
    delete_all_button.place(x=340,y=650)
    run_for_find_an_error_button.place(x=850,y=650)
    add_to_main_code_one_symbol.place(x=150,y=650)
    result = tk.Label(root, text="Результат:",justify=tk.LEFT)
    result.place(x=500,y=470)
Made_all()
root.mainloop()
