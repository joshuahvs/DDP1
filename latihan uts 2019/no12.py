# def hitung_token_per_kalimat(file):
#     open_file = open(file, "r")
#     list_of = []
#     counter = 0

#     for line in open_file:
#         word = line.split('\t')
#         print(word)
#         if word != '\n':
#             counter+=1
#         else:
#             list_of.append(counter)
#             counter = 0
#         return counter
    
def hitung_token_per_kalimat(fileName):
          fileObj = open(fileName, "r")
          lines = fileObj.readlines()
          print(lines)
          result = []
          lineCounter = 0
          for line in lines:
          
               if line != "\n":
                    lineCounter += 1
               else:
                    result.append(lineCounter)
                    lineCounter = 0
          if lineCounter != 0: # if the last line is not “\n”
               result.append(lineCounter)
          return result

print(hitung_token_per_kalimat("file.txt"))
