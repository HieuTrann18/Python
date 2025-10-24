const express = require("express");
const app = express();
require("dotenv").config();
const port = process.env.PORT || 8080;
const cors = require("cors");
const swaggerUi = require("swagger-ui-express");
const swaggerDocument = require("./swagger.json");
const connectDB = require("./config/db");
const authRoutes = require("./routers/auth.routes");
const adminRoutes = require("./routers/admin.routes");

connectDB()
app.use(cors());
app.use(express.json());
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));
app.use("/api/auth", authRoutes)
app.use("/api/admin", adminRoutes)



app.get("/", (req, res) => {
  res.redirect("/api-docs");
});



app.listen(port, () => {
  console.log(`demo on http://localhost:${port}`);
});
