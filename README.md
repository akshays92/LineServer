# Line Server
The following questions are answered in the readme.md

  - How does the system work?
  - What is needed to build the system?
  - How will the system perform with a 1gb, 10GB and a 100gb text file?
  - How will the system perform with 100 users, 10000 users and 1000000 users?
  - What documentation, papers and websites were consulted doing this project?
  - What 3rd party libraries and tools does the system use ? Why did I choose these libraries and frameworks ?
  - How long did I spend on this project ? If I had unlimited time, how would I spend it and prioritize each item ?
  - If I had to critique my code, what would I say about it ?

### How does the system work?

  - The system is basically divided in 3 different parts :
    1) build.sh : which basically installs the necessary dependencies and sets up the environment for the solution to be deployed and work
    2) run.sh filename : indexes the data in the file passed as the parameter linewise into a aws hosted free tier mongo DB database and starts the flask server
    3) server_v1.py : starts the rest server which interacts with the mongoDB database collection and returns results or appropriate error code as stated in the Line Server Interview Problem - Architect.pdf file
- The system indexes all the lines of the file in a collection in mongoDB along with their line nunmber. This is required to be done only once everytime the file is changed. 
- Next the flask rest server hits the database with the line number obtained as the get parameter and gets the appropriate line from the database and returns it (or returns the appropriate error code with message)

### What is needed to build the system?
- A linux system with python 3.x and sudo access (code doesnot implement virtual box yet!!) is required to build the system. 
- you can deploy and run the code with the help of the following commands:
    > git clone https://github.com/akshays92/LineServer.git
    > cd LineServer/
    > sh build.sh (enter password for sudo access if prompted)
    > sh run.sh filename
- this gets the file indexed and starts the REST server when the while file is indexed in the MongoDB

### How will the system perform with a 1gb, 10GB and a 100gb text file?
The design of the system is highly scalable in terms of the file size. As the size of the input file increases, the time to index the file also increases linearly but the time for read lines with  given the line number is of the order of O(Log(N)). To improve the performance further, we can use elastic search to index the data which has an amortized performance of O(1) search time while keeping the indexing performance of O(N). Since it is easy to scale MongoDB horizontally, I have selected Mongo DB to index the file in the database.

### How will the system perform with 100 users, 10000 users and 1000000 users?
As the number of users hitting the API increase, this system is bound to fail. But the design of the system is such that it can be scalled up easily without a lot of reprogramming. We can spin up multiple instances of dockers in different machines running our REST server which are interacting with the same instance of MongoDB. This tecnique will require a load balancer and some form of caching will also be useful. The database and the REST server are kept on different machines as an additional measure for security and scalibility.

### What documentation, papers and websites were consulted doing this project?
- I have referenced the documentation for MongoDB and MLabs. 
- python documentation for FLASK and pymongo 
- some google searches for basic shell scripting to make the build.sh file

### What 3rd party libraries and tools does the system use ? Why did I choose these libraries and frameworks ?
- The project is coded in Python 3 as it was suggested in the requirements document obtained.
- I have used MongoDB because it is easy to code with on python because of its rich documentation and community support 
- One of the other reason to use Mongo was that it is highly scalable (one of the questions answered above on the increase in the size of the file)
- I have used flask for creating the REST server because it doesnot have a lot of boiler plate code and is easy to setup and get goining on flask
- I have also used pickle to store the credentials on the database and other metadata on a file in the system so that it is easy to change them if required.

### How long did I spend on this project ? If I had unlimited time, how would I spend it and prioritize each item ?
- I spend about 2 hours researching on the question and coming up with a design.
- After that, I spent about 6-8 hours coding the system and optimizing the code.
- 1-2 hours coming up with the readme and other documentation
- If I had unlimited time to work on this project, I would spend more time in researching and designing a system which would be more easy to scale and runs faster and spend more time in implementing security of the credentials. Both these tasks will take up equal priority in the case of unlimited time / resuouces with me.

### If I had to critique my code, what would I say about it ?
1) Currently each time the run.sh is called it drops the existing collection in the database and creats a new one with the file provided. The System should check if the file provided in the parameters is the one indexed in the database by keeping its hash in some metadata file. If the hashes are the same, just skip the indexing part and start the REST server directly.
2) ALso the code currently indexws the lines in the file in a one-by-one fashion. MongoDB provides a BULK insert API which should have been used in this system to make the process of indexing faster.

