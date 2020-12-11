# Hosting_Local_HTTP_Server 🌐📶💻
Using Raspberry Pi and Python to host a local HTTP server

<p> 
  <img width=384 height=384 align='Right' src="https://github.com/Raziz1/Hosting_Local_HTTP_Server/blob/main/images/webserver.png? raw=true">
</p>

## Overview 📄
This project was made using my [First_Webpage](https://github.com/Raziz1/First_Webpage) as the website to host. The python script is responsible for scrapping a bit of data for the website and writing to a text file(Not Relevant). The python script is also responsible for waking the Raspberry Pi (4) display and running the http server on a seperate thread.

## Libraries 📚
 *  [requests](https://pypi.org/project/requests/)
 *  [json](https://docs.python.org/3/library/json.html)
 *  [datetime](https://docs.python.org/3/library/datetime.html)
 *  [re](https://docs.python.org/3/library/re.html)
 *  [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
 *  [os](https://docs.python.org/3/library/os.html)
 *  [sys](https://docs.python.org/3/library/sys.html)
 *  [threading](https://docs.python.org/3/library/threading.html)
 *  [HTTPServer](https://docs.python.org/3/library/http.server.html)
 *  [webbrowser](https://docs.python.org/3/library/webbrowser.html)
 *  [subprocess](https://docs.python.org/3/library/subprocess.html)
 
 ## HTTP Server 🌐
 *  Ensure that the python (.py) script is in the same folder as your html, css, and javascript files.
 *  You can run the python script or you can manually create a new host port in the terminal by typing `python -m SimpleHTTPServer 8000` (Python 2) or `python3 -m http.server 8000` (Python 3). Then in your browser type in `localhost:8000`.
 *  To close the server simple press `CTRL + C` in the Terminal window
 * [Serving Files with Python's SimpleHTTPServer Module](https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/) is a great resource if you need further instruction.
 
## Crontab 🕒
 * Similarly to one of my previous projects you can setup a task scheduler that runs you python script at specified times. This is done by crontab on a raspberry pi.
  1. Press CTRL + ALT + T to open the terminal
  2. Type in `crontab -e`
  3. At the bottom of the terminal type in the interval of execution as well as the path to the python script
      * It should look something like this: `50 5 * * * export DISPLAY:=0 /home/pi/Downloads/script.py` This will run the script every day at 5:50am. You can use [Crontab.guru](https://crontab.guru/) to check your expression. 
      * Ensure that the script has executable permissions by using `chmod a+x foo.py`
      * Ensure that the python script contains "shebang" line at the top `#!/usr/bin/python`
      
 <pre># ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                   7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * &lt;command to execute&gt;
</pre>

 
