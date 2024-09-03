from ReadParams import ReadParameters
from Utils import ReadTest,ParsePython,SaveResult,AddImport
from GenerateCode import GenerateCode, GenerateTests
import time,io,sys



if __name__ == '__main__':
    Algorithm,Test,GPT,isValid = ReadParameters()
    if(isValid == True):
        start_time = time.time()
        if(GPT == 3 ):
            print("\n[INFO] Generating code from GPT3:\n")
            if(Test==True):
                code = GenerateCode(3, Algorithm)
                test = GenerateTests(3, Algorithm, code)
                code = ParsePython(code)
                print(code)
                print("\n[INFO] Generating the test from GPT3:\n")
                test = ParsePython(test)
                print(test)
                result=AddImport(test)
            else:
                code = GenerateCode(3, Algorithm)
                code = ParsePython(code)
                print(code)
                test = ReadTest()
                result = test.replace("CODIGOINSERTAR", code)
                print("\n[INFO] Running predefined tests for the generated code:\n")
                print(result)
        elif(GPT == 4):
            print("\n[INFO] Generating code from GPT4\n")
            if(Test==True):
                code = GenerateCode(4, Algorithm)
                test = GenerateTests(4, Algorithm, code)
                code = ParsePython(code)
                print(code)
                print("\n[INFO] Generating the test from GPT4:\n")
                test = ParsePython(test)
                result = AddImport(test)
                print(test)
            else:
                code = GenerateCode(4, Algorithm)
                code = ParsePython(code)
                print(code)
                test = ReadTest()
                result = test.replace("CODIGOINSERTAR", code)
                print("\n[INFO] Running predefined tests for the generated code\n")
                print(result)
        elif(GPT == 5):
            print("\n[INFO] Generating code from Mistral\n")
            if (Test == True):
                code = GenerateCode(5, Algorithm)
                test = GenerateTests(4, Algorithm, code)
                code = ParsePython(code)
                print(code)
                print("\n[INFO] Generating the test from Mistral:\n")
                test = ParsePython(test)
                result = AddImport(test)
                print(result)
            else:
                code = GenerateCode(5, Algorithm)
                code = ParsePython(code)
                print(code)
                test = ReadTest()
                result = test.replace("CODIGOINSERTAR", code)
                print("\n[INFO] Running predefined tests for the generated code\n")
                print(result)

        try:
           print("\n\n########### TEST RESULTS ############\n\n")
           exec(result)
        except Exception as e:
           print(f"\n[ERROR] Somenthing went wrong trying to execute the tests: {e}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        time = f"[INFO] The elapsed time was: {elapsed_time} segundos"
        print(time)
        SaveResult(result ,time)
