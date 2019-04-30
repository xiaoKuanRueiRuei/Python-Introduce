s=input("Enter a genome string:")
s=s[s.find("ATG")+3:]
while (s.find("ATG" or "TAG" or "TAA" or "TGA") !=-1):
    s2=s[:s.find("ATG" or "TAG" or "TAA" or "TGA")]
         
if len(s2)%3==0:
    print(s2)
else:
    print("No gene is found.")