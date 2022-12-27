class Frankenstein:
    def read():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            file_contents=file_contents.lower()
            #print(file_contents)
            file_arr=file_contents.split()
            #print(file_arr)
            file_dict={
                "a":0,
                "b":0,
                "c":0,
                "d":0,
                "e":0,
                "f":0,
                "g":0,
                "h":0,
                "i":0,
                "j":0,
                "k":0,
                "l":0,
                "m":0,
                "n":0,
                "o":0,
                "p":0,
                "q":0,
                "r":0,
                "s":0,
                "t":0,
                "u":0,
                "v":0,
                "w":0,
                "x":0,
                "y":0,
                "z":0
            }
            count=0
            for x in file_arr:
                count=count+1
                for i in x:
                    #print(i)
                    if(i in file_dict):
                        file_dict[i]=file_dict[i]+1
                    

               
            print(f"{count} words found in the document")
            print()
            #file_dict["a"]=file_dict["a"]+1
            #print(file_dict["a"])
            #print(file_dict)
            for i in file_dict:
                print(f"The {i} character was found {file_dict[i]} times")

def main():
    Frankenstein.read()

main()


