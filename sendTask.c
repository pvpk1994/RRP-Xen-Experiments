/****************************************************************
* author: Guangli Dai @RTLab @UH
* Input the density of the task; the wcet of the task; the port and the ip of the server set up.
* This file sets up a client that spawn a task remotely and collect real-time data for the benchmark.
* The program halts automatically after accomplishing certain jobs.
* Usage: compile with "gcc sendTask.c -lrt -o sendTask" in Linux with gcc 6,
*		 or "gcc sendTask.c -lrt -o sendTask" in Mac with clang 11.
* Last modified: Oct 5th, 2019
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
#include <time.h>
#include <inttypes.h>

#define MAXLINE 1024
#define THOUSAND 1000.0
#define MILLION 1000000.0
#define PHASE_MAX 100

void error(char *msg)
{
	perror(msg);
	exit(1);
}

void sendInfo(int conn, char *info, int len)
{
	if( send(conn, info, len, 0) < 0)
	{
		error("ERROR sending messages.");
	}
}
int main(int argc, char *argv[])
{
	if(argc<6)
	{
		printf("Please give the density, wcet, the port number, the IP address and the file name. \n");
		return 0;
	}
	double density = atof(argv[1]);
	double wcet = atof(argv[2]);
	int phase = 1;
	double ddl = wcet / density;
	wcet = wcet/1.5; //to eliminate the influence of inaccuracy of the execute function
	//build the server connection.
	struct sockaddr_in serv_addr;
	struct hostent *server;
	int portno = atoi(argv[3]);

	int sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) 
	    error("ERROR opening socket");
	server = gethostbyname(argv[4]);//set it to the ip address
	FILE *fp;
	fp = fopen(argv[5],"a");

	if (server == NULL) {
	    fprintf(stderr,"ERROR, no such host\n");
	    exit(0);
	}
	bzero((char *) &serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	bcopy((char *)server->h_addr, 
	     (char *)&serv_addr.sin_addr.s_addr,
	     server->h_length);
	serv_addr.sin_port = htons(portno);
	if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0) 
	    error("ERROR connecting");
	char buffer[MAXLINE];
	memset(buffer,0,sizeof(char)*MAXLINE);
	sprintf(buffer, "%f", wcet);
	char recBuffer[MAXLINE];

	struct timespec start_time;
	clock_gettime(CLOCK_REALTIME, &start_time);
	while(1)
	{

		sendInfo(sockfd, buffer, MAXLINE);
		memset(recBuffer, 0, sizeof(recBuffer));
		//judge whether it is done properly
		int n = read(sockfd, recBuffer, MAXLINE);
		if(n<0)
		{
			error("ERROR receiving replies.");
		}
		printf("Reply: %s\n", recBuffer);
		
		struct timespec now;
		clock_gettime(CLOCK_REALTIME, &now);
		double interval = (now.tv_sec - start_time.tv_sec)*THOUSAND + (now.tv_nsec - start_time.tv_nsec)/MILLION;
		if(interval> ddl*phase)
			printf("Job %d fails to meet the deadline %lf while it ends at %lf\n", phase, ddl*phase, interval);
		else
			printf("Job %d meets its deadline %lf and it ends at %lf.\n", phase, ddl*phase, interval);
		fprintf(fp, "%lf,%lf\n", ddl*phase, interval);
		while(interval < phase*ddl)
		{
			clock_gettime(CLOCK_REALTIME, &now);
			interval = (now.tv_sec - start_time.tv_sec)*THOUSAND + (now.tv_nsec - start_time.tv_nsec)/MILLION;
		}
		phase ++;
		if(phase>=PHASE_MAX)
		{
			memset(recBuffer, 0, sizeof(char)*MAXLINE);
			strcpy(recBuffer, "End.\n");
			sendInfo(sockfd, recBuffer, MAXLINE);
			memset(recBuffer, 0, sizeof(recBuffer));
			int n = read(sockfd, recBuffer, MAXLINE);
			printf("Ending message from the server: %s\n", recBuffer);
			break;
		}

	}
	
	fclose(fp);
	close(sockfd);

}
