# This python code is opening the file um-server-01.txt so we can access it.

log_file = open("um-server-01.txt")


# def will create a function calaled sales_reports in the file
# You use the for to loop through the function on the line in the file.
# you can use rstrip to deal with getting rid of whitespace. rstrip will get rid of the space to the right of line. lstrip will do the left. and strip will take the whitespace on both sides.
# The day line is telling where to stip in the file using the[0:3] is where to stip. You can do this in an array or list as python calls them
# Then If is just wrintng and if statement looking if the day is TUE
# print refefs to TUE and will print the orders of the watermelon that came on TUE
# sales_report at the end is calling the function like you do in JS
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
