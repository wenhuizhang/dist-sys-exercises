/******************************************************************************
 *
 *  CS 6421 - Simple Conversation
 *  Compilation:  javac ConvServer.java
 *  Execution:    java ConvServer port
 *
 ******************************************************************************/

import java.net.Socket;
import java.net.ServerSocket;
import java.net.UnknownHostException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.*;


/******************************************************************************
 *
 *    Convertion Server Class
 *
 ******************************************************************************/

public class ConvServer {

    public static boolean isNumeric(String str)
    {
          return str.matches("-?\\d+(\\.\\d+)?"); 
    }
    
    //TODO: implement your register function here, incluses add and remove
    
    /******************************************************************************
     *   Function to add and remove from discovery server
     ******************************************************************************/

    
    
    
    /******************************************************************************
     *   Function to process requests
     ******************************************************************************/
    public static void process (Socket clientSocket) throws IOException {
        double index = 0.442;
        String unit1 = "g";
        String unit2 = "b";
        // open up IO streams
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

        /* read and print the client's request */
        // readLine() blocks until the server receives a new line from client
        String userInput;
        String response = "";
        double num;

        if ((userInput = in.readLine()) == null) {
            System.out.println("Error reading message");
            out.close();
            in.close();
            clientSocket.close();
            return;
        }

        System.out.println(userInput);
        //--TODO: add your converting functions here, msg = func(userInput);
        String[] userInputs = userInput.split(" ");

        if (userInputs.length != 3) {
            response = "Invalid Data";
        }else {
            System.out.printf("Conversion Amount: %s\n", userInputs[2]);
            if (isNumeric(userInputs[2])) {
                num = Double.parseDouble(userInputs[2]);
                if(userInputs[0].equals(unit1) && userInputs[1].equals(unit2)) {
                    response = Double.toString(num/index);
                } 
                else if (userInputs[0].equals(unit2) && userInputs[1].equals(unit1)) {
                    response = Double.toString(num*index);
                }
                else {
                    response = "Do not support the conversion from " + userInputs[0] + " to " + userInputs[1]; 
                }
            }
            else {
                response = "Invalid Data";
            }

        }


        System.out.printf("Response: %s\n", response);
        out.println(response);
        // close IO streams, then socket
        out.close();
        in.close();
        clientSocket.close();
    }
    
    
    /******************************************************************************
     *   Main Function
     ******************************************************************************/
    
    public static void main(String[] args) throws Exception {

        //check if argument length is invalid
        if(args.length != 1) {
            System.err.println("Usage: java ConvServer port");
            System.exit(1);
        }
        
        //TODO: add your register code here, add
        
        // create socket
        int port = Integer.parseInt(args[0]);
        ServerSocket serverSocket = new ServerSocket(port);
        System.err.println("Started server on port " + port);

        // wait for connections, and process
        try {
            while(true) {
                // a "blocking" call which waits until a connection is requested
                Socket clientSocket = serverSocket.accept();
                System.err.println("\nAccepted connection from client");
                process(clientSocket);
            }

        }catch (IOException e) {
            System.err.println("Connection Error");
        }
        //TODO: add your unregister code here, remove
        
        serverSocket.close();
        System.exit(0);
    }
}
