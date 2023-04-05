package DAO;
import Util.ConnectionUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import Model.Account;
import Model.Message;

public class SocialMediaDAO {

    public Account insertAccount(Account account){
        Connection connection = ConnectionUtil.getConnection();
        try {
            if (account.getPassword().length() < 4 || account.getUsername().length()<1){
                return null;
            }
            String sql = "INSERT INTO Account (username, password) VALUES (?, ?);";

            PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);

            ps.setString(1, account.getUsername());
            ps.setString(2, account.getPassword());
            System.out.println(ps);
            ps.executeUpdate();
            ResultSet pkeyrs = ps.getGeneratedKeys();
            System.out.println("This is the generated keys " + pkeyrs);
            if(pkeyrs.next()){
                int generated_acct_id = pkeyrs.getInt(1);
                System.out.println("in the if statement: " + generated_acct_id);
                // int posted_by = pkeyrs.getInt(2);
                // String message_text = pkeyrs.getString(3);
                // long time_posted = pkeyrs.getLong(4);
                return new Account(generated_acct_id, account.getUsername(), account.getPassword());
            }
        }catch(SQLException e){
            System.out.println(e.getMessage());
        }
        return null;
    }

    public Account login(Account account){
        Connection connection = ConnectionUtil.getConnection();
        try {
            String sql = "SELECT * FROM account WHERE username = ? AND password = ?;";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setString(1, account.getUsername());
            ps.setString(2, account.getPassword());
            System.out.println(ps);
            ResultSet rs = ps.executeQuery();
            System.out.println(rs);
            while(rs.next()){
                Account acct = new Account(
                    rs.getInt("account_id"),
                    rs.getString("username"),
                    rs.getString("password")
                );
                return acct;
            }
        }catch(SQLException e){
            System.out.println(e.getMessage());
        }
        return null;
    }

    public Message insertMsg(Message message){
        System.out.println(message);
        Connection connection = ConnectionUtil.getConnection();
        try {
            if (message.getMessage_text().length() < 1 || message.getMessage_text().length() > 254){
                return null;
            }
            String sql = "INSERT INTO message (posted_by, message_text, time_posted_epoch) VALUES (?, ?, ?);";

            PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
            
            ps.setInt(1, message.getPosted_by());
            ps.setString(2, message.getMessage_text());
            ps.setLong(3, message.getTime_posted_epoch());
            
            System.out.println(ps);
            ps.executeUpdate();
            ResultSet pkeyrs = ps.getGeneratedKeys();
            System.out.println("This is the generated keys " + pkeyrs);
            if(pkeyrs.next()){
                int generated_msg_id = pkeyrs.getInt(1);
                System.out.println("in the if statement: " + generated_msg_id);
                // int posted_by = pkeyrs.getInt(2);
                // String message_text = pkeyrs.getString(3);
                // long time_posted = pkeyrs.getLong(4);
                return new Message(generated_msg_id, message.getPosted_by(), message.getMessage_text(), message.getTime_posted_epoch());
            }
        }catch(SQLException e){
            System.out.println(e.getMessage());
        }
        return null;
    }

    public List<Message> getAllMsg(){
        Connection connection = ConnectionUtil.getConnection();
        List<Message> messages = new ArrayList<>();
        try {
            String sql = "SELECT * FROM message;";

            PreparedStatement ps = connection.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                Message message = new Message(
                    rs.getInt("message_id"),
                    rs.getInt("posted_by"),
                    rs.getString("message_text"),
                    rs.getLong("time_posted_epoch")
                );
                messages.add(message);
            }
        }catch(SQLException e){
            e.printStackTrace();
        }
        System.out.println(messages);
        return messages;
    }

    public Message getMsgById(int id){
        Connection connection = ConnectionUtil.getConnection();
        Message message = new Message();
        try {
            String sql = "SELECT * FROM message WHERE message_id = (?);";

            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if(rs.next()){
                // Message message = new Message(rs.getInt("message_id"), rs.getInt("posted_by"), rs.getString("message_text"), rs.getLong("time_posted_epoch"));
                message.setMessage_id(rs.getInt("message_id"));
                message.setPosted_by(rs.getInt("posted_by"));
                message.setMessage_text(rs.getString("message_text"));
                message.setTime_posted_epoch(rs.getLong("time_posted_epoch"));
                return message;
            }
        }catch(SQLException e){
            e.printStackTrace();
        }
        System.out.println("this shows? " + message);
        return message;
    }

    public void deleteMsgById(int id){
        Connection connection = ConnectionUtil.getConnection();
        try {
            //if(){

            //}else{
                String sql = "DELETE FROM message WHERE message_id = ?;";
                PreparedStatement ps = connection.prepareStatement(sql);
                ps.setInt(1, id);
                ps.executeQuery();
            //}
        }catch(SQLException e){
            e.printStackTrace();
        }
    }

    public void updateMsgById(int id, String message){
        Connection connection = ConnectionUtil.getConnection();
        try {
            //Write SQL logic here
            String sql = "UPDATE message SET message_text = ? WHERE message_id = ?";
            PreparedStatement ps = connection.prepareStatement(sql);

            ps.setString(1, message);
            ps.setInt(2, id);

            ps.executeUpdate();
        }catch(SQLException e){
            System.out.println(e.getMessage());
        }
    }

    public List<Message> getMsgByUserId(int userId){
        Connection connection = ConnectionUtil.getConnection();
        List<Message> messages = new ArrayList<>();
        try {

            String sql = "SELECT * FROM message INNER JOIN account ON message.posted_by = account.account_id WHERE account.account_id = ?;";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1,userId);

            ps.executeQuery();
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                Message message = new Message(rs.getInt("message_id"), rs.getInt("posted_by"), rs.getString("message_text"), rs.getLong("time_posted_epoch"));
                messages.add(message);
            }
        }catch(SQLException e){
            e.printStackTrace();
        }
        return messages;
    }

}
