package com.example;

import java.sql.SQLException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            System.out.println("==== Active Record Pattern Example ====");

            // 1. Create a new book (not yet in database)
            System.out.println("\n1. Creating a new book object...");
            Book book = new Book("The Hobbit", "J.R.R. Tolkien", 1937);
            System.out.println("Created: " + book);

            // 2. Save the book to the database
            System.out.println("\n2. Saving book to database...");
            book.save();
            System.out.println("After save: " + book);
            System.out.println("Notice that the book now has an ID!");

            // 3. fetch a book by ID
            System.out.println("\n3. fetching book #" + book.getId() + " from database...");
            Book foundBook = Book.fetchById(book.getId());
            System.out.println("Found: " + foundBook);

            // 4. Update a book
            System.out.println("\n4. Updating book title...");
            foundBook.setTitle("The Hobbit, or There and Back Again");
            foundBook.save();
            System.out.println("After update: " + foundBook);

            // 5. fetch books by author
            System.out.println("\n5. fetching books by author 'Tolkien'...");
            List<Book> tolkienBooks = Book.fetchByAuthor("Tolkien");
            System.out.println("Found " + tolkienBooks.size() + " books");
            for (Book b : tolkienBooks) {
                System.out.println("- " + b);
            }

            // 6. Get all books
            System.out.println("\n6. Listing all books...");
            List<Book> allBooks = Book.fetchAll();
            System.out.println("Total books: " + allBooks.size());
            for (Book b : allBooks) {
                System.out.println("- " + b.toString());
            }

            // 7. Delete a book
            System.out.println("\n7. Deleting book #" + book.getId() + "...");
            book.delete();
            System.out.println("After delete, book ID is: " + book.getId());

        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
