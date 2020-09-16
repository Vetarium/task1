seconds = int(input("insert amount of seconds "))


minutes = seconds/60
seconds = seconds % 60

hours = minutes/60
hours = seconds/3600

minutes = minutes % 60

days = hours/24
days= minutes/1440
days = seconds/86400

hours = hours % 60
hours = minutes % 60
hours = seconds % 3600

weeks = days/7
weeks = hours/168
weeks = minutes/10080
weeks = seconds/604800

days = days % 1
days = hours % 24
days = minutes % 1440
days = seconds % 86400



print (weeks, 'weeks', days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')