# SMS-Weather-Updates
Get weather updates texted to you when keywords are in the forecast

<b>Overview:</b> Uses Selenium to launch weather.gov and search for weather by zip code. A BeautifulSoup object is created for the loaded URL and the forecast for the week is extracted. A while loop and if statements are used to determine if "snow" or any other keywords of your choosing are in the forecast. When the keyword is found, a text message is sent to the user. 
 
<b>Pre-requisites:</b>
<ul>
<li> Python v3.x </li>
<li> IDLE (or any other IDE of your choosing) </li>
<li> A free Twilio account for sending SMS messages </li>
</ul>
<b> Source Data:</b><br>
<img src="image002.jpg" alt="">
<b> Output: </b><br>
<img src="image004.jpg" alt="CSV File Location">
<br>
<b> Future Enhancements:</b><br>
<ul>
<li> Schedule the script to run automatically</li>
<li> Cleanup If statement code with Regular Expressions</li>
<li> Modify code to send an e-mail instead of text </li>
</ul>
