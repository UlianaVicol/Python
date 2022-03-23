## INS:
##   start time: HH:MM  "10:05"
##   end time  : HH:MM

##OUT:
##   duration in minutes

#24H format for
# test1: "10:05" ---> "10:15" = 10
# test2: "10:05" ---> "11:15" = 70
# test3: "11:15" ---> "12:05" = 6 -10 -> 500 
# test4: "22:45" ---> "01:30" = 165  = (1-22) * 60 + 30 - 45 | -1260 +- 15 -> - 1275(-21h -15m) !! 165
# test5: "22:45" ---> "24:00" | "00:00" --> "01:30" 

#integer numbers

start_time = input( "start time (HH:MM): " )
start_time_h = int( start_time[0:2] )
start_time_m = int( start_time[3:5] )

end_time   = input( "end time (HH:MM): " )
end_time_h = int( end_time[0:2] )
end_time_m = int( end_time[3:5] )



duration_h   = end_time_h - start_time_h
duration_m   = end_time_m - start_time_m
duration_m_f = duration_h * 60 + duration_m + 24 * 60 * (start_time_h > end_time_h) 

# HW1: calculate and print duration: HOURS + MINUTES

duration_h = duration_m_f // 60
duration_m = duration_m_f % 60

print("Event duration:", duration_h, "H", duration_m,  "minutes")

# print("Event duration:", duration_m_f,  "minutes")
