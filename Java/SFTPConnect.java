import com.jcraft.jsch.ChannelSftp;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

public class SFTPConnect
{
    public static void main(String[] args)
    {
        String user = "user";
        String password = "password";
        String host = "URL";
        int port = 22;
        boolean usePassword = true;
        File clePrivee; // to initialize
        String pass; // contains either the password or the passphrase

        try
        {
            System.out.println("Establishing Connection...");

            // Using the jsch librairy
            JSch jsch = new JSch();
            // Adding the private key file if the file does exist
            if(clePrivee.exists()) 
            {
                jsch.addIdentity(clePrivee);
                usePassword = false;
                System.out.println("Using the private key file authentication.");
            }
            else
            {
                usePassword = true;
                System.out.println("Using the password authentication.");
            }
            
            // Starting the session
            Session session = jsch.getSession(user, host, port);
            
            session.setConfig("StrictHostKeyChecking", "no");
            session.setConfig("PreferredAuthentications", "publickey,password");
            session.setUserInfo(new UserInfoSSH(usePassword, pass));
            
            session.setPassword(password);
            
            // Try connection
            session.connect();
            System.out.println("Connection established.");

            System.out.println("Creating SFTP Channel.");
            ChannelSftp sftpChannel = (ChannelSftp) session.openChannel("sftp");
            sftpChannel.connect();
            System.out.println("SFTP Channel created.");
            
            // Disconnect the sessions
            sftpChannel.disconnect();
            session.disconnect();
        }
        catch (JSchException e)
        {
            System.out.println(e);
        }
    }
}
