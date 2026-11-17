# Name: Fakhri Al Ghifari Busra
# NIM: 2611531013
# Question 7

name = "Fakhri Al Ghifari Busra"
nim = "2611531013"
username = "fakhri013" 
intake = "20" + nim[:2]
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name'.ljust(10)}: {name.title()}")
print(f"{'NIM'.ljust(10)}: {nim}")
print(f"{'Username'.ljust(10)}: {username}")
print(f"{'Intake'.ljust(10)}: {intake}")
print("=" * 30)