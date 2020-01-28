/****************************************************************
* author: Guangli Dai @RTLab @UH
* Input: A port number the server listens to.
* This file sets up a server that continuously wait for connections for the benchmark test.
* In this version, you need to use Ctrl+C to stop the server after all tests are done.
* Usage: compile with "gcc receiveTask.c -lrt -o recTask" in Linux with gcc 6,
*		 or "gcc receiveTask.c -o recTask" in Mac with clang 11.
* 		 Run it with a port given as the first argument, e.g., ./recTask 2019
* Last modified: Oct 4th, 2019
****************************************************************/

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <fcntl.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<inttypes.h>
#define MILLION  1000000.0
#define THOUSAND 1000.0
#define ONE_ROUND_TIME 3951.595

#define MAXLINE 1024

void error(char *msg)
{
	perror(msg);
	exit(1);
}

//keep the CPU run for wcet milliseconds.
void execute(double wcet)
{
	double end_time = wcet/ONE_ROUND_TIME * 2147483647.0;
	for(int i=0;i<end_time;i++)
		;
	/* //not working in the virtualized system because the clock() is messed up.
	clock_t start, end;
	start = clock();
	while(1)
	{
		end = clock();
		double interval = (end - start)/THOUSAND;
		if(interval>=wcet)
			break;
	}
	*/
}

void sendInfo(int conn, char *info, int len)
{
	if(len>MAXLINE)
	{
		error("ERROR: Too long a message.");
	}
	if(send(conn, info, len, 0)<0)
	{
		error("ERROR sending messages.");
	}
}

int dealRequest(int conn, char* info)
{
	int n = read(conn, info, MAXLINE);
	printf("Received: %s\n", info);
	if(strcmp(info, "End.\n")==0)
	{
		memset(info, 0, MAXLINE*sizeof(char));
		strcpy(info, "Ended.\n");
		sendInfo(conn, info, MAXLINE);
		return 0;
	}
	double exe_time = atof(info);
	//analyze the number and execute 
	clock_t start = clock(), end;
	struct timespec start_t, end_t;
	clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_t);
	execute(exe_time);
	end = clock();
	clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_t);
	double interval = (end - start)/THOUSAND;
	printf("The clock in the domain passes %lf ms.\n", interval);
	interval = (end_t.tv_sec - start_t.tv_sec)*THOUSAND + (end_t.tv_nsec - start_t.tv_nsec)/MILLION;
	printf("gettime shows %lf ms. \n", interval);
	//send a feed back of accomplishments
	memset(info, 0, MAXLINE*sizeof(char));
	strcpy(info, "Done.\n");
	sendInfo(conn, info, MAXLINE);
	return 1;

}

int main(int argc, char *argv[])
{
	if(argc<2)
	{
		printf("Please give the port number.\n");
		return 0;
	}
	//server code
	int newsockfd, clilen;
	int portno = atoi(argv[1]);
	struct sockaddr_in serv_addr, cli_addr;
	int sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) 
		error("ERROR opening socket");
	bzero((char *) &serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(portno);
	int flag = 1;
	if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &flag, sizeof(flag)) < 0) 
		error("ERROR setting sockets.");
	if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
		error("ERROR on binding");
	listen(sockfd,5);
	clilen = sizeof(cli_addr);
	while(1)
	{
		printf("Waiting for next connection.\n");
		newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, (socklen_t *)&clilen);

		//receive the first info
		char buffer[MAXLINE];
		while(1)
		{
			memset(buffer, 0, MAXLINE*sizeof(char));
			if(!dealRequest(newsockfd, buffer))
				break;
		}
		close(newsockfd);
	}

	
}
