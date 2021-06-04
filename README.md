<!DOCTYPE html>

<html lang="en">
<head>
    <title>Informational Sector</title>
</head>
<body style="background-color: rgba(243, 239, 239, 0.856);">

# PyDA

## Python Digital Assistant

<h6 id="Author-details">
Creator - Samora Machel <br/>
Version - 1.2 <br/>
Status - Prototype <br/>
Date - 29-04-2020 <br/>

</h6>

<hr/>

<h4 class="header" style="color:blue;"> WELCOME</h3> 
    <br\>
    <pre style="color:black">This is PyDa your personal Digital Assistant
It gets all query that you input in the Entry box and even speak
out the answer after retrieving the query. 
Basically it retrived any query you want. Think of it as 
simplified webbrowser or wikipedia but it is not limited to querying
data only. It has capabilities to do much more when given specific
commands </pre>
<hr/>
<h4 class="header" style="color:blue;">COMMANDS</h3>
    <br\>
        <pre style="color:black">All commands start with a capital letter and are only executed
after you have initiated it with " > " symbol otherwise PyDa 
will assume it is a normal query 
There are basically 6 commands that PyDa Understands:</pre>
<hr/>
<ol>
    <li style="color:crimson">Help - 
        <pre class="content", style="color:black">
            Gives a general overview of what PyDa does but for deeper
            and more detailed information on PyDa, the command "Help-More"
            is very useful
                ::: <span style="color:darkcyan;font-weight:bolder;">Executed as "> Help" or "> Help-More"</span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Instagram - 
        <pre class="content", style="color:black">
            PyDa has an inbuild Instagram Bot that automatically Follows 
            and likes people from your instagram account. It can help
            you manage your instagram account incase your busy and sometimes
            don't have time for Instagram
            The Parameters it requires is :
                - The maximum ammount of people to follow
                - The maximum amount of like to give per person
                - To Prevent follow of people past what amount of followers
            To be on the safe side run the Instagram Bot once per day as 
            Instagram algorithm might seize your account for one week
               :::<span style="color:darkcyan;font-weight:bolder;"> Executed a"> Instagram" </span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Browser - 
        <pre class="content", style="color:black">
            This command enabled you to open your default browser, not only
            that but you can also query information like so
                ::: <span style="color:darkcyan;font-weight:bolder;">"> Browser who is SamoraMachel" </span>
            and you can opt to just open the browser like so 
                ::: <span style="color:darkcyan;font-weight:bolder;">"> Browser" </span> </pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">YouTube - 
        <pre class="content", style="color:black">
            PyDa has an inbult program to enable you to download programs from
            YouTube only. You can seperatly launch the program by typing
                :::<span style="color:darkcyan;font-weight:bolder;"> "> YouTube"</span>
            and then you enter the URL of the video to download and the 
            location where the video will to downloaded to 
            You can also opt to download the video without running the program 
            PyDa allows you to do so. 
            Like so,
                :::<span style="color:darkcyan;font-weight:bolder;"> "> YouTube URL-of-the-video"</span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Notebook -
        <pre class="content", style="color:black">
            PyDa has an internal Notebook
            :::<span style="color:darkcyan;font-weight:bolder;"> Executed as "> Notebook"</span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Convert -
        <pre class="content", style="color:black">
            PyDa is also able to convert a video to audio. This can be made 
            possible through the command
                :::<span style="color:darkcyan;font-weight:bolder;"> Executed as "> Convert" </span></pre>
    </li>
</ol>



## Usage

First we install the necessary packages using

```python
pip install -r requirements.txt
```

after a successful installation of all the packages we can then run the app using

```python
python3 PyDA-V2.py
```

![Sample PYDA Usage](app/play.gif)

</body>
</html>
