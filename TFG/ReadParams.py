import sys
def VerifyParams():
  validAlg = ["bubble", "merge", "counting"]
  numParam = len(sys.argv) - 1
  if numParam != 3 or (int(sys.argv[2]) < 1 or (int(sys.argv[2]) > 2) or (int(sys.argv[3])) < 3 or int(sys.argv[3]) > 5) or sys.argv[1] not in validAlg:
    return False
  else:
    return True


def ReadParameters():
    Algorithm = ""
    testGPT = False
    GPT = 0
    isValid = False
    if not VerifyParams():
     print("Usage: python main.py [ALGORITMO] [1|2] [3|4|5]\n"
          "\t ALGORITMO: <bubble> <merge> <counting>\n"
          "\t 1: TEST GENERADOS POR GPT\n"
          "\t 2: TEST PRE-GENERADOS\n"
          "\t 3: GPT 3.5\n"
          "\t 4: GPT 4 \n"
          "\t 5: Mistral")
     return Algorithm, testGPT, GPT, isValid
    else:
     isValid = True
     Algorithm = sys.argv[1]
     if (int(sys.argv[2]) == 1):
       testGPT = True
     else:
       testGPT = False
     if(int(sys.argv[3]) == 3):
       GPT = 3
     elif(int(sys.argv[3]) == 4):
       GPT = 4
     elif(int(sys.argv[3]) == 5):
       GPT = 5
     return Algorithm, testGPT, GPT, isValid
