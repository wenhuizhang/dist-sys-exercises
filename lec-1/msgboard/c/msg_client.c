// CS 6421 - Simple Message Board Client in C
// T. Wood
// Compile with: gcc msg_client -o msg_client
// Run with:     ./msg_client

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <inttypes.h>
#include <string.h>
#include <stdint.h>
#include <stdarg.h>
#include <errno.h>
#include <getopt.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/queue.h>
#include <netinet/in.h>
#include <netdb.h>


static char* server_port = "5555";
static char* server_ip;
static char* name;
static char* message;

/*
 * Print a usage message
 */
static void
usage(const char* progname) {
    printf("Usage: %s ", progname);
    printf("	  	-h : your host ip address \n");
    printf("       	-p : your host port number\n");
    printf("       	-n : your name \n");
    printf("       	-m : your message\n");
    printf("\n\n");
}



/*
 * Parse the application arguments.
 */
static int
parse_app_args(int argc, char* argv[]) {
    const char* progname = argv[0];
    int c;
    
    opterr = 0;
    
    while ((c = getopt (argc, argv, "h:p:n:m:")) != -1)
    switch (c) {
        case 'h':
            server_ip = optarg;
            break;
        case 'p':
            server_port = optarg;
            break;
        case 'n':
            name = optarg;
            break;
        case 'm':
            message = optarg;
            break;
        default:
            usage(progname);
    }
    return optind;
}




int main(int argc, char ** argv)
{
	int rc;
	struct addrinfo hints, *server;
    
	if (parse_app_args(argc, argv) < 0){
        	printf("Invalid command-line arguments\n");
    	}

	memset(&hints, 0, sizeof hints);
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;

	if ((rc = getaddrinfo(server_ip, server_port, &hints, &server)) != 0) {
		perror(gai_strerror(rc));
		exit(-1);
	}


	int sockfd = socket(server->ai_family, server->ai_socktype, server->ai_protocol);
	if (sockfd == -1) {
		perror("ERROR opening socket");
		exit(-1);
	}
	
	rc = connect(sockfd, server->ai_addr, server->ai_addrlen);
	if (rc == -1) {
		perror("ERROR on connect");
		close(sockfd);
		exit(-1);
	}

    
	rc = send(sockfd, name, strlen(name)+1, 0);
        if(rc < 0) {
        	perror("ERROR on send name");
        	exit(-1);
    	}

	rc = send(sockfd, "\n", strlen("\n")+1, 0);
    	if(rc < 0) {
        	perror("ERROR on send message");
        	exit(-1);
    	}

    	rc = send(sockfd, message, strlen(message)+1, 0);
    	if(rc < 0) {
        	perror("ERROR on send message");
        	exit(-1);
    	}
    
    	
    	freeaddrinfo(server);
    	close(sockfd);

    	printf("Done.\n");
    	return 0;
    
}
