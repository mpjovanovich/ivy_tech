package com.example;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class Book {
    // Fields that match our database columns
    private Integer id;
    private String title;
    private String author;
    private Integer publicationYear;

    /****************************************
     * CONSTRUCTOR
     ****************************************/
    // Default constructor
    public Book() {
        // All fields are null by default
    }

    // Constructor for creating a new Book (without an ID yet)
    // We don't set the ID because the database will generate it when we save
    public Book(String title, String author, Integer publicationYear) {
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
    }

    /****************************************
     * GETTERS AND SETTERS
     ****************************************/

    // ID is our primary key.
    // - It will be "null" if the book has not yet been saved to the database.
    // - We have no setId because the database creates the ID when
    // a new record is created. The application should never be allowed to set the
    // ID.
    public Integer getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Integer getPublicationYear() {
        return publicationYear;
    }

    public void setPublicationYear(Integer publicationYear) {
        this.publicationYear = publicationYear;
    }

    // Override the toString method to return a useful string representation
    // of the Book when it's dropped into a print statement
    @Override
    public String toString() {
        return "Book{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", publicationYear=" + publicationYear +
                '}';
    }

    /****************************************
     * DATABASE METHODS - Modify operations
     ****************************************/

    /*
     * Save this book to the database
     * This save is an "upsert" operation.
     * - If the book has no ID, this is a new book
     * - If the book has an ID, this is an update
     */
    public void save() throws SQLException {
        // If there's no ID, this is a new book
        if (this.id == null) {
            // --- INSERT NEW BOOK ---
            String sql = "INSERT INTO Book (title, author, publication_year) VALUES (?, ?, ?)";

            // Get connection and prepare statement
            try (Connection conn = DBManager.getConnection();
                    // The second argument to prepareStatement tells it to return the primary key
                    // for the new record that we inserted.
                    PreparedStatement stmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

                // Set the values in our prepared statement
                stmt.setString(1, this.title);
                stmt.setString(2, this.author);
                stmt.setInt(3, this.publicationYear);

                // Do the insert
                // It will return a value that tells us how many rows were affected
                int rowsAffected = stmt.executeUpdate();

                // If insert worked, get the ID that the database generated
                if (rowsAffected > 0) {
                    try (ResultSet rs = stmt.getGeneratedKeys()) {
                        if (rs.next()) {
                            // Now that the database has generated the ID,
                            // set the generated ID to our object
                            // We normally use the column name, but we have to use the index
                            // when we use getGeneratedKeys()
                            this.id = rs.getInt(1);
                        }
                    }
                }
            }
        } else {
            // --- UPDATE EXISTING BOOK ---
            String sql = "UPDATE Book SET title = ?, author = ?, publication_year = ? WHERE id = ?";

            try (Connection conn = DBManager.getConnection();
                    PreparedStatement stmt = conn.prepareStatement(sql)) {

                // We're not going to bother trying to figure out which fields changed -
                // just update all of them. It's more efficient to do it this way because of
                // the way that prepared statements work.
                stmt.setString(1, this.title);
                stmt.setString(2, this.author);
                stmt.setInt(3, this.publicationYear);
                stmt.setInt(4, this.id); // Use ID in the WHERE clause

                // Do the update
                // We don't care about the number of rows affected, so we're not consuming the
                // result
                stmt.executeUpdate();
            }
        }
    }

    /**
     * Delete this book from the database
     */
    public void delete() throws SQLException {
        // Can only delete if we have an ID
        if (this.id != null) {
            String sql = "DELETE FROM Book WHERE id = ?";

            try (Connection conn = DBManager.getConnection();
                    PreparedStatement stmt = conn.prepareStatement(sql)) {

                // Set the ID to delete
                stmt.setInt(1, this.id);

                // Execute the delete
                stmt.executeUpdate();

                // Clear the ID since it no longer exists in the database
                this.id = null;
            }
        }
    }

    /****************************************
     * DATABASE METHODS - Fetch operations
     ****************************************/
    // These methods are static because they don't need to be associated with a
    // specific instance of a Book - they don't require state.

    /**
     * Fetch a book by its ID
     */
    public static Book fetchById(int id) throws SQLException {
        String sql = "SELECT * FROM Book WHERE id = ?";

        try (Connection conn = DBManager.getConnection();
                PreparedStatement stmt = conn.prepareStatement(sql)) {

            // Set the ID to fetch
            stmt.setInt(1, id);

            // Execute the query
            try (ResultSet rs = stmt.executeQuery()) {
                // If we found a matching book
                if (rs.next()) {
                    // Create a Book object from the database row
                    Book book = new Book();

                    // Each line gets a value from the result set column
                    book.id = rs.getInt("id");
                    book.title = rs.getString("title");
                    book.author = rs.getString("author");
                    book.publicationYear = rs.getInt("publication_year");

                    return book;
                }
            }
        }

        // No book found with that ID
        return null;
    }

    /**
     * Fetch all books in the database
     */
    public static List<Book> fetchAll() throws SQLException {
        List<Book> books = new ArrayList<>();
        String sql = "SELECT * FROM Book";

        try (Connection conn = DBManager.getConnection();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // For each row in the result...
            while (rs.next()) {
                // Create a new Book
                Book book = new Book();

                // Fill the Book with data from this row
                book.id = rs.getInt("id");
                book.title = rs.getString("title");
                book.author = rs.getString("author");
                book.publicationYear = rs.getInt("publication_year");

                // Add to our list
                books.add(book);
            }
        }

        return books;
    }

    /**
     * Fetch books by a specific author
     */
    public static List<Book> fetchByAuthor(String authorName) throws SQLException {
        List<Book> books = new ArrayList<>();
        String sql = "SELECT * FROM Book WHERE author LIKE ?";

        try (Connection conn = DBManager.getConnection();
                PreparedStatement stmt = conn.prepareStatement(sql)) {

            // Use LIKE for partial matches
            stmt.setString(1, "%" + authorName + "%");

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    Book book = new Book();
                    book.id = rs.getInt("id");
                    book.title = rs.getString("title");
                    book.author = rs.getString("author");
                    book.publicationYear = rs.getInt("publication_year");
                    books.add(book);
                }
            }
        }

        return books;
    }
}