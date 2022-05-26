# ZoomIPGeography
Pull Country Locations into csv file for all Zoom Servers

If you go to https://assets.zoom.us/docs/ipranges/ZoomMeetings.txt you get a current list of all our IP ranges.  
If you take that list to a service like “https://ipwhois.app/json/11.11.11.11” it will spit out a response showing where it thinks 
that IP address originates.   

So I wrote a little python script that automates that process and leaves the result in a csv file.  
There is a variable in the script “usOnly = True” that determines whether you want only US IP addresses in the list.

Comment 1 - If someone else hosts a meeting on a non-us server, you may not be able to join because you are blocking access to servers in their country.

Comment 2 - The IP ranges don’t change that often, but they do change on occasion.  
Weird symptoms will result when you cherry pick the servers and miss one or two.

Comment 3 - This alone doesn’t keep you from joining meetings with servers in other countries.  
For instance, everyone joining your meeting from your network would only join via Zoom’s US servers.  
If someone in Germany, not VPN’d into your network, joined the meeting, Zoom would connect them to the closest Zoom server in Germany 
and that server would connect to a Zoom server in the US.  
The Zoom server in Germany would be a part of the meeting but would never attempt to connect to anyone on your network.  

To fix this issue, you need to have Zoom limit the geography of servers allowed in your meetings.  
zoom.us/ portal -    Admin/Account Management/Account Profile/ Transit Data
