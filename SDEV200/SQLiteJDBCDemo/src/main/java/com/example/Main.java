package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Main {
    public static void main(String[] args) {
        // The last part (data/example.db) is the relative path to the database.
        String jdbcUrl = "jdbc:sqlite:data/example.db";

        // Make sure to use try with resources so that connections are closed!
        // Create connection object, then create statement object from
        // that connection.
        try (Connection connection = DriverManager.getConnection(jdbcUrl);
                Statement statement = connection.createStatement();) {

            // Create query to get all books, ordered by author
            String query = "SELECT title, author, publication_year FROM Book ORDER BY author;";

            // Execute the query - send it to the database and get results
            ResultSet rs = statement.executeQuery(query);

            // Loop through and print the fetched results
            while (rs.next()) {
                System.out.println("--- BOOK ---");
                System.out.println("Title = " + rs.getString("title"));
                System.out.println("Author = " + rs.getString("author"));
                System.out.println("Published = " + rs.getInt("publication_year"));
                System.out.println("");
            }

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}