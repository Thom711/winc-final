Winc Academy Final Assignment - CI/CD

## 3 Components
1: The deploy script. This thing is basicly the whole pipeline. It checks out the 
github repo and runs the test suite. It creates a safe login to the server,
copies over the files and then restarts systemctl. All in one file!
2: rsync. Considering there's no packages to install or docker container to build
on the server, a simple file copy will do for this assignment. If the test suite
finishes, the dist folder is copied to the server.
3: ssh. Github needs access to the server somehow. That's where SSH and Github secrets
come in. This allows a remote login into the server to run the commands in the CLI.

## 3 Problems
1: Figuring out how this all works together. I found there to be very little useful 
documentation on how to do this. Most sites and tutorials assume you use Docker or 
have a Node backend setup. It was surprisingly difficult to just find information
on how to copy files via Github Actions.
2: SSH. It took a while to get Github access to the server. I tried a bunch of different
methods (incuding the Appleboy stuff) and this is what ended up working for me.
3: systemctl. I kept getting 'interactive authentication required' when trying to run
the systemctl command. No googling could help me fix it. What ended up working was
ssh'ing into the server from the server and running it via sudo. Somehow.

## Optional
I think this assignment could have been a lot better / more fun with just a little bit
more of handholding. This is very difficult stuff and we're just let loose like
'go figure it out'. I know this is how it works in the real world, but still. I found
this to be a bit too much of 'in het diepe gegooid worden'.
