import os
from datetime import datetime

def ReadPrompt(prompt):
    if(prompt == "OnlyCode"):
        try:
            with open('Prompts/PromptOnlyCode.txt', 'r') as archivo:
                contenido = archivo.read()
        except FileNotFoundError:
            raise Exception("[ERROR] Cannot find the prompt")
        except Exception as e:
            raise Exception("[ERROR] An error has ocurred")
    else:
        try:
             with open('Prompts/PromptCodeAndTest', 'r') as archivo:
                contenido = archivo.read()
        except FileNotFoundError:
            raise Exception("[ERROR] Cannot find the prompt")
        except Exception as e:
            raise Exception("[ERROR] An error has ocurred")
    return contenido

def ReadTest():
    try:
        with open('Tests/TestsDeOrdenación.txt', 'r') as tests:
            test = tests.read()
    except FileNotFoundError:
        raise Exception("[ERROR] Cannot find the test")
    except Exception as e:
        raise Exception("[ERROR] An error has ocurred")
    return test


def ParsePython(code):
     code = code.replace("```python","")
     return code.replace("```","")

def AddImport(test):
    test_split = test.split('\n', 1)
    result = test_split[0] + "\n" + "import math" + "\n" + "\n" + test_split[1]
    return result


def SaveResult(result,time):
    name="Result_" + datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    carpeta='Results/' + name
    toWrite = result + time
    try:
        with open(carpeta, 'w') as archivo:
            archivo.write(toWrite)
    except FileNotFoundError:
        raise Exception("[ERROR] Cannot save the code")
    except Exception as e:
        raise Exception("[ERROR] An error has ocurred")
    print(f"[INFO] The code,test and exec was succesfully saved in:Results/{name}")


