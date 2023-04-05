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

    public Account postRegisterHandler(Account account){
        return socialMediaDAO.insertAccount(account);
    }

    public Account postLoginHandler(Account account){
        return socialMediaDAO.login(account);
    }

    public Message addMsg(Message message) {
        return socialMediaDAO.insertMsg(message);
    }

    public List<Message> getAllMsgHandler() {
        return socialMediaDAO.getAllMsg();
    }
    
    public Message getMsgByIdHandler(int message_id) {
        return socialMediaDAO.getMsgById(message_id);
    }

    // public Message deleteMsgByIdHandler(int id) {
    //     return socialMediaDAO.deleteMsgById(id);
    // }

    public void patchMsgByIdHandler(int message_id, String message_text) {
        socialMediaDAO.updateMsgById(message_id, message_text);
    }

    public List<Message> getMsgByUserIdHandler(int userId) {
        return socialMediaDAO.getMsgByUserId(userId);
    }
}
