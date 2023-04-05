package Service;

import java.util.List;

import DAO.SocialMediaDAO;
import Model.Account;
import Model.Message;

public class SocialMediaService {
    SocialMediaDAO socialMediaDAO;

    public SocialMediaService(){
        socialMediaDAO = new SocialMediaDAO();
    }

    public SocialMediaService(SocialMediaDAO socialMediaDAO){
        this.socialMediaDAO = socialMediaDAO;
    }

    public Account postRegister(Account account){
        return socialMediaDAO.insertAccount(account);
    }

    public Account postLogin(Account account){
        return socialMediaDAO.login(account);
    }

    public Message addMsg(Message message) {
        return socialMediaDAO.insertMsg(message);
    }

    public List<Message> getAllMsg() {
        return socialMediaDAO.getAllMsg();
    }
    
    public Message getMsgById(int message_id) {
        return socialMediaDAO.getMsgById(message_id);
    }

    // public Message deleteMsgByIdHandler(int id) {
    //     return socialMediaDAO.deleteMsgById(id);
    // }

    public void patchMsgById(int message_id, String message_text) {
        socialMediaDAO.updateMsgById(message_id, message_text);
    }

    public List<Message> getMsgByUserId(int userId) {
        return socialMediaDAO.getMsgByUserId(userId);
    }
}
