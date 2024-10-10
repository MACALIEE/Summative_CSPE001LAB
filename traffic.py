import matplotlib.pyplot as plt


local_speed = 25      # average speed for local streets (mph)
major_speed = 40      # average speed for a major street (mph)
normal_freeway = 55   # average freeway speed in normal conditions (mph)
congest_freeway = 18  # average freeway speed during congestion (mph)
Avg_redlight = 2.0    # average time for traffic light (minutes)
left_on_major = 2.5   # time delay to make left onto major street (minutes)
stop_sign = 0.5       # average time for a stop sign (minutes) - 30 seconds

segment = [0.]*11

segment[0] = 1325.  # Segment 1
segment[1] = 716.   # Segment 2
segment[2] = 2800.  # Segment 3
segment[3] = 3052.  # Segment 4
segment[4] = 2995.  # Segment 5
segment[5] = 1839.  # Segment 6
segment[6] = 1725.  # Segment 7
segment[7] = 707.   # Segment 8
segment[8] = 2340.  # Segment 9
segment[9] = 10235. # Segment 10 (Freeway)
segment[10] = 868.  # Segment 11

# Convert segment lengths from feet to miles
for i in range(11):
    segment[i] = segment[i] / 5280  # Convert feet to miles


freeway_normal = [0.]*8
free_norm_cum = [0.]*8
freeway_congest = [0.]*8
free_con_cum = [0.]*8
local = [0.]*8
local_cum = [0.]*8


ind = [1, 2, 3, 4, 5, 6, 7, 8]


freeway_normal[0] = (segment[0] / normal_freeway) * 60 + stop_sign  # Segment 1
freeway_normal[1] = (segment[8] / normal_freeway) * 60              # Segment 9
freeway_normal[2] = (segment[9] / normal_freeway) * 60              # Segment 10
freeway_normal[3] = (segment[10] / normal_freeway) * 60 + Avg_redlight  # Segment 11 + traffic light
freeway_normal[4] = (segment[6] / major_speed) * 60                 # Segment 7
freeway_normal[5] = (segment[7] / local_speed) * 60 + Avg_redlight  # Segment 8 + traffic light


freeway_congest[0] = (segment[0] / congest_freeway) * 60 + stop_sign  # Segment 1
freeway_congest[1] = (segment[8] / congest_freeway) * 60              # Segment 9
freeway_congest[2] = (segment[9] / congest_freeway) * 60              # Segment 10
freeway_congest[3] = (segment[10] / congest_freeway) * 60 + Avg_redlight  # Segment 11 + traffic light
freeway_congest[4] = (segment[6] / major_speed) * 60                 # Segment 7
freeway_congest[5] = (segment[7] / local_speed) * 60 + Avg_redlight  # Segment 8 + traffic light


local[0] = (segment[0] / local_speed) * 60 + stop_sign               # Segment 1
local[1] = (segment[1] / major_speed) * 60 + Avg_redlight + left_on_major  # Segment 2 + traffic light + left turn
local[2] = (segment[2] / major_speed) * 60 + stop_sign               # Segment 3
local[3] = (segment[3] / major_speed) * 60 + stop_sign               # Segment 4
local[4] = (segment[4] / major_speed) * 60 + stop_sign               # Segment 5
local[5] = (segment[5] / major_speed) * 60                           # Segment 6 (no left turn here)
local[6] = (segment[6] / major_speed) * 60 + Avg_redlight            # Segment 7 + traffic light
local[7] = (segment[7] / local_speed) * 60 + Avg_redlight + left_on_major  # Segment 8 + traffic light + left turn


local_cum[0] = local[0]
free_norm_cum[0] = freeway_normal[0]
free_con_cum[0] = freeway_congest[0]

for y in range(1, 8):
    local_cum[y] = local_cum[y-1] + local[y]
    free_norm_cum[y] = free_norm_cum[y-1] + freeway_normal[y]
    free_con_cum[y] = free_con_cum[y-1] + freeway_congest[y]


plt.plot(ind, free_norm_cum, color='r', label="Freeway Normal")
plt.plot(ind, free_con_cum, color='g', label="Freeway Congested")
plt.plot(ind, local_cum, color='b', label="Local")
plt.xlabel('Segments')
plt.ylabel('Time (minutes)')
plt.legend(loc=2)
plt.show()

print("Local Route Cumulative Times:", local_cum)
print("Freeway Normal Cumulative Times:", free_norm_cum)
print("Freeway Congested Cumulative Times:", free_con_cum)

local_tot = sum(local[:8])
free_norm_tot = sum(freeway_normal[:8])
free_cong_tot = sum(freeway_congest[:8])

print('Local Total:', local_tot)
print('Freeway Normal Total:', free_norm_tot)
print('Freeway Congested Total:', free_cong_tot)
