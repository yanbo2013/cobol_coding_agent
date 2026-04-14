       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.
       AUTHOR. COBOL-EXPERT.
       DATE-WRITTEN. 2023-10-27.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. ANY.
       OBJECT-COMPUTER. ANY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       *> Definition of the greeting message
       01 WS-HELLO-MESSAGE.
           05 WS-TEXT PIC X(12) VALUE 'Hello World!'.

       PROCEDURE DIVISION.
       *> Main execution routine
       0000-START-UP.
           DISPLAY WS-TEXT.
           STOP RUN.