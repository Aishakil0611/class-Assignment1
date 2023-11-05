class MultipleFunctions():
    def subfields():
        print("sub-fields in AI are:")
        subfieldsInAI=["Machine Learning","Neural Networks","vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in subfieldsInAI:
            print(i)
            message=subfieldsInAI
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even Number")
        else:
            print(num, "Odd Number")
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Age>20):
             print("ELIGIBLE")
        elif(Age>18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        M1=int(input("Subject1="))
        M2=int(input("Subject2="))
        M3=int(input("Subject3="))
        M4=int(input("Subject4="))
        M5=int(input("Subject5="))
        Total= M1+M2+M3+M4+M5
        print("Total:",Total)
        percentage=(Total)/5
        print("Percentage:",percentage)
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area_formula=(Height*Breadth)/2
        print("Area formula=(Height*Breadth)/2")
        print("Area of Triangle",Area_formula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter_formula=Height1+Height2+Breadth
        print("Perimeter formula=Height1+Height2+Breadth")
        print("Perimeter of Triangle",Perimeter_formula)