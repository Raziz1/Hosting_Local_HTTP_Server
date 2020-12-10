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

 
