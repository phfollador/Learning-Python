# GETTIG SECONDS
def getting_seconds():
    seconds = int(input("SECONDS> "))
    return seconds

# CALCULATE HH:MM:SS
def cal_time(seconds):
    seconds_rest = seconds%86400
    hours = seconds_rest//3600
    seconds_rest = seconds_rest%3600
    minutes = seconds_rest//60
    seconds_rest = seconds_rest%60

    print(hours, ":", minutes, ":", seconds_rest)

def main():
    sec = getting_seconds()
    cal_time(sec)
main()