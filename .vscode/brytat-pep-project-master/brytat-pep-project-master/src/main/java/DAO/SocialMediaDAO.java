package DAO;
import Util.ConnectionUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import Model.Account;
import Model.Message;

public class SocialMediaDAO {

    public Account insertAccount(Account account){
        Connection connection = ConnectionUtil.getConnection();
        try {
            String sql = "INSERT INTO Account (username, password) VALUES (?, ?);";

            PreparedStatement ps = connection.prepareStatement(sql);

            ps.setString(1, account.getUsername());
            ps.setString(2, account.getPassword());
            ps.executeQuery();
            // while(rs.next()){
            //     Account account = new Account(rs.getInt("flight_id"), rs.getString("departure_city"),
            //             rs.getString("arrival_city"));
            //     account.add(account);
            // }
        }catch(SQLException e){
            e.printStackTrace();
        }
        return account;
    }

    public Account login(Account account){
        Connection connection = ConnectionUtil.getConnection();
        try {
            String sql = "SELECT * FROM account WHERE username = ? && password = ?;";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setString(1, account.getUsername());
            ps.setString(2, account.getPassword());
            ps.executeQuery();
        //     while(rs.next()){
        //         rs.getString("message_body");
        //     }
        }catch(SQLException e){
            e.printStackTrace();
        }
        return account;
    }

    public Message insertMsg(Message message){
        Connection connection = ConnectionUtil.getConnection();
        try {
            String sql = "INSERT INTO message (posted_by, message_text) VALUES (?, ?);";

            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1, message.getPosted_by());
            ps.setString(2, message.getMessage_text());
            ResultSet rs = ps.executeQuery();;
            while(rs.next()){
                int message_id = rs.getInt(1);
                int posted_by = rs.getInt(2);
                String message_text = rs.getString(3);
                long time_posted = rs.getLong(4);
                return new Message(message_id, posted_by, message_text, time_posted);
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
            ps.executeQuery();
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                Message message = new Message();
                messages.add(message);
            }
        }catch(SQLException e){
            e.printStackTrace();
        }
        return messages;
    }

    public List<Message> getAllMsgById(int id){
        Connection connection = ConnectionUtil.getConnection();
        List<Message> messages = new ArrayList<>();
        try {
            String sql = "SELECT * FROM message WHERE message_id = (?);";

            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1, id);
            ps.executeQuery();
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                Message message = new Message();
                messages.add(message);
            }
        }catch(SQLException e){
            e.printStackTrace();
        }
        return messages;
    }

    // public void deleteMsgById(int id){
    //     Connection connection = ConnectionUtil.getConnection();
    //     try {
    //         String sql = "DELETE FROM message WHERE message_id = ?;";
    //         PreparedStatement ps = connection.prepareStatement(sql);
    //         ps.setInt(1, id);
    //         ps.executeQuery();
    //     }catch(SQLException e){
    //         e.printStackTrace();
    //     }
    // }

    // public void updateMsgById(int id){
    //     Connection connection = ConnectionUtil.getConnection();
    //     try {
    //         String sql = "SELECT * FROM Message WHERE message_id = (?);";
    //         PreparedStatement ps = connection.prepareStatement(sql);
    //         ps.setInt(1,id);
    //         ps.executeQuery();
    //     }catch(SQLException e){
    //         e.printStackTrace();
    //     }
    // }

    public List<Message> getMsgByUserId(int userId){
        Connection connection = ConnectionUtil.getConnection();
        List<Message> messages = new ArrayList<>();
        try {

            String sql = "SELECT * FROM Message RIGHT JOIN account ON message.posted_by = account.account_id WHERE account.account_id = ?;";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1,userId);

            ps.executeUpdate();
        }catch(SQLException e){
            e.printStackTrace();
        }
        return messages;
    }

}
