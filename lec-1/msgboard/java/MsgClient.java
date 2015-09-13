// CS 6421 - Simple Message Board Client in Java
// T. Wood
// Compile with: javac MsgClient
// Run with:     java MsgClient

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;


public class MsgClient {
    public static void main(String[] args) {

        // Your code here!
	
	Scanner scanner = new Scanner(System.in);
	System.out.print("Enter your host IP address: ");
	String host = scanner.next();

	System.out.print("Enter your host port number: ");
	int  portnum = Integer.parseInt(scanner.next());

	System.out.print("Enter your name: ");
	String name = scanner.next();

	System.out.print("Enter your message: ");
	String msg = scanner.next();


	try {
		//Creates a stream socket and connects it to the specified port number on the named host.
		Socket sock = new Socket(host, portnum);
		// sock must be a Socket object
		PrintWriter out = new PrintWriter(sock.getOutputStream(), true);

		out.println(name);
		out.println(msg);

		out.flush();
		out.close();
		sock.close();
	} catch (IOException e) {
		e.printStackTrace();
	} 
	

    }
}
