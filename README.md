if you are creating CloudFormation template for many customers, it is important to keep the template 
static and have the customers update the parameter store or the parameterblock on the teplate to suit 
the region they are working in. Of course the ami's,keypairs,subnet Ids wouldn't be the same, (jsut to name a few)

In this pipeline, your customer doesnt need to update or touch the template but they need to go to the 
parameter store to update the template

I checked in my template in github but you can use any repository of your choice.
The idea is for a pipeline to be triggered from the checking into Github and this is possible by a logic which is configured
in Jenkins which in turn will create a cfn stack and provide all the resources specified in your cfn template.

A jenkins image is pulled on the container which is in turn installed on
an Ubuntu EC2 instance 

here is the template tell me how this goes.Try creating the pipeline, doing first deployment and 
commiting changes on that same code and see if your pipeline triggers a build.

Rem to install aws cli on the container that you install jenkins

install docker on ubuntu 22 and pull a jenkins image.then run a container
creating a directory where you will mount your data incase you restart yout 
container


1.install from official repo or from default repository
https://cloudchamp.notion.site/How-to-Install-Docker-on-Ubuntu-20-f6cda544c64f44ccb83443f8204b098e

#Download Dependencies
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
#Adding Docker GPG kEY
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#install docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
#install latest Docker, start by updating again
sudo apt update
docker
#verify installation
#enable docker service
sudo systemctl start docker(to start docker service)
sudo systemctl enable docker (enable docker run at startup)
#check if service is running
sudo service docker status


Installing docker from default repo
#update repo
sudo apt update
#uninstall old versions of Docker
sudo apt-get remove docker docker-engine docker.io
# install docker
sudo apt install docker.io
#check installation
docker --version
suod service docker status


if not running
sudo service docker start
2.Pull jenkins image from dockerhub(you must have a dockerhub account)
4. sudo docker image ls (to check if image was pulled)
5. create the directory to store the containers data in case you restart container 
your data will remain safe).
mkdir /var/jenkins_home/
# remember to give it permissions 
sudo chmod 777 /var/jenkins_home/ -R (bc docker has to write to this directory -R is for recursive)
ls
6.  docker container ls
 cd /var/jenkins_home/
 docker container ls (copy the container image)
 docker logs -f contianerimageID 
copy the initial password and open the jenkins in your browser and use the password

docker run -p 8080:8080 -d -v /var/jenkins_home:/var/jenkins_home jenkins/jenkins

note: on your instance sg donot forget to open the port for jenkins (ICMP, 8080)


