from Compitation import Compitation

def main():
    
    print("---------------Coding Contest--------------")
    comp = Compitation("Coding Contest", 1000)
    comp.participants.append("Ravi")
    print(Compitation.participants)

if __name__ == "__main__":
    main()