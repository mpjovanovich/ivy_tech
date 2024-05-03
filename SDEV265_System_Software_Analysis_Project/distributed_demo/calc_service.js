/*
To test:
node calc_service.js 3001 CALC_SERVICE_ALPHA_007
*/
const express = require("express");

// Command line arguments
const PORT = process.argv[2] || 3001;
const SERVICE_NAME = process.argv[3] || "CALC_SERVICE";

// Create an express app
const app = express();
app.use(express.json());

app.post("/calculate", async (req, res) => {
  const { message } = req.body;

  // DEBUG MESSAGE
  console.log(`${SERVICE_NAME} received message: ${message}`);

  // Pretend this is really hard and will take awhile
  await new Promise((resolve) => setTimeout(resolve, 2000));

  // Shuffle the characters in the message
  const shuffledMessage = message
    .split("")
    .sort(() => Math.random() - 0.5)
    .join("");

  // Stringify the shuffled message and service name, and return them
  res.json({ message: shuffledMessage, service: SERVICE_NAME });
});

app.listen(PORT, () => {
  console.log(`${SERVICE_NAME} is running on port ${PORT}`);
});
