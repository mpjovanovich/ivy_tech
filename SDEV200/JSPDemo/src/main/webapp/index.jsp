<!--
Execute with: mvn clean package tomcat7:run
Access with: http://localhost:[port-from-pom]/[path-from-pom]/index.jsp
-->

<!-- This directive tells the JSP engine that we are embedding Java code in the JSP page. 
The code is executed when the page is requested by the client. -->
<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Minimal JSP Demo</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 40px;
        line-height: 1.6;
      }
      .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 5px;
      }
      h1 {
        color: #4a6ea9;
      }
      .demo-box {
        background-color: #f7f7f7;
        border: 1px solid #ddd;
        padding: 15px;
        margin: 15px 0;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Minimal JSP Demo</h1>

      <div class="demo-box">
        <!-- JSP Expressions are used to output the result of an expression
         directly into the response. This is useful when there is no logic
         associated with the output. -->
        <h2>Basic JSP Expression</h2>
        <p>Current server time: <%= new java.util.Date() %></p>
      </div>

      <div class="demo-box">
        <!-- JSP Scriptlets are used to embed Java code into the page. -->
        <h2>JSP Scriptlet</h2>
        <p>
        <% 
            // Plain old Java code...
            String name = request.getParameter("name"); 
            if (name == null || name.isEmpty()) { 
                name = "Guest"; 
            } 
            // In a scriptlet we use out.println() to write content to the response.
            out.println("Hello, " + name + "!"); 
        %>
        </p>
        <p>Try adding ?name=YourName to the URL.</p>
      </div>

        <!-- 
        JSP declarations are used to declare variables and methods with instance scope.
        This means that it will be shared across all requests to the page, even from
        different users. 
        
        Normally this is not a good thing for variables, but it can be useful for methods.
        They will essentially be static methods that can be called from the JSP page.
        -->
        <%! 
            public int add(int a, int b) { 
                return a + b; 
            } 
        %>
      <div class="demo-box">
        <h2>JSP Declaration and Method</h2>
        <p>2 + 3 = <%= add(2, 3) %></p>
      </div>

      <!-- We have access to the request variable, juse as we did with servlets. -->
      <div class="demo-box">
        <h2>Request Information</h2>
        <p>Your IP address: <%= request.getRemoteAddr() %></p>
        <p>Browser: <%= request.getHeader("User-Agent") %></p>
      </div>
    </div>
  </body>
</html>
