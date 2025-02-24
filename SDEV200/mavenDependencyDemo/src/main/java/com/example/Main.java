package com.example;

import org.fusesource.jansi.Ansi;
import org.fusesource.jansi.AnsiConsole;

public class Main {
    public static void main(String[] args) {
        AnsiConsole.systemInstall();

        // Rainbow text
        System.out.println(Ansi.ansi().fgRed().a("Hello ").fgYellow().a("colorful ").fgGreen().a("Java!")
                .fgCyan().a(" This ").fgBlue().a("is ").fgMagenta().a("ANSI!").reset());

        AnsiConsole.systemUninstall();
    }
}