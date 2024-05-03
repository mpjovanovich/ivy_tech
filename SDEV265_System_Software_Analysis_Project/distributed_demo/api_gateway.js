/*
To test:

curl -X POST -H "Content-Type: application/json" -d '{"message":"I'm the message!"}' http://localhost:3000/calculate
*/

const SERVICE_NAME = process.argv[2] || "api_gateway";
const express = require("express");
const app = express();
const port = 3000;

app.use(express.json());

app.post("/calculate", async (req, res) => {
  // Extract the necessary data from the request body
  const { message } = req.body;

  // Wait to simulate a long running operation
  //   await new Promise((resolve) => setTimeout(resolve, 5000));
  await new Promise((resolve) => setTimeout(resolve, 1));

  // Shuffle the characters in the message
  const shuffledMessage = message
    .split("")
    .sort(() => Math.random() - 0.5)
    .join("");

  // Stringify the shuffled message and service name, and return them
  res.json({ data: shuffledMessage, service: SERVICE_NAME });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
