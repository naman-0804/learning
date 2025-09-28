import mongoose from "mongoose";

// ✅ Replace with your full connection string and database name
const MONGO_URI = "mongodb+srv://namansrivastava1608:tmUdjxBmfuziAqLb@cluster0.rtdhv.mongodb.net?retryWrites=true&w=majority";

async function testConnection() {
  try {
    console.log("Connecting to MongoDB...");
    await mongoose.connect(MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      serverSelectionTimeoutMS: 10000, // fail faster if unreachable
    });
    console.log("✅ MongoDB connection successful!");

    // Define a small schema and model
    const TestSchema = new mongoose.Schema({ name: String });
    const Test = mongoose.model("Test", TestSchema);

    // Insert a test document
    const doc = new Test({ name: "MongoDB connection works!" });
    await doc.save();
    console.log("✅ Document inserted:", doc);

    // Fetch documents to confirm read
    const docs = await Test.find();
    console.log("✅ Fetched docs:", docs);

    await mongoose.disconnect();
    console.log("🔌 Disconnected successfully");
  } catch (err) {
    console.error("❌ MongoDB connection failed:", err.message);
  }
}

testConnection();
