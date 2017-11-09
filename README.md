# Setting up the Environment
Prerequisites: ryu, mininet, and behave

For the best results download the Virtual Machine Image with Ryu and Mininet following the steps here https://github.com/osrg/ryu/wiki/OpenFlow_Tutorial 

Once the virtual machine is ready and running it is time to install the Behave function
To do so run the command "pip install behave"
If you have any issues the guide can be found here http://pythonhosted.org/behave/install.html

Once you have all of this downloaded and running it is time to install our code. 
This picture shows how the file structure should be set up

![screenshot 65](https://user-images.githubusercontent.com/25207378/29027615-0bb0d5f4-7b47-11e7-922d-037beca710b5.png)

Once this is done, you are ready to run the code

# Running the Code

First we need to launch mininet to do so we run to prompt "sudo mn --mac --controller remote --switch ovsk"
This will run an instance of mininet with a basic topology and no running controller

If you have a custom topology you can run the command as shown in the picture, I have included our own as an example

![screenshot 68](https://user-images.githubusercontent.com/25207378/29029230-96a5b300-7b4c-11e7-8c07-0bfec353f237.png)

(note: your custom topology files will need to be located in the mininet/custom folder)

Then open up a second terminal window and navigate to either "behave/simple_switch" or "behave/rest_firewall"
Once you are in the folder containing the "steps" folder and a ".feature" file run the command "behave"

![screenshot 71](https://user-images.githubusercontent.com/25207378/29029921-efdd5c78-7b4e-11e7-8f21-f2aee133b25b.png)
(ex: simple_switch)

As you can see now, when you run a pingall test on the mininet network there is now a connection and all packets have been recieved

To exit out of the behave file simply enter "ctrl+c" and for mininet enter ">exit" 


Extra note:
Please remember to put "export BDNM_ROOT=~/bdnm" or in the .bashrc and source it.