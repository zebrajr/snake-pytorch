# Snake with AI
A python (pygame) snake game in a docker (compose) stack to learn and develop Reinforcement Learning technics.


### Running
Before executing the docker stack you need to make sure that the container has permissions to display the window on your local host.

You can do this by executing ``xhost +local:docker``

If you getting an error on the docker stack / still not getting a window, you can use the following command to make sure it's not a permissions issue ``xhost +``.

Due to security issues, you should remove the permissions afterwards ``xhost -``