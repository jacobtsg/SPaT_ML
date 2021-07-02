# SPaT_ML
SPaT
signal_events.txt - https://drive.google.com/file/d/1Efgf770MC4W3vB284u84Hs97ucJzfWAU/view?usp=sharing  

Input Data:

Variable #1:  Timestamp
Variable #2:  DeviceID
Variable #3:  EventID ( “Phase”)
Variable #4:  Parameter (“Light Number” )

combine with Traffic_Count and INcident/NearMiss Data...

Output Goals:

Output Variable #1:  “Time_Wasted”  per intersection per hour 
Output Variable #2:  “Fuel_Consumption_Wasted”  per intersection per hour
Output Variable #3:  “Total_Emissions_Wasted”  per intersection per hour
Output Variable #4:  “Incident_Rate_Per_Phase” per intersection per hour
Output Variable #5:  Intersection_Metric_Score (combine these features to identify problematic intersections) - rank them based on Score

Output #6: I2V application to send Red light warnings to incoming smart vehicles.

Output #7: I2V Pedestrian warnings sent (especially at night) when there has been a SPaT eventID of pedestrian crossing, i.e. this could be sent to cars that are approaching an intersection (within for example. 120 -150 seconds of a previous pedestrian crossing signal ) so that cars are aware there is a pedestrian is on the road beyond the intersection (in the general vicinity), which is often the case of pedestrian deaths

Output #8: Emergency situations SPAT with traffic flow can help to ease the path for emergency vehicles and arrange the traffic based on the situation. The models can predict when a lane will be used by emergency vehicles.

Output #9: Traffic Signal Optimization using I2V : use computer vision to reduce the waiting time of a car/pedestrian at an intersection using SPaT Data

