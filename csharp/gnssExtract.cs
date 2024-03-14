using System;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;
using MongoDB.Bson;
using MongoDB.Driver;

class Program
{
    static void Main(string[] args)
    {
        // Replace the connection string and database/collection names with your actual details
        string connectionString = "mongodb://localhost:27017";
        string databaseName = "ads_passenger_processed";
        string collectionName = "ads_passenger_processed";

        var topics = new List<string>();

        topics.Add("/apollo/localization/pose");
        topics.Add("/apollo/sensor/gnss/gnss_status");
        topics.Add("/apollo/sensor/gnss/ins_status");
        topics.Add("/apollo/sensor/gnss/best_pose");
        topics.Add("/apollo/sensor/gnss/corrected_imu");
        topics.Add("/apollo/sensor/gnss/ins_stat");
        topics.Add("/apollo/sensor/gnss/rtk_eph");
        topics.Add("/apollo/sensor/gnss/rtk_obs");
        topics.Add("/apollo/sensor/gnss/heading");
        topics.Add("/apollo/sensor/gnss/imu");
        topics.Add("/apollo/sensor/gnss/odometry");
        topics.Add("/apollo/sensor/gnss/stream_status");
        topics.Add("/apollo/sensor/gnss/raw_data");
        topics.Add("/apollo/sensor/gnss/rtcm_data");

        // Establishing connection to MongoDB server
        MongoClient client = new MongoClient(connectionString);
        IMongoDatabase database = client.GetDatabase(databaseName);
        IMongoCollection<BsonDocument> collection = database.GetCollection<BsonDocument>(collectionName);

        foreach (var topic in topics)
            {
            // Define the query filter with multiple conditions
            var filter = Builders<BsonDocument>.Filter.Eq("topic", topic);
            var documents = collection.Find(filter).ToList();
        
            // Displaying the retrieved documents
            string[] words = topic.Split('/');

            string jsonFilePath = "json_out/" + words.Last() + ".json";

                using (StreamWriter file = File.CreateText(jsonFilePath))
                {
                    // Serialize each document individually to JSON with formatting and write to the file
                    foreach (var document in documents)
                    {
                        string json = document.ToJson(new MongoDB.Bson.IO.JsonWriterSettings { Indent = true });
                        file.WriteLine(json);
                    }
                }


            Console.WriteLine($"Data dumped to '{jsonFilePath}'.");
        }
    }
}