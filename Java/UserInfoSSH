import com.jcraft.jsch.UserInfo;

public class UserInfoSSH implements UserInfo
{
    private boolean utiliserMotDePasse;
    private String passwordOuPassphrase;

    /**
     * 
     * @param aUtiliserMotDePasse
     * @param aPasswordOuPassphrase
     */
    public UserInfoSSH(boolean aUtiliserMotDePasse, String aPasswordOuPassphrase)
    {
        super();
        this.utiliserMotDePasse = aUtiliserMotDePasse;
        this.passwordOuPassphrase = aPasswordOuPassphrase;
    }

    @Override
    public String getPassphrase()
    {
        return utiliserMotDePasse ? null : passwordOuPassphrase;
    }

    @Override
    public String getPassword()
    {
        return utiliserMotDePasse ? passwordOuPassphrase : null;
    }

    @Override
    public boolean promptPassphrase(String aArg0)
    {
        return true;
    }

    @Override
    public boolean promptPassword(String aArg0)
    {
        return true;
    }

    @Override
    public boolean promptYesNo(String aArg0)
    {
        return true;
    }

    @Override
    public void showMessage(String aArg0)
    {
    }

}
