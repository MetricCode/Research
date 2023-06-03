
### Managing Docker images

- Downloading a docker image (from docker hub) - `docker pull image_name`
- If the docker image has a tag, we can run `docker pull image_name:tag`
- If we want to manage our docker images present on the machine(e.g remove an image) - `docker image COMMAND`
- To list the present docker images - `docker image ls`
- To remove - `docker image rm IAMGE_ID`

### Running a docker container

Docker containers can be run with various options - depending on how we will use the container. 

- To execute a command - `docker run -it  docker_ID COMMAND`

#### Docker run options

- `-d` - Start the container in detatched mode.(running in the background)
- `-it` - i for interactively. t run a shell.(used to interact with the container itself.)
- `-v` - Volume. Tells the container to mount a directory from the host to a location inside the container.(docker run -v /host/os/directory:/container/directory DOCKER_ID)
- `-p` - Bind a port onto the host from the container. (docker run -p 80:80 webserver )
- `-rm` - Remove the container once done running a command. (docker run --rm helloworld)
- `--name` - This lets us give a container a rememberable name. (docker run --name helloworld)

### Docker list running containers.

- `docker ps` - List current running containers.
- `docker ps -a` - List all current containers even stopped one's.

### DockerFiles

Dockerfiles is a formatted text file which essentially serves as an instruction manual for what containers should do and ultimately assembles a Docker image.

You use Dockerfiles to contain the commands the container should execute when it is built.

__Essential dockerfiles instructions__

![Screenshot from 2023-05-24 22-09-33](https://github.com/MetricCode/MetricCode/assets/99975622/4bc8aa76-543d-44d9-8ac0-e77a7d3159a4)


### Building a docker container...

Once you have your docker file present, we can now build the container.

`docker build -t helloworld .` -t will name the docker image from the dockerfile.

after building the image, we can check for it using `docker image ls`

### Docker compose...

Docker Compose, in summary, allows multiple containers (or applications) to interact with each other when needed while running in isolation from one another.

Docker Compose allows us to create these “microservices” as one singular “service”.

To work with docker compose;

- We need Docker Compose installed (it does not come with Docker by default).
- We need a valid _docker-compose.yml_ file
- A fundamental understanding of using Docker Compose to build and manage containers.

Example of docker-compose commands...

![Screenshot from 2023-05-24 22-27-16](https://github.com/MetricCode/MetricCode/assets/99975622/613e6997-10c2-4a47-a22c-c232cf4a0a23)

Other commands 

![Screenshot from 2023-05-24 22-29-55](https://github.com/MetricCode/MetricCode/assets/99975622/9d36aad4-5a1e-4355-9596-9d388d2b8b11)


Example of a docker-compose.yml file;

This _docker-compose.yml_ file assumes the following:

1. We will run one web server (named web) from the previously mentioned scenario.
2. We will run a database server (named database) from the previously mentioned scenario.
3. The web server is going to be built using its Dockerfile, but we are going to use an already-built image for the database server (MySQL)
4. The containers will be networked to communicate with each other (the network is called ecommerce).
5. Our directory listing looks like the following:
6. docker-compose.yml
7. web/Dockerfile

```
yml
version: '3.3'
services:
  web:
    build: ./web
    networks:
      - ecommerce
    ports:
      - '80:80'


  database:
    image: mysql:latest
    networks:
      - ecommerce
    environment:
      - MYSQL_DATABASE=ecommerce
      - MYSQL_USERNAME=root
      - MYSQL_ROOT_PASSWORD=helloword
    
networks:
  ecommerce:
```

### Docker Socket.

When you install Docker, there are two programs that get installed:

1. The Docker Client
2. The Docker Server

Docker works in a client/server model. 

Docker achieves this communication using something called a socket. Sockets are an essential feature of the operating system that allows data to be communicated.

The program will interact with these two sockets to store or retrieve the data within them! A socket can either be a network connection or what is represented as a file. What's important to know about sockets is that they allow for Interprocess Communication (IPC).

n the context of Docker, the Docker Server is effectively just an API. The Docker Server uses this API to **listen** for requests, whereas the Docker Client uses the API to **send** requests.

For example, let's take this command: `docker run helloworld`. The Docker Client will request the Docker server to run a container using the image "helloworld". Now, whilst this explanation is fairly basic, it is the essential premise of how Docker works.

What's interesting is that because of this, we can interact with the Docker Server using commands like `curl` or an API developer tool such as Postman.

Finally, it's important to note that because of this, the host machine running Docker can be configured to process commands sent from another device. This is an extremely dangerous vulnerability if it is not correctly configured because it means someone can remotely stop, start, and access Docker containers.
