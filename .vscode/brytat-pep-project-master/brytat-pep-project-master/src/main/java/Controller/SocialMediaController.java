package Controller;

import java.util.List;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import DAO.SocialMediaDAO;
import Model.Account;
import Model.Message;
import Service.SocialMediaService;
import io.javalin.Javalin;
import io.javalin.http.Context;

/**
 * TODO: You will need to write your own endpoints and handlers for your controller. The endpoints you will need can be
 * found in readme.md as well as the test cases. You should
 * refer to prior mini-project labs and lecture materials for guidance on how a controller may be built.
 */
public class SocialMediaController {
    /**
     * In order for the test cases to work, you will need to write the endpoints in the startAPI() method, as the test
     * suite must receive a Javalin object from this method.
     * @return a Javalin app object which defines the behavior of the Javalin controller.
     */
    SocialMediaService socialMediaService;
    public SocialMediaController(){
        socialMediaService = new SocialMediaService();
    }

    public Javalin startAPI() {
        Javalin app = Javalin.create();

        //User Registration
        app.post("/register", this::postRegisterHandler);

        //Login
        app.post("/login", this::postLoginHandler);

        //Create New Message
        app.post("/messages", this::postMsgHandler);

        //Get All Messages
        app.get("/messages", this::getAllMsgHandler);

        //Get One Message Given Message Id
        app.get("/messages/{message_id}", this::getMsgByIdHandler);

        //Delete a Message Given Message Id
        app.delete("/messages/{message_id}", this::deleteMsgByIdHandler);

        //Update Message Given Message Id
        app.patch("/messages/{message_id}", this::patchMsgByIdHandler);

        //Get all messages from user given account
        app.get("/accounts/{account_id}/messages", this::getMsgByUserIdHandler);

        return app;
    }

    /**
     * This is an example handler for an example endpoint.
     * @param context The Javalin Context object manages information about both the HTTP request and response.
     */
    private void postRegisterHandler(Context ctx) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        Account account = mapper.readValue(ctx.body(), Account.class);
        Account addedAcct = socialMediaService.postRegister(account);
        System.out.println(account);
        if(addedAcct==null){
            ctx.status(400);
        }else{
            ctx.json(addedAcct);
        }
    }

    private void postLoginHandler(Context ctx) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        Account account = mapper.readValue(ctx.body(), Account.class);
        Account loggedInAcct = socialMediaService.postLogin(account);
        if(loggedInAcct==null){
            ctx.status(401);
        }else{
            ctx.json(loggedInAcct);
        }
    }

    private void postMsgHandler(Context ctx) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        Message message = mapper.readValue(ctx.body(), Message.class);
        Message addedMessage = socialMediaService.addMsg(message);
        System.out.println(message);
        if(addedMessage==null){
            ctx.status(400);
        }else{
            ctx.json(addedMessage);
        }
    }

    private void getAllMsgHandler(Context ctx) {
        ctx.json(socialMediaService.getAllMsg());
    }
    // updated code!!!!
    private void getMsgByIdHandler(Context ctx) {
        Message message = socialMediaService.getMsgById(Integer.parseInt(ctx.pathParam("message_id")));
        if(message.message_id == 0){
        }else {
            ctx.json(message);
        }
    }

    private void deleteMsgByIdHandler(Context ctx) {
        ctx.json("sample text");
    }

    //THIS TOO!
    private void patchMsgByIdHandler(Context ctx) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        Message message = mapper.readValue(ctx.body(), Message.class);
        int message_id = Integer.parseInt(ctx.pathParam("message_id"));
        if (message.getMessage_text().length() < 1 || message.getMessage_text().length() > 254 || socialMediaService.getMsgById(message_id).message_id == 0) {
            System.out.println("invalid message");
            ctx.status(400);
        } else {
            socialMediaService.patchMsgById(message_id, message.getMessage_text());
            Message ret = socialMediaService.getMsgById(message_id);
            System.out.println(ret);
            ctx.json(ret);
        }
    }

    private void getMsgByUserIdHandler(Context ctx) {
        ctx.json(socialMediaService.getMsgByUserId(Integer.valueOf(ctx.pathParam("account_id"))));
    }
}