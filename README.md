# Pass-fail determination
This is a simple `python-html` project based on python-based web technology `Flask`. The project aims to determine state of performance of a candidate whether he has failed or passed on the basis of his/her marks obtained in four subjects **Science, Maths, C Programming and Data science**. 
## Dependencies
    pip install -r requirements.txt
## Arguments
    .\directory> python app.py --help
    usage: app.py [-h] [-p PASSING_MARKS]

    Form for pass-fail determination

    optional arguments:
      -h, --help            show this help message and exit
      -p PASSING_MARKS, --passing_marks PASSING_MARKS
                            The marks determining pass or fail
## Execute
    .\directory> python app.py -p 40
## Output
- By running the code a url similar to http://127.0.0.1:5000/ will be generated.
- By copying and pasting the url to browser a page like below will be generated ![image1](https://github.com/SohamChattopadhyayEE/Pass-fail-determination/blob/main/pictures/Screenshot%20(33).png)
- In the page the user has to give his/her marks and has to press the `Submit` button.
- On pressing the `Submit` button, current page will be redirected to the page `./show_results`.
- There the average score of the user will be mentined and based on the passing marks the passing status of the user will be determined.
- ![pass](https://github.com/SohamChattopadhyayEE/Pass-fail-determination/blob/main/pictures/Slide1.JPG) ![fail](https://github.com/SohamChattopadhyayEE/Pass-fail-determination/blob/main/pictures/Slide2.JPG)
