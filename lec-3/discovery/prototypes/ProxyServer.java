
/******************************************************************************
 *
 *  CS 6421 - Proxy Conversation Server
 *  Compilation:  javac ProxyServer.java
 *  Execution:    java ProxyServer port
 * 
 ******************************************************************************/
 
import java.net.Socket;
import java.net.ServerSocket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.regex.Pattern;
import java.io.*;



/******************************************************************************
 *
 *    Proxy Server Class
 *
 ******************************************************************************/

public class ProxyServer {
    //constant value 
    //unit this program may resolve
    //ip address of Servers
    //port num of Servers
    
    
    //TODO: implement your get convertion server list function here
    
    /******************************************************************************
     *   GetList function: get convertion service list from discovery server
     ******************************************************************************/
    
    
    
    
    
    

    /******************************************************************************
     *   Function to process requests
     ******************************************************************************/
    public static void process (Socket clientSocket, HashMap<String, String> ServerTable) throws IOException {
        // open up IO streams
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);


        /* read and print the client's request */
        // readLine() blocks until the server receives a new line from client
        String userInput;
        userInput = in.readLine();
        if (userInput == null) {
            System.out.println("Error reading message");
            out.close();
            in.close();
            clientSocket.close();
        }

        System.out.println("Conversion Request from user: " + userInput);
        //--TODO: add your converting functions here, msg = func(userInput);
        
        String[] userInputs = userInput.split(" ");
        
        boolean flag = true;
        try {
            Double.parseDouble(userInputs[2]);
        } catch (Exception ex) {
            flag = false;
        }
        
        String unit1 = "";
        String unit2 = "";
        String res = "No method to convert from " + unit1 + " to " + unit2;	
        //Check the input and call other servers
        if(userInputs.length != 3) {
            out.println("Invalid Data");
            out.close();
            in.close();
            clientSocket.close();
        }else if(flag) {
               System.out.println("Request Conversion Amount: " + userInputs[2]);
               unit1 = userInputs[0];
               unit2 = userInputs[1];
               String data = ServerTable.get(unit1 + ":" + unit2);	
	       if (data == null) { 
		    res = "No method to convert from " + unit1 + " to " + unit2;
		} else {
                    String[] split_data = data.split(" ");
                    String host = split_data[0];
                    int  port = Integer.parseInt(split_data[1]);
                    res = Convertion(host, port, unit1, unit2, userInputs[2]);
		}
	}else {
		res = "Invalid Amount";	
        }
       
        System.out.println(res);
        out.println(res);
        
        // close IO streams, then socket
        out.close();
        in.close();
        clientSocket.close();
    }
    
    /******************************************************************************
     *   Convertion function
     ******************************************************************************/
    public static String Convertion(String host, int port, String unit1, String unit2, String amt) throws IOException{
        System.out.println("Connecting...");
       
        Socket socket;	
        try{
            socket = new Socket(host, port);
        }catch(IOException e){
            System.err.println("Conection Failed!");
            return null;
        }
        
        PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        
        out.println(unit1 + ' ' + unit2 + ' ' + amt);
        
        String output;
        output = in.readLine();
        if(output == null || output.equals("Invalid Input!")){
            System.out.println("!!!"+output);
            System.err.println("Error reading message");
            out.close();
            in.close();
            socket.close();
            return null;
        }

        return output;

    }
    /******************************************************************************
     *   Main Function
     ******************************************************************************/
    
    public static void main(String[] args) throws Exception {

        //check if argument length is invalid
        if(args.length != 1) {
            System.err.println("Usage: java ConvServer port");
            System.exit(-1);
        }
        
        String strIn;
        //read server info from routing table file
        HashMap<String, String> ServerTable = new HashMap<String, String>();
        try{
            BufferedReader reader = new BufferedReader(new FileReader("path.txt"));
            strIn = reader.readLine();
            while(strIn != null){
                String[] split = strIn.split(" ");
                if(split.length != 4){
                    System.err.println("Please input as \"<input> <output> <value>\"");
                    continue;
                }

                String unit1 = split[0];
                String unit2 = split[1];
                String host = split[2];
                int port = Integer.parseInt(split[3]);

                ServerTable.put(unit1 + ':' + unit2, host + " " + split[3]);
                ServerTable.put(unit2 + ':' + unit1, host + " " + split[3]);
                strIn = reader.readLine();
	    }
        System.out.println(ServerTable);
        }catch(FileNotFoundException fnfe){
            System.err.println(fnfe);
        }catch(IOException ioe){
            System.err.println(ioe);
        }
        
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
                process(clientSocket, ServerTable);
            }

        }catch (IOException e) {
            System.err.println("Connection Error");
        }
        System.exit(0);
    }
}
