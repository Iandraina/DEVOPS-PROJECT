# DEVOPS PROJECT

## PROJECT
This is an open source project that implements a simple calculator using _python_ and _pytest_ for _unit testing_ without a user interface.
This little project is also using _GITHUB_ & _TRAVIS CI_.

## GITHUB REPOSITORY FOR CLONING THE PROJECT
- Clone the project with the following command line :
   ```$ git clone https://github.com/Iandraina/DEVOPS-PROJECT.git```

## INSTRUCTIONS
### TOOLS
- You need to have python on your computer : 
  [python installation](https://www.python.org/downloads/windows/)

- You have to install _pip_ if it isn't done yet :
  ```$ python get-pip.py```

- You need then to install pytest to be able to run the tests if it isn't done yet : 
  ```pip install -U pytest```

### RUN BUILD
- The build we run automatically wen you launch the project, because this project's repository is build within _Travis CI_.

### RUN DEVELOPMENT
To run the project you have to open your python IDLE and copy past the code and run it
Or if you are using VS Code (Visual Studio Code) :
-     In your console press Ctrl + shift + P (Windows)
-     Change the Command property from "_tsc_" (TypeScript) to "_Python_"
-     Change showOutput from "_silent_" to "_Always_"
-     Change args (Arguments) from ["Helloworld.ts"] to ["${file}"] (filename)
-     Delete the last property problemMatcher
-     Save the changes made


### RUN TEST 
To run the tests you have to open your terminal in your file directory and type the following command line : 
 ```$ pytest```

## PROBLEMS 
- The first issue was _how to use docker in windows_ : a problem that I could not solve
- The lack of time and efficiency made it impossible for me to operate a huge project
- The implementation of tests and the use of travis CI

## COLLABORATORS
- _RAVELOMANANA_ _Iandraina_



