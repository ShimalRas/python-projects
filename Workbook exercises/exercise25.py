#Units of time 2
# do it in reverse

User_seconds = int(input("Enter the amount of seconds: "))
seconds = User_seconds%60
minutes = User_seconds//60

hours = minutes//60
days = hours//24
print(f"the days is {days}, and hours is {hours}, and minutes is {minutes} and seconds {seconds}")