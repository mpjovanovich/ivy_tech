/*
This is the API Gateway service. It is responsible for receiving messages from clients and sending them to the calc services for processing. It uses a simple round-robin algorithm to distribute messages to the calc services.

Example usage:
node api_gateway.js 3000 API_GATEWAY 3001 3002

Example post request:
curl -X POST -H "Content-Type: application/json" -d '{"message":"Yay message!"}' http://localhost:3000/shuffle
*/

// Command line arguments
const PORT = process.argv[2] || 3000;
const SERVICE_NAME = process.argv[3] || "api_gateway";
const CALC_SERVICE_PORTS = process.argv.slice(4).map(Number);

// Array of calc service URLs
const calcServices = CALC_SERVICE_PORTS.map(
  (port) => `http://localhost:${port}`
);

// Create an express app
const axios = require("axios");
const express = require("express");
const app = express();
app.use(express.json());

app.post("/shuffle", async (req, res) => {
  const { message } = req.body;

  // Wait for a calc service to become available
  while (calcServices.length === 0) {
    await new Promise((resolve) => setTimeout(resolve, 1000)); // Wait for 1 second
  }

  // Pop a calc service from the array
  const serviceUrl = calcServices.shift();

  try {
    // For now just log the message
    console.log(
      `${SERVICE_NAME} received message: ${message}. Sending to ${serviceUrl}`
    );

    // Send the message to the calc service for processing
    const response = await axios.post(`${serviceUrl}/calculate`, { message });

    // Send the response back to the client
    res.json(response.data);
  } catch (error) {
    console.error(`Error sending message to calc service: ${error}`);
    res
      .status(500)
      .json({ error: "An error occurred while processing the message." });
  } finally {
    // Add the service back to the array
    calcServices.push(serviceUrl);
  }
});

app.listen(PORT, () => {
  console.log(`${SERVICE_NAME} is running on port ${PORT}`);
});
